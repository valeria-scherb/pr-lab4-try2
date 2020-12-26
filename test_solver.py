import unittest, json
from Solver import Solver

class TestSolver(unittest.TestCase):

    def _test_board(self, name):
        with open('tests/' + name + '.json', 'r') as f:
            test = json.load(f)
        inp = test['board']
        exp = test['expect']
        try:
            sol = test['solution']
        except KeyError:
            sol = None
        s = Solver()
        s_exp, s_sol = s.solve(inp)
        self.assertEqual(exp, s_exp)
        self.assertEqual(sol, s_sol)

    def test_good(self):
        self._test_board("good")

    def test_bad(self):
        self._test_board("bad")

    def test_ugly(self):
        self._test_board("ugly")

    def test_empty(self):
        self._test_board("empty")
