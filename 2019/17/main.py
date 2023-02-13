from collections import defaultdict


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

    ic = Intcode(code)
    scaffold = defaultdict(bool)
    x, y, d = 0, 0, 0
    xi, yi = 0, 0
    while ic.is_running():
        out = ic.get_output()
        if out is not None:
            print(chr(out), end="")
            match chr(out):
                case '#':
                    scaffold[xi, yi] = True
                    xi += 1
                case '.':
                    xi += 1
                case '\n':
                    xi = 0
                    yi += 1
                case '^':
                    scaffold[xi, yi] = True
                    x, y = xi, yi
                    d = 0
                    xi += 1

    xs, ys = zip(*scaffold.keys())
    s = 0
    for yi in range(0, max(ys)+1):
        for xi in range(0, max(xs)+1):
            if (
                scaffold[xi, yi] and
                scaffold[xi+1, yi] and scaffold[xi-1, yi] and
                scaffold[xi, yi+1] and scaffold[xi, yi-1]
            ):
                s += xi * yi
    # pt 1
    print(s)

    dirs = (0, -1), (1, 0), (0, 1), (-1, 0)
    path = []
    while True:
        # can we go straight?
        xn, yn = x+dirs[d][0], y+dirs[d][1]
        if scaffold[xn, yn]:
            x, y = xn, yn
            if isinstance(path[-1], int):
                path[-1] += 1
            else:
                path.append(1)
            continue
        # no? check left or right (never back)
        d2 = (d-1) % 4
        xn, yn = x+dirs[d2][0], y+dirs[d2][1]
        if scaffold[xn, yn]:
            d = d2
            path.append('L')
            continue
        d2 = (d+1) % 4
        xn, yn = x+dirs[d2][0], y+dirs[d2][1]
        if scaffold[xn, yn]:
            d = d2
            path.append('R')
            continue
        break

    path = [str(c) for c in path]

    found = False
    for ae in range(0, 10):
        if found:
            break
        for bs in range(ae+1, len(path)):
            if found:
                break
            for be in range(bs+2, bs+2+10):
                a = ''.join(path[0:ae])
                b = ''.join(path[bs:be])
                rem = set(''.join(path).replace(a, ' ').replace(b, ' ').split())
                if len(rem) == 1:
                    c = rem.pop()
                    found = True
                    break
    main = ','.join(''.join(path).replace(a, ' A ').replace(b, ' B ').replace(c, ' C ').split())
    main += '\n'

    a = ','.join(a.replace('R', ' R ').replace('L', ' L ').split()) + '\n'
    b = ','.join(b.replace('R', ' R ').replace('L', ' L ').split()) + '\n'
    c = ','.join(c.replace('R', ' R ').replace('L', ' L ').split()) + '\n'

    code[0] = 2
    ic = Intcode(code)

    for msg in main, a, b, c:
        for c in msg:
            ic.set_input(ord(c))

    ic.set_input(ord('n'))
    ic.set_input(ord('\n'))

    while ic.is_running():
        out = ic.get_output()
        if out is not None and out < 256:
            print(chr(out), end="")
        else:
            break
    # pt 2
    print(out)


task1('input.txt')
