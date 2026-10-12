"""Record explicit commands and check Lean evidence. Standard library, Python 3.11+."""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import stat
import subprocess
import sys

ALLOWED_AXIOMS = frozenset({"propext", "Classical.choice", "Quot.sound"})
STATUSES = frozenset({"unreviewed", "specified", "in_progress", "kernel_verified",
                     "refuted", "experiment_only", "source_gap", "superseded", "open"})
RESULT = re.compile(
    r"^'(?P<name>[^'\r\n]+)' (?:depends on axioms: \[(?P<axioms>[^\]]*)\]"
    r"|does not depend on any axioms)[ \t]*\r?$", re.MULTILINE)
COLOR = re.compile(r"\x1b\[[0-9;]*m")


def fail(message: str) -> None:
    raise ValueError(message)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def within(root: Path, name: str) -> Path:
    path = (root / name).resolve()
    if not path.is_relative_to(root.resolve()):
        fail(f"Path leaves declared root: {name}")
    return path


def reject_link(path: Path) -> None:
    info = path.lstat()
    if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 0x400:
        fail(f"Symlink/reparse-point input is unsupported: {path}")


def input_files(path: Path):
    reject_link(path)
    if path.is_file():
        yield path
    elif path.is_dir():
        for child in sorted(path.iterdir()):
            yield from input_files(child)
    else:
        fail(f"Input is not a regular file/directory: {path}")


def snapshot(project: Path, inputs: list[str]) -> dict[str, str]:
    """Hash all files under explicit inputs, rejecting escapes and empty selections."""
    hashes: dict[str, str] = {}
    for entry in inputs:
        raw = project / entry
        # Check every named component before resolve() can hide a link.
        if raw.exists():
            for parent in (raw, *raw.parents):
                if parent == project.parent:
                    break
                reject_link(parent)
        path = within(project, entry)
        if not path.exists():
            fail(f"Missing input: {entry}")
        for file in input_files(path):
            resolved = file.resolve()
            if not resolved.is_relative_to(project):
                fail(f"Input leaves project: {file}")
            hashes[resolved.relative_to(project).as_posix()] = digest(file)
    if not hashes:
        fail("Input selection contains no files")
    return dict(sorted(hashes.items()))


def record(project: Path, out: Path, inputs: list[str], kind: str,
           command: list[str]) -> dict:
    project, out = project.resolve(), out.resolve()
    if not command:
        fail("Supply an executable and argv after --")
    if not project.is_dir():
        fail("Project directory does not exist")
    for name in inputs:
        selected = within(project, name)
        if selected.is_dir() and out.is_relative_to(selected):
            fail("Evidence output must not be inside a selected input directory")
    before = snapshot(project, inputs)
    out.mkdir(parents=True, exist_ok=False)
    result = {"schema": 1, "kind": kind, "project": str(project), "argv": command,
              "started_utc": utc_now(), "inputs": inputs, "before": before}
    try:
        with (out / "stdout.log").open("wb") as stdout, (out / "stderr.log").open("wb") as stderr:
            completed = subprocess.run(command, cwd=project, stdout=stdout, stderr=stderr,
                                       shell=False, check=False)
        result["returncode"] = completed.returncode
    except OSError as exc:
        result["returncode"] = None
        result["execution_error"] = str(exc)
    try:
        result["after"] = snapshot(project, inputs)
    except (ValueError, OSError) as exc:
        result["after"] = None
        result["snapshot_error"] = str(exc)
    result["finished_utc"] = utc_now()
    result["logs"] = {name: digest(out / name) for name in ("stdout.log", "stderr.log")}
    (out / "run.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n",
                                  encoding="utf-8")
    return result


def parse_axioms(text: str, expected: set[str]) -> dict[str, list[str]]:
    if not expected:
        fail("Expected declaration list is empty")
    clean = COLOR.sub("", text)
    found: dict[str, list[str]] = {}
    matches = list(RESULT.finditer(clean))
    for match in matches:
        name = match["name"]
        if name in found:
            fail(f"Duplicate audit result: {name}")
        raw = match["axioms"]
        if raw is None or not raw.strip():
            axioms: list[str] = []
        else:
            axioms = [item.strip() for item in raw.split(",")]
            if any(not item for item in axioms):
                fail(f"Malformed axiom list for {name}")
        unexpected = set(axioms) - ALLOWED_AXIOMS
        if unexpected:
            fail(f"Disallowed axioms for {name}: {sorted(unexpected)}")
        found[name] = axioms
    residue = RESULT.sub("", clean)
    if re.search(r"^'[^'\r\n]+' .*axioms", residue, re.MULTILINE):
        fail("Unparsed axiom output; inspect raw log and actual Lean version")
    missing = expected - found.keys()
    if missing:
        fail(f"Missing declarations: {sorted(missing)}")
    return found


def load_run(file: Path, project: Path, kind: str) -> tuple[dict, str]:
    file = file.resolve()
    data = json.loads(file.read_text(encoding="utf-8-sig"))
    if data.get("schema") != 1 or data.get("kind") != kind:
        fail(f"Wrong record schema/kind: {file}")
    if data.get("returncode") != 0 or data.get("execution_error"):
        fail(f"Command did not succeed: {file}")
    if Path(data.get("project", "")).resolve() != project:
        fail(f"Different project recorded: {file}")
    if not data.get("before") or data["before"] != data.get("after"):
        fail(f"Inputs changed during command: {file}")
    if not isinstance(data.get("inputs"), list) or not data["inputs"]:
        fail(f"Missing input selection: {file}")
    if snapshot(project, data["inputs"]) != data["after"]:
        fail(f"Current inputs differ from checked snapshot: {file}")
    for name in ("stdout.log", "stderr.log"):
        if data.get("logs", {}).get(name) != digest(file.parent / name):
            fail(f"Log hash mismatch: {name}")
    return data, (file.parent / "stdout.log").read_text(encoding="utf-8-sig")


def audit(project: Path, build_run: Path, axiom_run: Path, expected_file: str) -> dict:
    project = project.resolve()
    build, _ = load_run(build_run, project, "build")
    axioms, output = load_run(axiom_run, project, "axioms")
    if build["after"] != axioms["after"] or sorted(build["inputs"]) != sorted(axioms["inputs"]):
        fail("Build and axiom runs checked different input selections or snapshots")
    expected_path = within(project, expected_file)
    relative = expected_path.relative_to(project).as_posix()
    if relative not in axioms["after"]:
        fail("Expected declaration list was not included in recorded inputs")
    lines = [line.strip() for line in expected_path.read_text(encoding="utf-8-sig").splitlines()
             if line.strip() and not line.lstrip().startswith("#")]
    if len(lines) != len(set(lines)):
        fail("Duplicate declaration in expected list")
    found = parse_axioms(output, set(lines))
    return {"evidence_checks": "passed", "required_declarations": len(lines),
            "audited_declarations": len(found), "selected_files": len(build["after"]),
            "axioms": sorted({ax for values in found.values() for ax in values}),
            "boundary": "Saved evidence integrity only; inspect command/runtime, imports, and statement correspondence."}


def coverage(ledger: Path) -> dict:
    data = json.loads(ledger.read_text(encoding="utf-8-sig"))
    claims = data.get("claims")
    if not isinstance(claims, list) or not claims:
        fail("Ledger must contain a nonempty claims list")
    keys: set[str] = set()
    counts = {"current": Counter(), "historical": Counter()}
    missing_evidence: list[str] = []
    free_text_evidence: list[str] = []
    for claim in claims:
        key, status = claim.get("key"), claim.get("review_status")
        if not isinstance(key, str) or not key or key in keys:
            fail("Missing or duplicate claim key")
        keys.add(key)
        if status not in STATUSES or not isinstance(claim.get("historical"), bool):
            fail(f"Invalid status/history flag: {key}")
        counts["historical" if claim["historical"] else "current"][status] += 1
        if status in {"kernel_verified", "refuted"}:
            if any(not claim.get(field) for field in ("exact_statement", "lean_declarations",
                                                      "build_evidence", "axiom_evidence")):
                missing_evidence.append(key)
            if any(isinstance(claim.get(field), str) for field in ("build_evidence", "axiom_evidence")):
                free_text_evidence.append(key)
    return {"records": len(claims), "recorded_statuses": counts,
            "accepted_records_missing_basic_evidence": missing_evidence,
            "accepted_records_with_free_text_evidence": free_text_evidence,
            "boundary": "Bookkeeping only; no independent-result count, source hash validation, or mathematical certification."}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    rec = sub.add_parser("record", help="Run explicit argv and preserve logs, exit code and selected input hashes")
    rec.add_argument("--project", type=Path, required=True)
    rec.add_argument("--out", type=Path, required=True)
    rec.add_argument("--input", action="append", required=True, dest="inputs")
    rec.add_argument("--kind", choices=("build", "axioms", "probe"), required=True)
    rec.add_argument("command", nargs=argparse.REMAINDER)
    aud = sub.add_parser("audit", help="Check saved build/axiom evidence against current selected inputs")
    aud.add_argument("--project", type=Path, required=True)
    aud.add_argument("--build-run", type=Path, required=True)
    aud.add_argument("--axiom-run", type=Path, required=True)
    aud.add_argument("--expected", required=True)
    cov = sub.add_parser("coverage", help="Summarize recorded claim statuses; not a correctness check")
    cov.add_argument("--ledger", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        if args.action == "record":
            command = args.command[1:] if args.command[:1] == ["--"] else args.command
            result = record(args.project, args.out, args.inputs, args.kind, command)
            code = result["returncode"]
            output = {"run": str(args.out.resolve() / "run.json"), "returncode": code,
                      "inputs_unchanged": result["before"] == result["after"]}
            if code != 0:
                exit_code = code if isinstance(code, int) and 0 < code < 256 else 1
            else:
                exit_code = 0 if output["inputs_unchanged"] else 1
        elif args.action == "audit":
            output, exit_code = audit(args.project, args.build_run, args.axiom_run, args.expected), 0
        else:
            output, exit_code = coverage(args.ledger), 0
        print(json.dumps(output, ensure_ascii=True, indent=2))
        return exit_code
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=True), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
