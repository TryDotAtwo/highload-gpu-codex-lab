"""Helper tests use Python subprocess fixtures, never pretend these are Lean runs."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import lean_evidence as evidence


class ParserTests(unittest.TestCase):
    def test_real_output_shapes(self):
        log = ("'QuantumGraph.swapProgram_length' does not depend on any axioms\r\n"
               "'QuantumGraph.cnotDistance_symm' depends on axioms: [propext,\n"
               " Classical.choice, Quot.sound]\n")
        parsed = evidence.parse_axioms(log, {"QuantumGraph.swapProgram_length", "QuantumGraph.cnotDistance_symm"})
        self.assertEqual(parsed["QuantumGraph.swapProgram_length"], [])
        self.assertEqual(set(parsed["QuantumGraph.cnotDistance_symm"]), evidence.ALLOWED_AXIOMS)

    def test_unicode_names_color_and_empty_list(self):
        parsed = evidence.parse_axioms("\x1b[32m'A.«имя с пробелом»' depends on axioms: []\x1b[0m\n",
                                       {"A.«имя с пробелом»"})
        self.assertEqual(parsed, {"A.«имя с пробелом»": []})

    def test_missing_not_accepted(self):
        with self.assertRaisesRegex(ValueError, "Missing"):
            evidence.parse_axioms("Build completed successfully (8947 jobs).", {"A"})

    def test_empty_required_list_not_accepted(self):
        with self.assertRaisesRegex(ValueError, "empty"):
            evidence.parse_axioms("", set())

    def test_all_reported_axioms_are_checked(self):
        for ax in ("sorryAx", "Lean.ofReduceBool", "MyAssumption"):
            with self.subTest(axiom=ax), self.assertRaisesRegex(ValueError, "Disallowed"):
                evidence.parse_axioms("'A' depends on axioms: []\n'Extra' depends on axioms: [" + ax + "]", {"A"})

    def test_duplicate_results_fail(self):
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            evidence.parse_axioms("'A' depends on axioms: []\n'A' does not depend on any axioms", {"A"})

    def test_malformed_output_fails(self):
        for log in ("'A' depends on axioms: [propext,]", "'A' depends on axioms: [propext",
                    "'A' does not depend on any axioms\n'Extra' depends on axioms: broken"):
            with self.subTest(log=log), self.assertRaises(ValueError):
                evidence.parse_axioms(log, {"A"})


class RecordTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="lean evidence ")
        self.root = Path(self.temp.name).resolve()
        self.project = self.root / "project with spaces"
        self.project.mkdir()
        (self.project / "Proof.lean").write_text("theorem t : True := True.intro\n", encoding="utf-8")
        (self.project / "expected.txt").write_text("A\n", encoding="utf-8")
        self.inputs = ["Proof.lean", "expected.txt"]

    def tearDown(self):
        self.temp.cleanup()

    def run_fixture(self, kind, code="print('fixture')", suffix=""):
        out = self.root / (kind + suffix)
        evidence.record(self.project, out, self.inputs, kind, [sys.executable, "-c", code])
        return out / "run.json"

    def pair(self):
        return (self.run_fixture("build"), self.run_fixture("axioms",
                'print("\'A\' does not depend on any axioms")'))

    def test_unchanged_evidence_passes(self):
        build, ax = self.pair()
        result = evidence.audit(self.project, build, ax, "expected.txt")
        self.assertEqual(result["required_declarations"], 1)
        self.assertEqual(result["evidence_checks"], "passed")

    def test_failed_process_retains_logs_and_is_rejected(self):
        build = self.run_fixture("build", "import sys; print('partial'); print('failure', file=sys.stderr); sys.exit(7)")
        ax = self.run_fixture("axioms", 'print("\'A\' depends on axioms: []")')
        self.assertEqual(json.loads(build.read_text(encoding="utf-8"))["returncode"], 7)
        self.assertIn("failure", (build.parent / "stderr.log").read_text())
        with self.assertRaisesRegex(ValueError, "did not succeed"):
            evidence.audit(self.project, build, ax, "expected.txt")

    def test_source_change_after_run_fails(self):
        build, ax = self.pair()
        (self.project / "Proof.lean").write_text("changed\n")
        with self.assertRaisesRegex(ValueError, "Current inputs"):
            evidence.audit(self.project, build, ax, "expected.txt")

    def test_source_change_during_run_fails(self):
        build = self.run_fixture("build", "from pathlib import Path; Path('Proof.lean').write_text('changed')")
        ax = self.run_fixture("axioms", 'print("\'A\' depends on axioms: []")')
        with self.assertRaisesRegex(ValueError, "during"):
            evidence.audit(self.project, build, ax, "expected.txt")

    def test_log_tamper_fails(self):
        build, ax = self.pair()
        (ax.parent / "stdout.log").write_text("'A' depends on axioms: []\n")
        with self.assertRaisesRegex(ValueError, "Log hash"):
            evidence.audit(self.project, build, ax, "expected.txt")

    def test_list_must_be_in_snapshot(self):
        self.inputs = ["Proof.lean"]
        build, ax = self.pair()
        with self.assertRaisesRegex(ValueError, "not included"):
            evidence.audit(self.project, build, ax, "expected.txt")

    def test_different_input_selection_fails(self):
        build = self.run_fixture("build")
        self.inputs = ["Proof.lean"]
        ax = self.run_fixture("axioms", 'print("\'A\' depends on axioms: []")')
        with self.assertRaisesRegex(ValueError, "different input"):
            evidence.audit(self.project, build, ax, "expected.txt")

    def test_record_does_not_overwrite(self):
        self.run_fixture("build")
        with self.assertRaises(FileExistsError):
            self.run_fixture("build")

    def test_missing_executable_retains_failure_record(self):
        out = self.root / "spawn-error"
        result = evidence.record(self.project, out, self.inputs, "build",
                                 [str(self.root / "no-such-executable")])
        self.assertIsNone(result["returncode"])
        self.assertTrue((out / "run.json").is_file())
        with self.assertRaisesRegex(ValueError, "did not succeed"):
            evidence.load_run(out / "run.json", self.project, "build")

    def test_duplicate_required_declaration_rejected(self):
        (self.project / "expected.txt").write_text("A\nA\n", encoding="utf-8")
        build, ax = self.pair()
        with self.assertRaisesRegex(ValueError, "Duplicate declaration"):
            evidence.audit(self.project, build, ax, "expected.txt")

    def test_escape_and_self_recording_rejected(self):
        with self.assertRaisesRegex(ValueError, "leaves declared root"):
            evidence.snapshot(self.project, ["../outside"])
        with self.assertRaisesRegex(ValueError, "Evidence output"):
            evidence.record(self.project, self.project / "evidence", ["."], "build", [sys.executable, "-V"])

    def test_added_file_under_directory_invalidates(self):
        self.inputs = ["."]
        build, ax = self.pair()
        (self.project / "New.lean").write_text("new")
        with self.assertRaisesRegex(ValueError, "Current inputs"):
            evidence.audit(self.project, build, ax, "expected.txt")

    def test_cli_propagates_failure_without_shell(self):
        command = [sys.executable, str(Path(evidence.__file__).resolve()), "record", "--project",
                   str(self.project), "--out", str(self.root / "cli"), "--kind", "probe",
                   "--input", "Proof.lean", "--", sys.executable, "-c", "import sys; sys.exit(7)"]
        completed = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(completed.returncode, 7, completed.stderr)
        self.assertEqual(json.loads(completed.stdout)["returncode"], 7)


class CoverageTests(unittest.TestCase):
    def test_history_counts_do_not_become_independent_results(self):
        with tempfile.TemporaryDirectory() as tmp:
            file = Path(tmp) / "ledger.json"
            rows = [{"key": "history", "historical": True, "review_status": "kernel_verified",
                     "exact_statement": "True", "lean_declarations": ["A"],
                     "build_evidence": "passed", "axiom_evidence": "passed"},
                    {"key": "current", "historical": False, "review_status": "unreviewed"}]
            file.write_text(json.dumps({"claims": rows}))
            report = evidence.coverage(file)
            self.assertEqual(report["recorded_statuses"]["historical"]["kernel_verified"], 1)
            self.assertEqual(report["recorded_statuses"]["current"]["unreviewed"], 1)
            self.assertEqual(report["accepted_records_with_free_text_evidence"], ["history"])
            rows.append(rows[0])
            file.write_text(json.dumps({"claims": rows}))
            with self.assertRaisesRegex(ValueError, "duplicate"):
                evidence.coverage(file)


if __name__ == "__main__":
    unittest.main(verbosity=2)
