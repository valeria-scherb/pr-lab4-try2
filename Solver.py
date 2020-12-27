from Board import Board

class Solver:
    def solve(self, inp, loud=False):
        b = Board(inp)
        if loud:
            print('Input board:')
            b.print()
            print()
        if not b.valid:
            if loud:
                print('Refusing to solve (bad data)\n')
            return "refuse", b.bad
        while True:
            t = b.apply_unconditional()
            if type(t) == bool:
                if t:
                    if b.solved():
                        if loud:
                            print('Finally solved the board!')
                            b.print()
                            print()
                        return "solved", b.brd
                    else:
                        if loud:
                            print('End of algorithm with no success')
                            b.print()
                            print()
                        return "giveup", b.brd
                else:
                    if loud:
                        print('Found impossible constraint set')
                        b.print()
                        print()
                    return "giveup", None
            i, j, k = t
            if loud:
                print('Applied ' + str(k) + ' in cell (' +
                      str(i+1) + ', ' + str(j+1) + ')')
                b.evident(i, j)
                print()
