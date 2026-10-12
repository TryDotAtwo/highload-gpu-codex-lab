import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


def module(name):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).parents[1] / "scripts" / f"{name}.py")
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


manifest = module("verify_manifest")
usage = module("inspect_skill_usage")
snapshot = module("project_snapshot")


class Helpers(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.root = Path(self.directory.name)
        (self.root / "a.bin").write_bytes(b"abc")
        self.entry = {"bytes": 3, "sha256": hashlib.sha256(b"abc").hexdigest()}

    def tearDown(self):
        self.directory.cleanup()

    def test_bytes_and_corruption(self):
        spec = {"files": {"a.bin": self.entry}}
        self.assertTrue(manifest.verify(self.root, spec)["byte_verification_passed"])
        (self.root / "a.bin").write_bytes(b"abd")
        self.assertFalse(manifest.verify(self.root, spec)["byte_verification_passed"])

    def test_missing_unsafe_size_and_hash(self):
        for path in ("missing", "../a.bin", "/a.bin", "C:/a.bin", "./a.bin", "a.bin:stream"):
            with self.subTest(path=path):
                self.assertFalse(manifest.verify(self.root, {"files": {path: self.entry}})["byte_verification_passed"])
        for entry in ({"bytes": 4, "sha256": self.entry["sha256"]}, {"bytes": True, "sha256": "z" * 64}):
            self.assertFalse(manifest.verify(self.root, {"files": {"a.bin": entry}})["byte_verification_passed"])

    def test_empty_or_duplicate_manifest(self):
        with self.assertRaises(ValueError):
            manifest.verify(self.root, {"files": {}})
        path = self.root / "manifest.json"
        path.write_text('{"files": {}, "files": {}}', encoding="utf-8")
        with self.assertRaises(ValueError):
            manifest.load_manifest(path)

    def test_link_escape(self):
        link = self.root / "link"
        try:
            link.symlink_to(self.root / "a.bin")
        except OSError:
            self.skipTest("symlink creation unavailable on this host")
        self.assertFalse(manifest.verify(self.root, {"files": {"link": self.entry}})["byte_verification_passed"])

    def test_reads_not_catalog_or_mentions(self):
        events = [
            {"type": "turn_context", "payload": {"text": "Get-Content '/skills/fake/SKILL.md'"}},
            {"type": "response_item", "payload": {"type": "message", "text": "Read fake SKILL.md"}},
            {"type": "response_item", "timestamp": "2026-09-24T08:28:37Z", "payload": {
                "type": "function_call", "name": "functions.exec", "arguments":
                'text(await tools.exec_command({cmd:"Get-Content -LiteralPath \'C:\\\\Users\\\\private\\\\work-with-molab\\\\SKILL.md\'"}));'}},
            {"type": "response_item", "payload": {"type": "function_call", "name": "exec_command",
                "arguments": json.dumps({"cmd": "Write-Output 'please read /fake/SKILL.md'"})}},
        ]
        path = self.root / "session.jsonl"
        path.write_text("\n".join(json.dumps(e) for e in events) + "\n{partial", encoding="utf-8")
        result = usage.inspect_session(path)
        self.assertEqual([r["skill"] for r in result["skill_read_requests"]], ["work-with-molab"])
        self.assertEqual(result["malformed_lines"], 1)
        self.assertNotIn("private", json.dumps(result))
        self.assertEqual(result["instruction_application"], "not_proven_by_read_requests")

    def test_snapshot_does_not_promote_pass_or_dump_strings(self):
        (self.root / "reports").mkdir()
        (self.root / "reports/brain_rocket_diagnostic.json").write_text(
            json.dumps({"passed": True, "secret": "do-not-print"}), encoding="utf-8")
        result = snapshot.snapshot(self.root)
        self.assertEqual(result["goal_assessment"], "not_performed")
        self.assertNotIn("do-not-print", json.dumps(result))
        row = next(r for r in result["files"] if r["path"].endswith("brain_rocket_diagnostic.json"))
        self.assertEqual(row["reported_fields_unverified"], {"passed": True})


if __name__ == "__main__":
    unittest.main()
