from collections import defaultdict


def compute(code_in, in_):
    code = defaultdict(lambda: 0)
    for i, v in enumerate(code_in):
        code[i] = v
    ptr = 0
    relative_base = 0
    while True:
        instr = code[ptr]
        op = instr % 100
        # one parameter, none writing
        if op in (4, 9):
            ap = code[ptr+1]
            match instr // 100 % 10:
                case 0:
                    a = code[ap]
                case 1:
                    a = ap
                case 2:
                    a = code[relative_base + ap]
        # one parameter, writing
        elif op in (3, ):
            ap = code[ptr+1]
            if instr // 100 % 10 == 2:
                a = relative_base + ap
            else:
                a = ap
        # two parameters, no writing
        elif op in (5, 6):
            ap = code[ptr+1]
            match instr // 100 % 10:
                case 0:
                    a = code[ap]
                case 1:
                    a = ap
                case 2:
                    a = code[relative_base + ap]
            bp = code[ptr+2]
            match instr // 1000 % 10:
                case 0:
                    b = code[bp]
                case 1:
                    b = bp
                case 2:
                    b = code[relative_base + bp]
        # three parameters, last one writing
        elif op in (1, 2, 7, 8):
            ap = code[ptr+1]
            match instr // 100 % 10:
                case 0:
                    a = code[ap]
                case 1:
                    a = ap
                case 2:
                    a = code[relative_base + ap]
            bp = code[ptr+2]
            match instr // 1000 % 10:
                case 0:
                    b = code[bp]
                case 1:
                    b = bp
                case 2:
                    b = code[relative_base + bp]
            cp = code[ptr+3]
            if instr // 10000 % 10 == 2:
                c = relative_base + cp
            else:
                c = cp

        match op:
            case 1:
                code[c] = a + b
                ptr += 4
            case 2:
                code[c] = a * b
                ptr += 4
            case 3:
                code[a] = in_
                ptr += 2
            case 4:
                print(a)
                ptr += 2
            case 5:
                ptr = b-3 if a else ptr
                ptr += 3
            case 6:
                ptr = b-3 if not a else ptr
                ptr += 3
            case 7:
                code[c] = 1 if a < b else 0
                ptr += 4
            case 8:
                code[c] = 1 if a == b else 0
                ptr += 4
            case 9:
                relative_base += a
                ptr += 2
            case 99:
                break


def task1(fn):
    with open(fn) as fh:
        code = [int(n) for n in fh.read().strip().split(',')]

    compute(code, 1)


def task2(fn):
    with open(fn) as fh:
        code = [int(n) for n in fh.read().strip().split(',')]

    compute(code, 2)

# compute([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99], 0)
# compute([1102,34915192,34915192,7,4,7,99,0], 0)
# compute([104,1125899906842624,99], 0)


task1('input.txt')
task2('input.txt')
