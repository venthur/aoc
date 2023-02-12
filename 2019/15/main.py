from collections import defaultdict
from random import choice, seed
import heapq
from math import dist

seed(0)


class Intcode:

    def __init__(self, code):
        self.code = defaultdict(lambda: 0)
        for i, v in enumerate(code):
            self.code[i] = v

        self.ptr = 0
        self.relative_base = 0
        self.inputs = []
        self.running = True

    def is_running(self):
        return self.running

    def set_input(self, in_):
        self.inputs.append(in_)

    def clear_input(self):
        self.inputs = []

    def get_output(self):
        while True:
            instr = self.code[self.ptr]
            op = instr % 100
            # one parameter, none writing
            if op in (4, 9):
                ap = self.code[self.ptr+1]
                match instr // 100 % 10:
                    case 0:
                        a = self.code[ap]
                    case 1:
                        a = ap
                    case 2:
                        a = self.code[self.relative_base + ap]
            # one parameter, writing
            elif op in (3, ):
                ap = self.code[self.ptr+1]
                if instr // 100 % 10 == 2:
                    a = self.relative_base + ap
                else:
                    a = ap
            # two parameters, no writing
            elif op in (5, 6):
                ap = self.code[self.ptr+1]
                match instr // 100 % 10:
                    case 0:
                        a = self.code[ap]
                    case 1:
                        a = ap
                    case 2:
                        a = self.code[self.relative_base + ap]
                bp = self.code[self.ptr+2]
                match instr // 1000 % 10:
                    case 0:
                        b = self.code[bp]
                    case 1:
                        b = bp
                    case 2:
                        b = self.code[self.relative_base + bp]
            # three parameters, last one writing
            elif op in (1, 2, 7, 8):
                ap = self.code[self.ptr+1]
                match instr // 100 % 10:
                    case 0:
                        a = self.code[ap]
                    case 1:
                        a = ap
                    case 2:
                        a = self.code[self.relative_base + ap]
                bp = self.code[self.ptr+2]
                match instr // 1000 % 10:
                    case 0:
                        b = self.code[bp]
                    case 1:
                        b = bp
                    case 2:
                        b = self.code[self.relative_base + bp]
                cp = self.code[self.ptr+3]
                if instr // 10000 % 10 == 2:
                    c = self.relative_base + cp
                else:
                    c = cp

            match op:
                case 1:
                    self.code[c] = a + b
                    self.ptr += 4
                case 2:
                    self.code[c] = a * b
                    self.ptr += 4
                case 3:
                    if self.inputs:
                        self.code[a] = self.inputs.pop(0)
                    else:
                        in_ = input('Input: ')
                        self.code[a] = in_
                    self.ptr += 2
                case 4:
                    self.ptr += 2
                    return a
                case 5:
                    self.ptr = b-3 if a else self.ptr
                    self.ptr += 3
                case 6:
                    self.ptr = b-3 if not a else self.ptr
                    self.ptr += 3
                case 7:
                    self.code[c] = 1 if a < b else 0
                    self.ptr += 4
                case 8:
                    self.code[c] = 1 if a == b else 0
                    self.ptr += 4
                case 9:
                    self.relative_base += a
                    self.ptr += 2
                case 99:
                    self.running = False
                    break


def task1(fn):
    with open(fn) as fh:
        code = [int(n) for n in fh.read().strip().split(',')]

    x, y = 0, 0
    dirs = {
        1: (0, -1),  # n
        2: (0, 1),   # s
        3: (-1, 0),  # w
        4: (1, 0),   # e
    }
    hull = defaultdict(lambda: ' ')
    hull[x, y] = '.'
    ic = Intcode(code)

    while ic.is_running():
        # move
        # explore unknown
        for d, (dx, dy) in dirs.items():
            if hull[x+dx, y+dy] == ' ':
                direction = d
                break
        # or choose random
        else:
            direction = choice((1, 2, 3, 4))
        xi = x + dirs[direction][0]
        yi = y + dirs[direction][1]
        ic.set_input(direction)

        # get output
        out = ic.get_output()
        match out:
            case 0:
                # hit a wall, pos has not changed
                hull[xi, yi] = '#'
            case 1:
                # moved
                hull[xi, yi] = '.'
                x, y = xi, yi
            case 2:
                # moved, found oxygen station
                hull[xi, yi] = 'X'
                x, y = xi, yi
            case _:
                break

        # check if we have the whole map
        queue = [[0, 0]]
        seen = set()
        seen.add((0, 0))
        ready = True
        while queue and ready:
            xc, yc = queue.pop(0)
            for xci, yci in (xc+1, yc), (xc-1, yc), (xc, yc+1), (xc, yc-1):
                if hull[xci, yci] == ' ':
                    ready = False
                if (xci, yci) not in seen and hull[xci, yci] != "#":
                    seen.add((xci, yci))
                    queue.append((xci, yci))
        if ready:
            break

    # print
    xs, ys = zip(*hull.keys())
    s = ''
    for yi in range(min(ys), max(ys)+1):
        for xi in range(min(xs), max(xs)+1):
            if (xi, yi) == (x, y):
                s += '*'
            else:
                s += hull[xi, yi]
        s += '\n'
    print(s)

    (tx, ty), _ = list(filter(lambda x: x[-1] == 'X', hull.items()))[0]

    # a*
    pq = []
    heapq.heappush(pq, [0, 0, 0, 0])
    seen = {(0, 0)}
    while pq:
        _, x, y, d = heapq.heappop(pq)
        if (x, y) == (tx, ty):
            print(d)
            break
        for xi, yi in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if (xi, yi) not in seen and hull[xi, yi] in ".X":
                seen.add((xi, yi))
                heapq.heappush(pq, [1+d+dist((xi, yi), (tx, ty)), xi, yi, d+1])

    pq = []
    heapq.heappush(pq, [0, tx, ty])
    seen = {(tx, ty)}
    while pq:
        t, x, y = heapq.heappop(pq)
        for xi, yi in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if (xi, yi) not in seen and hull[xi, yi] != "#":
                seen.add((xi, yi))
                heapq.heappush(pq, (t+1, xi, yi))
    print(t)


task1('input.txt')
