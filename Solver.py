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
        prev = pi = pj = None
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
                        # if loud:
                        #     print('End of algorithm with no success')
                        #     b.print()
                        #     print()
                        # return "giveup", b.brd
                        pi, pj = b.next_empty()
                        poss = b.possible(pi, pj)
                        if len(poss) == 0:
                            if loud:
                                print('Cannot put anything into cell')
                                b.evident(pi, pj)
                                print()
                            return "giveup", b.brd
                        tryval = min(poss)
                        b.forbid(pi, pj, tryval)
                        prev = b.dc()
                        b.unsafe_set(pi, pj, tryval)
                        if loud:
                            print('Attempting ' + str(tryval) + ' into (' + str(pi+1) + ', ' + str(pj+1) + ')')
                            b.evident(pi, pj)
                            print()
                        continue
                else:
                    if loud:
                        print('Found impossible constraint set')
                        b.evident(b.ic[0], b.ic[1])
                        print()
                    if prev is not None:
                        print('Retrying mark at cell (' + str(pi+1) + ', ' + str(pj+1) + ')')
                        b = prev
                        poss = b.possible(pi, pj)
                        if len(poss) == 0:
                            if loud:
                                print('Cannot put anything into cell')
                                b.evident(pi, pj)
                                print()
                            return "giveup", b.brd
                        tryval = min(poss)
                        b.forbid(pi, pj, tryval)
                        prev = b.dc()
                        b.unsafe_set(pi, pj, tryval)
                        if loud:
                            print('Attempting ' + str(tryval) + ' into (' + str(pi+1) + ', ' + str(pj+1) + ')')
                            b.evident(pi, pj)
                            print()
                        continue
                    return "refuse", ['Found a cell with no possible values']
            i, j, k = t
            if loud:
                print('Applied ' + str(k) + ' in cell (' +
                      str(i+1) + ', ' + str(j+1) + ')')
                b.evident(i, j)
                print()
