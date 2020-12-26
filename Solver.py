from Board import Board

class Solver:
    def solve(self, inp):
        b = Board(inp)
        if not b.valid:
            return "refuse", None
        while True:
            t = b.apply_unconditional()
            if type(t) == bool:
                if t:
                    if b.solved():
                        return "solved", b.brd
                    else:
                        return "giveup", b.brd
                else:
                    return "giveup", None
