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
                        print('Error, no inputs!')
                        break
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

    hull = defaultdict(lambda: 0)
    x, y = 0, 0
    direction = 0
    ic = Intcode(code)
    painted = set()
    while ic.is_running():
        ic.set_input(hull[x, y])
        c = ic.get_output()
        d = ic.get_output()
        # paint
        hull[x, y] = c
        painted.add((x, y))
        # change direction
        if d == 0:
            direction -= 1
        elif d == 1:
            direction += 1
        direction %= 4
        # move
        match direction:
            case 0:
                y -= 1
            case 1:
                x += 1
            case 2:
                y += 1
            case 3:
                x -= 1

    return len(painted)


def task2(fn):
    with open(fn) as fh:
        code = [int(n) for n in fh.read().strip().split(',')]

    hull = defaultdict(lambda: 0)
    x, y = 0, 0
    hull[x, y] = 1
    direction = 0
    ic = Intcode(code)
    painted = set()
    while ic.is_running():
        ic.set_input(hull[x, y])
        c = ic.get_output()
        d = ic.get_output()
        # paint
        hull[x, y] = c
        painted.add((x, y))
        # change direction
        if d == 0:
            direction -= 1
        elif d == 1:
            direction += 1
        direction %= 4
        # move
        match direction:
            case 0:
                y -= 1
            case 1:
                x += 1
            case 2:
                y += 1
            case 3:
                x -= 1

    xs, ys = zip(*hull.keys())
    s = ''
    for y in range(min(ys), max(ys)+1):
        for x in range(min(xs), max(xs)+1):
            if hull[x, y] == 0:
                s += ' '
            else:
                s += '#'
        s += '\n'
    print(s)


print(task1('input.txt'))

task2('input.txt')
