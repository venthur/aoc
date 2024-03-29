from itertools import permutations


def compute(index, phase, code, io):

    ptr = 0
    first = True
    while True:
        instr = code[ptr]
        op = instr % 100
        if op in (3, 4):
            ap = code[ptr+1]
            ai = instr // 100 % 10
            a = code[ap] if not ai else ap
        if op in (5, 6):
            ap = code[ptr+1]
            ai = instr // 100 % 10
            a = code[ap] if not ai else ap
            bp = code[ptr+2]
            bi = instr // 1000 % 10
            b = code[bp] if not bi else bp
        if op in (1, 2, 7, 8):
            ap = code[ptr+1]
            ai = instr // 100 % 10
            a = code[ap] if not ai else ap
            bp = code[ptr+2]
            bi = instr // 1000 % 10
            b = code[bp] if not bi else bp
            cp = code[ptr+3]
            ci = instr // 10000 % 10
            c = code[cp] if not ci else cp

        # print(f'{ptr=} {code[ptr]=}, {a, b, c=} {ai, bi, ci=} {io=}')
        match op:
            case 1:
                code[cp] = a + b
                ptr += 4
            case 2:
                code[cp] = a * b
                ptr += 4
            case 3:
                if first:
                    code[ap] = phase
                    first = False
                else:
                    code[ap] = io[index]
                ptr += 2
            case 4:
                io[index+1] = a
                ptr += 2
            case 5:
                ptr = b-3 if a else ptr
                ptr += 3
            case 6:
                ptr = b-3 if not a else ptr
                ptr += 3
            case 7:
                code[cp] = 1 if a < b else 0
                ptr += 4
            case 8:
                code[cp] = 1 if a == b else 0
                ptr += 4
            case 99:
                break


def task1(fn):
    with open(fn) as fh:
        code = [int(n) for n in fh.read().strip().split(',')]

    maxv = None
    for p in permutations([0, 1, 2, 3, 4]):
        io = [0, None, None, None, None, None]

        for i, phase in enumerate(p):
            compute(i, phase, code, io)

        if maxv is None or io[-1] > maxv:
            maxv = io[-1]

    return maxv


def compute2(phase, code):
    io = [0, None, None, None, None]
    running = [True for i in range(5)]
    ptrs = [0 for i in range(5)]
    first = [True for i in range(5)]

    amp = 0
    while any(running):
        # print(f'{io=} {running=} {ptrs=} {first=} {amp=}')
        ptr = ptrs[amp]
        while running[amp]:
            instr = code[ptr]
            op = instr % 100
            if op in (3, 4):
                ap = code[ptr+1]
                ai = instr // 100 % 10
                a = code[ap] if not ai else ap
            if op in (5, 6):
                ap = code[ptr+1]
                ai = instr // 100 % 10
                a = code[ap] if not ai else ap
                bp = code[ptr+2]
                bi = instr // 1000 % 10
                b = code[bp] if not bi else bp
            if op in (1, 2, 7, 8):
                ap = code[ptr+1]
                ai = instr // 100 % 10
                a = code[ap] if not ai else ap
                bp = code[ptr+2]
                bi = instr // 1000 % 10
                b = code[bp] if not bi else bp
                cp = code[ptr+3]
                ci = instr // 10000 % 10
                c = code[cp] if not ci else cp

            match op:
                case 1:
                    code[cp] = a + b
                    ptr += 4
                case 2:
                    code[cp] = a * b
                    ptr += 4
                case 3:
                    if first[amp]:
                        code[ap] = phase[amp]
                        first[amp] = False
                    else:
                        code[ap] = io[amp]
                    ptr += 2
                case 4:
                    io[(amp+1) % 5] = a
                    ptr += 2
                    ptrs[amp] = ptr
                    break
                case 5:
                    ptr = b-3 if a else ptr
                    ptr += 3
                case 6:
                    ptr = b-3 if not a else ptr
                    ptr += 3
                case 7:
                    code[cp] = 1 if a < b else 0
                    ptr += 4
                case 8:
                    code[cp] = 1 if a == b else 0
                    ptr += 4
                case 99:
                    running[amp] = False
                    break

        amp += 1
        amp %= 5

    return io[0]


def task2(fn):
    with open(fn) as fh:
        code = [int(n) for n in fh.read().strip().split(',')]

    maxv = None
    for p in permutations([5, 6, 7, 8, 9]):
        output = compute2(p, code)

        if maxv is None or output > maxv:
            maxv = output

    return maxv


print(task1('input.txt'))

print(task2('input.txt'))
