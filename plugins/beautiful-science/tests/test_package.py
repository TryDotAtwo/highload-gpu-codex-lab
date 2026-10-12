"""Structural checks and exact example witnesses, not an empirical skill-quality score."""
import hashlib
import json
import math
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'choose-research-path'

class PackageContract(unittest.TestCase):
    def test_manifest_and_single_entrypoint(self):
        p = json.loads((ROOT / '.codex-plugin/plugin.json').read_text())
        self.assertEqual(p['name'], ROOT.name)
        self.assertEqual(p['skills'], './skills/')
        self.assertEqual(len(list((ROOT/'skills').glob('*/SKILL.md'))), 1)
        self.assertNotIn('mcpServers', p)
        self.assertNotIn('apps', p)
    def test_relative_reference_links_resolve(self):
        for f in SKILL.rglob('*.md'):
            for target in re.findall(r'\]\(([^ )]+)(?:[^)]*)\)', f.read_text()):
                if not re.match(r'^[a-z]+:', target) and not target.startswith('#'):
                    self.assertTrue((f.parent/target.split('#')[0]).resolve().is_file(), (f, target))
    def test_entrypoint_is_short_and_frontmatter_named(self):
        text = (SKILL/'SKILL.md').read_text()
        self.assertTrue(text.startswith('---\nname: choose-research-path\n'))
        self.assertLessEqual(len(text.split()), 900)
        self.assertNotIn('[TODO:', text)
    def test_test_case_ids_unique_and_required_coverage_present(self):
        cases = json.loads((ROOT/'tests/scenarios.json').read_text())
        ids = [c['id'] for c in cases]
        self.assertEqual(len(ids),len(set(ids)))
        self.assertEqual(set(ids), set(json.loads((ROOT/'tests/rubric.json').read_text())['cases']))
    def test_no_runtime_external_dependencies(self):
        for f in SKILL.rglob('*'):
            self.assertNotEqual(f.name, '.mcp.json')
        self.assertFalse((ROOT/'hooks').exists())
    def test_examples_marked_as_constructed(self):
        # Metadata contract, not a test of research judgment.
        p=json.loads((ROOT/'tests/witnesses.json').read_text())
        self.assertEqual(p['evidence_status'], 'constructed_exact_examples')

class ExactWitnesses(unittest.TestCase):
    def test_exponential_storage_at_target(self):
        self.assertEqual(16*(2**60), 2**64)
        self.assertEqual((16*(2**60))//(128*(2**30)), 2**27)
        self.assertGreater(16*(2**60), 128*10**9)
    def test_amortized_cost_is_not_query_cost(self):
        # Illustrative seconds, not measured performance.
        prep, query, baseline = 1200, 0.1, 20
        self.assertGreater(prep+10*query, 10*baseline)
        self.assertLess(prep+100*query, 100*baseline)
        q_min=math.floor(prep/(baseline-query))+1
        self.assertEqual(q_min,61)
    def test_one_counterexample_invalidates_universal_not_family(self):
        # Symmetric objective has asymmetric minimizers: symmetry != symmetric solution.
        f=lambda x:(x*x-1)**2
        self.assertEqual(f(-1), f(1))
        self.assertLess(f(-1),f(0))
    def test_equal_decay_rates_not_identifiable(self):
        # A convex sum of identical exponentials equals that exponential for all t.
        from fractions import Fraction
        for w in (Fraction(1,4),Fraction(1,2),Fraction(3,4)):
            self.assertEqual(w+(1-w),1)
        # Curvature of log-mixture at t=0: w(1-w)(k1-k2)^2.
        self.assertEqual(Fraction(1,4)*Fraction(3,4)*(2-2)**2,0)
        self.assertGreater(Fraction(1,4)*Fraction(3,4)*(2-3)**2,0)
    def test_connected_graph_vertex_deletion_can_disconnect(self):
        # A path of three vertices is connected; removing its middle vertex disconnects it.
        edges={(0,1),(1,2)}
        remaining={0,2}
        self.assertFalse(any(u in remaining and v in remaining for u,v in edges))
    def test_zero_and_target_gain_are_different_hypotheses(self):
        lower, upper, target = -0.8, 1.6, 5.0
        self.assertLess(lower,0)
        self.assertGreater(upper,0)
        self.assertLess(upper,target)
        # Valid CI interpretation still depends on the design, not this arithmetic.

if __name__=='__main__':
    unittest.main(verbosity=2)
