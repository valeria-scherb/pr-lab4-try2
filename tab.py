import copy

to9 = range(0, 9)
to3 = range(0, 3)
fullSet = set(range(1, 10))

class Tab:
    def __init__(self, tab):
        # Set table
        self.tab = tab
        # Initialize allowances
        self.ar = [fullSet.copy() for _ in to9]
        self.ac = [fullSet.copy() for _ in to9]
        self.aq = [[fullSet.copy() for _ in to3] for _ in to3]
        self.f = [[set() for _ in to9] for _ in to9]
        # Enforce constraints
        for i in to9:
            for j in to9:
                self.ar[j] -= {self.tab[j][i]}
                self.ac[i] -= {self.tab[j][i]}
                self.aq[j//3][i//3] -= {self.tab[j][i]}

    def print(self):
        for r in self.tab:
            print(' '.join([('·' if x == 0 else str(x)) for x in r]))
        print()

    def possible(self, i, j):
        if self.tab[j][i] != 0:
            return None
        return (self.ar[j] & self.ac[i] & self.aq[j//3][i//3]) - self.f[j][i]

    def get(self, i, j):
        return self.tab[j][i]

    def set(self, i, j, v):
        if v not in self.possible(i, j):
            return False
        self.unsafe_set(i, j, v)
        return True

    def unsafe_set(self, i, j, v):
        self.tab[j][i] = v
        self.ar[j] -= {v}
        self.ac[i] -= {v}
        self.aq[j//3][i//3] -= {v}

    def fixate(self):
        n = 0
        for j in to9:
            for i in to9:
                p = self.possible(i, j)
                if p is not None:
                    if len(p) == 0:
                        return False
                    if len(p) == 1:
                        self.unsafe_set(i, j, min(p))
                        n += 1
        return n

    def solved(self):
        return max([len(x) for x in self.ar] + [len(x) for x in self.ac]) == 0

    def dc(self):
        return copy.deepcopy(self)

    def next(self, cur):
        i, j = cur
        while self.get(i, j) != 0:
            i += 1
            if i == 9:
                i = 0
                j += 1
            if j == 9:
                return None, None
        return i, j

    def forbid(self, i, j, v):
        self.f[j][i] |= {v}