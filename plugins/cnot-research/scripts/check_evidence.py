"""Read-only source-drift and independent GF(2) certificate check; stdlib only."""
import argparse
import hashlib
import json
from pathlib import Path

BASE = Path('synthesis-methods/01_shared_basis_stage17')
IMPROVED = BASE / 'improved'
REPORTS = [
    'structured_field/runs/replay_v4_comparison.json',
    'policy_iteration/runs/teacher_policy_v3/comparison.json',
    'policy_iteration/runs/teacher_policy_v3/shortlist32.json',
    'policy_iteration/runs/walk_heat_on_v1/comparison.json',
    'policy_iteration/runs/walk_heat_off_v1/comparison.json',
    'policy_iteration/runs/walk_heat_on_v1/large.json',
    'policy_iteration/runs/walk_heat_off_v1/large.json',
]


def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def safe_child(root, relative):
    result = (root / relative).resolve()
    if not result.is_relative_to(root.resolve()):
        raise ValueError('Path outside specified project: ' + str(relative))
    return result


def matrix_rows(path):
    matrix = read(path)['matrix']
    n = len(matrix)
    if not n or any(len(row) != n or any(bit not in (0, 1) for bit in row) for row in matrix):
        raise ValueError('Invalid binary square target: ' + str(path))
    return tuple(sum(bit << j for j, bit in enumerate(row)) for row in matrix)


def verify_word(target, gates, count):
    if not isinstance(gates, list) or len(gates) != count:
        raise ValueError('Word/count mismatch')
    n = len(target)
    state = [1 << i for i in range(n)]
    for gate in gates:
        if not isinstance(gate, list) or len(gate) != 2:
            raise ValueError('Malformed gate')
        c, t = gate
        if type(c) is not int or type(t) is not int or c == t or not (0 <= c < n and 0 <= t < n):
            raise ValueError('Invalid CNOT indices')
        state[t] ^= state[c]
    if tuple(state) != target:
        raise ValueError('Encoder does not reproduce the entire target')


def check(project, plugin):
    result = dict(source_drift=[], missing_pinned=[], snapshot_errors=[], verified_words=[], failures=[], pending=[],
                  paired_files={}, errors=[])
    manifest = read(plugin / 'assets/evidence_manifest.json')
    for entry in manifest['files']:
        path = safe_child(project, entry['path'])
        if not path.is_file():
            result['missing_pinned'].append(entry['path'])
        elif hashlib.sha256(path.read_bytes()).hexdigest() != entry['sha256']:
            result['source_drift'].append(entry['path'])
        if 'snapshot' in entry:
            snapshot = safe_child(plugin, entry['snapshot'])
            if not snapshot.is_file() or hashlib.sha256(snapshot.read_bytes()).hexdigest() != entry['sha256']:
                result['snapshot_errors'].append(entry['snapshot'])
    for name in REPORTS:
        path = project / IMPROVED / name
        if not path.is_file():
            result['pending'].append(name)
            continue
        try:
            report = read(path)
            for row in report['rows']:
                case = row['case']
                if Path(case).name != case or '/' in case or '\\' in case:
                    raise ValueError('Invalid case name')
                target = matrix_rows(project / BASE / 'source_snapshot/inputs' / (case + '.json'))
                found = 0
                for method, value in row.items():
                    if not isinstance(value, dict) or 'verified' not in value:
                        continue
                    found += 1
                    item = dict(report=name, case=case, method=method)
                    if value['verified'] is True:
                        verify_word(target, value.get('gates'), value.get('count'))
                        result['verified_words'].append(dict(**item, count=value['count']))
                    else:
                        if value.get('count') is not None:
                            raise ValueError('Unverified outcome has a reported count')
                        result['failures'].append(dict(**item, reason=value.get('reason', 'unspecified')))
                if not found:
                    raise ValueError('No recognized certificate result in ' + case)
        except (ValueError, KeyError, TypeError, OSError) as exc:
            result['errors'].append(dict(report=name, error=str(exc)))
    for name in ('replay_initial.json', 'validation.json', 'walk_heat_profiles.json'):
        a = project / IMPROVED / 'policy_iteration/runs/walk_heat_on_v1' / name
        b = project / IMPROVED / 'policy_iteration/runs/walk_heat_off_v1' / name
        result['paired_files'][name] = a.is_file() and b.is_file() and a.read_bytes() == b.read_bytes()
    result['scope'] = ('SHA-256 of pinned files; independent full-matrix multiplication of recognized '
                       'newer comparison words; byte equality of paired initial data. Does not load '
                       'weights, retest training, certify optimality, or verify every historical replay word.')
    result['ok'] = not (result['errors'] or result['source_drift'] or result['missing_pinned'] or result['snapshot_errors']) and all(result['paired_files'].values())
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--project', type=Path, required=True)
    args = parser.parse_args()
    result = check(args.project.resolve(), Path(__file__).resolve().parents[1])
    print(json.dumps(result, ensure_ascii=True, indent=2))
    raise SystemExit(0 if result['ok'] else 1)


if __name__ == '__main__':
    main()
