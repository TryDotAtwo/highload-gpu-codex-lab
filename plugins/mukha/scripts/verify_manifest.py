"""Verify explicit immutable files; byte agreement does not establish provenance."""
import argparse
import hashlib
import json
import re
from pathlib import Path, PurePosixPath, PureWindowsPath


def load_manifest(path):
    def unique_keys(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate JSON key")
            result[key] = value
        return result
    with Path(path).open(encoding="utf-8-sig") as stream:
        return json.load(stream, object_pairs_hook=unique_keys)


def safe_path(root, relative):
    if not isinstance(relative, str) or not relative or "\\" in relative:
        raise ValueError("use nonempty relative POSIX paths")
    parts = relative.split("/")
    if (PurePosixPath(relative).is_absolute() or PureWindowsPath(relative).drive
            or any(p in ("", ".", "..") or ":" in p for p in parts)):
        raise ValueError("absolute, aliased, stream or traversal path")
    cursor = root
    for part in parts:
        cursor = cursor / part
        if cursor.is_symlink() or getattr(cursor, "is_junction", lambda: False)():
            raise ValueError("links are not permitted")
    target = cursor.resolve(strict=True)
    if not target.is_relative_to(root) or not target.is_file():
        raise ValueError("target must be a file under root")
    return target


def verify(root, manifest):
    root = Path(root).resolve(strict=True)
    if not root.is_dir():
        raise ValueError("root must be a directory")
    files = manifest.get("files") if isinstance(manifest, dict) else None
    if not isinstance(files, dict) or not files:
        raise ValueError("expected nonempty files object mapping paths to sha256 and bytes")
    rows, seen = [], set()
    for relative, spec in files.items():
        row = {"path": relative, "verified": False}
        try:
            if not isinstance(spec, dict):
                raise ValueError("entry must be an object")
            expected = spec.get("sha256")
            size = spec.get("bytes")
            if (not isinstance(expected, str) or not re.fullmatch(r"[a-fA-F0-9]{64}", expected)
                    or type(size) is not int or size < 0):
                raise ValueError("entry requires SHA-256 and nonnegative integer bytes")
            path = safe_path(root, relative)
            if path in seen:
                raise ValueError("duplicate resolved path")
            seen.add(path)
            before = path.stat()
            if before.st_size != size:
                raise ValueError("size mismatch")
            digest = hashlib.sha256()
            with path.open("rb") as stream:
                while chunk := stream.read(1024 * 1024):
                    digest.update(chunk)
            after = path.stat()
            if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
                raise ValueError("file changed during verification")
            if digest.hexdigest() != expected.lower():
                raise ValueError("SHA-256 mismatch")
            row.update(verified=True, bytes=size)
        except (OSError, ValueError) as exc:
            row["error"] = str(exc) if isinstance(exc, ValueError) else type(exc).__name__
        rows.append(row)
    return {"byte_verification_passed": all(r["verified"] for r in rows),
            "scope": "listed bytes only; not provenance, scientific validity or unlisted completeness",
            "files": rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--manifest", required=True, type=Path)
    args = parser.parse_args()
    try:
        result = verify(args.root, load_manifest(args.manifest))
    except (OSError, ValueError) as exc:
        print(json.dumps({"byte_verification_passed": False, "error": type(exc).__name__}))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["byte_verification_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
