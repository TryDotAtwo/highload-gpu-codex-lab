"""Read a small explicit project inventory; never infer scientific completion."""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

FILES = (
    "WORK_PLAN.md", "README.md", "NATIVE_ARCHITECTURE.md", "FEASIBILITY.md",
    "reports/malecns_source_lock.json",
    "data/derived/malecns_v1_candidates/manifest.json",
    "data/derived/mb_synapse_locations_v1/progress.json",
    "reports/shiu_native64_comparison.json",
    "reports/brain_rocket_diagnostic.json",
    "docs/PLASTICITY_REFERENCE.md", "docs/MOTOR_MAPPING_EVIDENCE.md",
    "docs/VISUAL_CAUSALITY.md", "docs/HF_ARCHIVE.md",
    "docs/NUMERICAL_CONTRACT.md", "docs/LANDING_ASSESSMENT.md",
    "tools/extract_mb_synapse_locations.py", "src/landing.rs",
    "native/brain_body_probe.cpp", "native/motor_filter.h",
)
MAX_READ = 2 * 1024 * 1024
FLAGS = {"biological_gate_passed", "passed", "completed", "complete",
         "sensory_feedback_enabled", "num_neurons", "num_edges", "n_neurons",
         "n_edges", "rows", "contacts", "completed_batches", "total_batches"}


def selected_fields(value, prefix="", depth=0):
    result = {}
    if depth > 3 or not isinstance(value, dict):
        return result
    for key, item in value.items():
        if not isinstance(key, str):
            continue
        field = f"{prefix}.{key}" if prefix else key
        if key in FLAGS and (item is None or type(item) in (bool, int, float)):
            result[field] = item
        elif isinstance(item, dict):
            result.update(selected_fields(item, field, depth + 1))
    return result


def snapshot(root):
    root = Path(root).resolve(strict=True)
    if not root.is_dir():
        raise ValueError("workspace must be a directory")
    entries = []
    for relative in FILES:
        path = root / relative
        row = {"path": relative}
        try:
            if not path.exists():
                row["state"] = "missing"
            elif any(p.is_symlink() or getattr(p, "is_junction", lambda: False)()
                     for p in (path, *path.parents) if p != root and root in p.parents):
                row["state"] = "link_skipped"
            elif not path.is_file() or not path.resolve().is_relative_to(root):
                row["state"] = "non_file_or_outside_root"
            else:
                before = path.stat()
                row.update(state="present", bytes=before.st_size,
                           modified_utc=datetime.fromtimestamp(
                               before.st_mtime, timezone.utc).isoformat())
                if before.st_size <= MAX_READ:
                    data = path.read_bytes()
                    after = path.stat()
                    row["sha256"] = hashlib.sha256(data).hexdigest()
                    if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
                        row["state"] = "changed_during_read"
                    elif path.suffix == ".json":
                        try:
                            row["reported_fields_unverified"] = selected_fields(json.loads(data))
                        except (ValueError, UnicodeError):
                            row["json_parse"] = "failed_or_in_progress"
                else:
                    row["content_read"] = "skipped_size_limit"
        except OSError:
            row["state"] = "unreadable"
        entries.append(row)
    return {"workspace": str(root), "generated_utc": datetime.now(timezone.utc).isoformat(),
            "scope": "allowlisted local files only; no live-job or artifact verification",
            "goal_assessment": "not_performed", "files": entries}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", required=True, type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(snapshot(args.workspace), ensure_ascii=False, indent=2))
    except (OSError, ValueError) as exc:
        parser.exit(2, f"snapshot failed: {type(exc).__name__}\n")


if __name__ == "__main__":
    main()
