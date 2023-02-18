from itertools import count
from collections import defaultdict


class Intcode:

    def __init__(self, code):
        self._code = code[:]
        self.reset()

    def reset(self):
        self.code = defaultdict(lambda: 0)
        for i, v in enumerate(self._code):
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
                        self.code[a] = int(in_)
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
    cnt = 0
    for y in range(50):
        for x in range(50):
            ic.reset()
            ic.set_input(x)
            ic.set_input(y)
            cnt += ic.get_output()
    # pt 1
    print(cnt)

    def check(x, y):
        ic.reset()
        ic.set_input(x)
        ic.set_input(y)
        return ic.get_output()

    x = 0
    for y in count(100):
        while check(x, y) == 0:
            x += 1
        if check(x+100-1, y-100+1):
            break
    print(x*10000 + y-99)


task1('input.txt')
