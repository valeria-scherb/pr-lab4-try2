import copy

to9 = range(0, 9)
to3 = range(0, 3)
fullSet = set(range(1, 10))

class Board:
    def __init__(self, brd):
        # Set board
        self.brd = brd
        # Initialize allowances
        self.ar = [fullSet.copy() for _ in to9]
        self.ac = [fullSet.copy() for _ in to9]
        self.aq = [[fullSet.copy() for _ in to3] for _ in to3]
        self.f = [[set() for _ in to9] for _ in to9]
        # Enforce constraints
        valid = True
        for i in to9:
            for j in to9:
                if self.brd[j][i] == 0:
                    continue
                valid &= (self.brd[j][i] in self.ar[j]) \
                     and (self.brd[j][i] in self.ac[i]) \
                     and (self.brd[j][i] in self.aq[j//3][i//3])
                self.ar[j] -= {self.brd[j][i]}
                self.ac[i] -= {self.brd[j][i]}
                self.aq[j//3][i//3] -= {self.brd[j][i]}
        self.valid = valid

    def print(self):
        for r in self.brd:
            print(' '.join([('·' if x == 0 else str(x)) for x in r]))
        print()

    def possible(self, i, j):
        if self.brd[j][i] != 0:
            return None
        return (self.ar[j] & self.ac[i] & self.aq[j//3][i//3]) - self.f[j][i]

    def get(self, i, j):
        return self.brd[j][i]

    def set(self, i, j, v):
        if v not in self.possible(i, j):
            return False
        self.unsafe_set(i, j, v)
        return True

    def unsafe_set(self, i, j, v):
        self.brd[j][i] = v
        self.ar[j] -= {v}
        self.ac[i] -= {v}
        self.aq[j//3][i//3] -= {v}

    def apply_unconditional(self):
        for j in to9:
            for i in to9:
                p = self.possible(i, j)
                if p is not None:
                    if len(p) == 0:
                        return False
                    if len(p) == 1:
                        self.unsafe_set(i, j, min(p))
                        return i, j, min(p)
        return True

    def solved(self):
        return max([len(x) for x in self.ar] + [len(x) for x in self.ac]) == 0

    def dc(self):
        return copy.deepcopy(self)
