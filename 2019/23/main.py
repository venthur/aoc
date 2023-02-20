from collections import defaultdict


class Intcode:

    def __init__(self, code, ascii_in=False, default_in=None):
        self.ascii_in = ascii_in
        self.default_in = default_in
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
        if not isinstance(in_, list):
            in_ = [in_]
        if self.ascii_in:
            in_ += '\n'
        for c in in_:
            if self.ascii_in:
                self.inputs.append(ord(c))
            else:
                self.inputs.append(int(c))

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
                    if not self.inputs and self.default_in is None:
                        in_ = input('Input: ')
                        if self.ascii_in:
                            in_ += '\n'
                        for c in in_:
                            if self.ascii_in:
                                self.inputs.append(ord(c))
                            else:
                                self.inputs.append(int(c))
                    if not self.inputs and self.default_in is not None:
                        self.inputs.append(self.default_in)
                    self.code[a] = self.inputs.pop(0)
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

            return


def task1(fn):
    with open(fn) as fh:
        code = [int(n) for n in fh.read().strip().split(',')]

    nics = [Intcode(code, default_in=-1) for i in range(50)]
    outputs = [[] for i in range(len(nics))]
    for i, nic in enumerate(nics):
        nic.set_input(i)

    while True:
        for i, nic in enumerate(nics):
            out = nic.get_output()
            if out is not None:
                outputs[i].append(out)
            if len(outputs[i]) == 3:
                addr, x, y = outputs[i]
                outputs[i] = []
                #print(f'{i:<2} {addr} -> {x, y}')

                if addr == 255:
                    print(y)
                    return

                nics[addr].set_input([x, y])


def task2(fn):
    with open(fn) as fh:
        code = [int(n) for n in fh.read().strip().split(',')]

    nics = [Intcode(code, default_in=-1) for i in range(50)]
    outputs = [[] for i in range(len(nics))]
    nat_outputs = []
    for i, nic in enumerate(nics):
        nic.set_input(i)

    idle_count = 0
    last_y = []
    while True:
        idle_count += 1
        for i, nic in enumerate(nics):
            out = nic.get_output()
            if out is not None:
                outputs[i].append(out)
            if len(outputs[i]) == 3:
                addr, x, y = outputs[i]
                outputs[i] = []
                #print(f'{i:<2} {addr} -> {x, y}')

                if addr == 255:
                    nat_outputs = [x, y]
                else:
                    nics[addr].set_input([x, y])
                    idle_count = 0

        if idle_count > 10000 and nat_outputs:
            nics[0].set_input(nat_outputs)
            last_y.append(nat_outputs[-1])
            nat_outputs = []

            if len(last_y) >= 2:
                last_y = last_y[-2:]
                if last_y[-1] == last_y[-2]:
                    print(last_y[-1])
                    return


task1('input.txt')
task2('input.txt')
