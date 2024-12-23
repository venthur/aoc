from collections import deque
from itertools import product


def read_input(fn):
    lines = []
    with open(fn) as fh:
        for line in fh:
            lines.append(line.strip())
    return lines


NUMPAD = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"],
]


DIRPAD = [
    [None, "^", "A"],
    ["<", "v", ">"],
]


def solve(string, keypad):
    pos = {}
    for r in range(len(keypad)):
        for c in range(len(keypad[r])):
            if keypad[r][c] is not None:
                pos[keypad[r][c]] = (r, c)
    seqs = {}
    for x in pos:
        for y in pos:
            if x == y:
                seqs[(x, y)] = ["A"]
                continue
            possibilities = []
            q = deque([(pos[x], "")])
            optimal = float("inf")
            while q:
                (r, c), moves = q.popleft()
                for nr, nc, nm in (r-1, c, "^"), (r+1, c, "v"), (r, c-1, "<"), (r, c+1, ">"),:
                    if nr < 0 or nc < 0 or nr >= len(keypad) or nc >= len(keypad[0]):
                        continue
                    if keypad[nr][nc] is None:
                        continue
                    if keypad[nr][nc] == y:
                        if optimal < len(moves) + 1:
                            break
                        optimal = len(moves) + 1
                        possibilities.append(moves + nm + "A")
                    else:
                        q.append(((nr, nc), moves + nm))
                else:
                    continue
                break
            seqs[(x, y)] = possibilities
    options = [seqs[(x, y)] for x, y in zip("A" + string, string)]
    return ["".join(x) for x in product(*options)]


def task1(fn):
    data = read_input(fn)
    total = 0
    for line in data:
        robot1 = solve(line, NUMPAD)
        next = robot1
        for _ in range(2):
            possible_next = []
            for seq in next:
                possible_next += solve(seq, DIRPAD)
            minlen = min(map(len, possible_next))
            next = [seq for seq in possible_next if len(seq) == minlen]
        total += len(next[0]) * int(line[:-1])
    return total


assert task1('test_input.txt') == 126384
print(task1('input.txt'))
