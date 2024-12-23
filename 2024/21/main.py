from collections import deque
from itertools import product
from functools import cache


def read_input(fn):
    lines = []
    with open(fn) as fh:
        for line in fh:
            lines.append(line.strip())
    return lines


def compute_seqs(keypad):
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
    return seqs


def solve(string, seqs):
    options = [seqs[(x, y)] for x, y in zip("A" + string, string)]
    return ["".join(x) for x in product(*options)]


@cache
def compute_length(seq, depth=2):
    if depth == 1:
        return sum(DIR_LENGTHS[(x, y)] for x, y in zip("A" + seq, seq))
    length = 0
    for x, y in zip("A" + seq, seq):
        length += min(compute_length(subseq, depth - 1) for subseq in DIR_SEQS[(x, y)])
    return length


NUMPAD = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"],
]
NUM_SEQS = compute_seqs(NUMPAD)


DIRPAD = [
    [None, "^", "A"],
    ["<", "v", ">"],
]
DIR_SEQS = compute_seqs(DIRPAD)
DIR_LENGTHS = {key: len(value[0]) for key, value in DIR_SEQS.items()}


def task1(fn, depth=2):
    data = read_input(fn)
    total = 0
    for line in data:
        inputs = solve(line, NUM_SEQS)
        length = min([compute_length(i, depth) for i in inputs])
        total += length * int(line[:-1])
    return total


assert task1('test_input.txt') == 126384
print(task1('input.txt'))

print(task1('input.txt', 25))
