"""Summarize skill-read requests in one explicit local Codex session, without arguments."""
import argparse
import json
import re
from collections import Counter
from pathlib import Path

READ = re.compile(r"\b(?:Get-Content|cat|read_text|readFileSync|readFile)\b", re.I)
# This deliberately recognizes literal paths, not variable-computed read targets.
PATH = re.compile(r"[\"']([^\"'\r\n]*[/\\]SKILL\.md)[\"']", re.I)
TOOL = re.compile(r"\btools\.([A-Za-z][A-Za-z0-9_]*)\s*\(")


def command_text(value):
    if isinstance(value, str):
        try:
            parsed = json.loads(value)
        except (ValueError, TypeError):
            return value
        if isinstance(parsed, dict):
            return command_text(parsed)
        return value
    if isinstance(value, dict):
        return "\n".join(command_text(value[key]) for key in ("cmd", "code", "input") if key in value)
    return ""


def inspect_session(path):
    counts, reads = Counter(), []
    malformed = calls = 0
    with Path(path).open(encoding="utf-8-sig") as stream:
        for line in stream:
            try:
                event = json.loads(line)
            except ValueError:
                malformed += 1
                continue
            if event.get("type") != "response_item":
                continue
            payload = event.get("payload", {})
            if payload.get("type") not in ("function_call", "custom_tool_call"):
                continue
            calls += 1
            name = payload.get("name", "")
            if re.fullmatch(r"[A-Za-z0-9_.]+", name):
                counts[name] += 1
            code = command_text(payload.get("arguments", payload.get("input", "")))
            counts.update(TOOL.findall(code))
            # Escaped Windows paths in embedded JSON command strings become slashes.
            code = code.replace("\\\"", '"').replace("\\n", "\n")
            code = re.sub(r"\\+", "/", code)
            for command in code.splitlines():
                if not READ.search(command):
                    continue
                for match in PATH.finditer(command):
                    # Output only the skill folder, never the whole command or private paths.
                    skill = match.group(1).split("/")[-2]
                    if re.fullmatch(r"[A-Za-z0-9_.-]+", skill):
                        stamp = event.get("timestamp", "")
                        if not re.fullmatch(r"[0-9TZ:+.\-]+", stamp):
                            stamp = "unavailable"
                        reads.append({"skill": skill, "timestamp": stamp,
                                      "evidence": "literal_read_requested"})
    return {"calls_seen": calls, "malformed_lines": malformed,
            "tool_call_counts": dict(sorted(counts.items())), "skill_read_requests": reads,
            "scope": "heuristic literal reads only; variables and other transports may be missed",
            "instruction_application": "not_proven_by_read_requests"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--session", required=True, type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(inspect_session(args.session), ensure_ascii=False, indent=2))
    except OSError as exc:
        parser.exit(2, f"session inspection failed: {type(exc).__name__}\n")


if __name__ == "__main__":
    main()
