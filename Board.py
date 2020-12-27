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
        bad = []
        for i in to9:
            for j in to9:
                b = self.brd[j][i]
                if b == 0:
                    continue
                if b not in self.ar[j]:
                    bad.append('Multiple ' + str(b) + ' in row ' + str(j+1))
                if b not in self.ac[i]:
                    bad.append('Multiple ' + str(b) + ' in column ' + str(i+1))
                if b not in self.aq[j//3][i//3]:
                    bad.append('Multiple ' + str(b) + ' in quadrant (' +
                               str(j//3+1) + ', ' + str(i//3+1) + ')')
                self.ar[j] -= {b}
                self.ac[i] -= {b}
                self.aq[j//3][i//3] -= {b}
        self.valid = len(bad) == 0
        self.bad = bad

    def print(self):
        for r in self.brd:
            print(' '.join([('·' if x == 0 else str(x)) for x in r]))
        print()

    def evident(self, ei, ej):
        for j in to9:
            if ej != j:
                print(' ' + ' '.join([('·' if x == 0 else str(x))
                                for x in self.brd[j]]))
            else:
                s = '' if ei == 0 else ' '
                for i in to9:
                    x = self.brd[j][i]
                    if i == ei:
                        s += '[' + ('·' if x == 0 else str(x)) + ']'
                    else:
                        s += ('·' if x == 0 else str(x)) + \
                             (' ' if i != ei - 1 else '')
                print(s)

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
