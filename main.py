import json, sys
from Board import Board
from Solver import Solver

if len(sys.argv) != 2:
    print('Usage: ' + sys.argv[0] + ' input_file.json')
    exit(1)

with open(sys.argv[1], 'r') as f:
    inp = json.load(f)
    if 'board' in inp:  # Support plain boards or tests
        inp = inp['board']

s = Solver()
res, sol = s.solve(inp, True)
if res == "solved":
    print("Solution found!")
    Board(sol).print()
    exit(0)
elif res == "giveup":
    print("I can't solve this puzzle!!!")
    print("Last state:")
    Board(sol).print()
    exit(1)
elif res == "refuse":
    print("The input is unsolvable!!!")
    Board(inp).print()
    print("Reasons:")
    for r in list(set(sol)):  # Unique
        print(r)
    exit(1)
