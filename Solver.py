from Board import Board

class Solver:
    def solve(self, inp):
        b = Board(inp)
        if not b.valid:
            return "refuse", None
        return "notimpl", None
