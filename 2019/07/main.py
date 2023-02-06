from itertools import permutations


def compute(index, phase, code, io):

    ptr = 0
    first = True
    while True:
        instr = code[ptr]
        op = instr % 100
        if (len(code) - ptr) > 3:
            c = code[ptr+3]
            ci = instr // 10000 % 10
        if (len(code) - ptr) > 2:
            b = code[ptr+2]
            bi = instr // 1000 % 10
        if (len(code) - ptr) > 1:
            a = code[ptr+1]
            ai = instr // 100 % 10

        # print(f'{ptr=} {code[ptr]=}, {a, b, c=} {ai, bi, ci=} {io=}')
        match op:
            case 1:
                a = code[a] if not ai else a
                b = code[b] if not bi else b
                code[c] = a + b
                ptr += 4
            case 2:
                a = code[a] if not ai else a
                b = code[b] if not bi else b
                code[c] = a * b
                ptr += 4
            case 3:
                if first:
                    code[a] = phase
                    first = False
                else:
                    code[a] = io[index]
                ptr += 2
            case 4:
                a = code[a] if not ai else a
                io[index+1] = a
                ptr += 2
            case 5:
                a = code[a] if not ai else a
                b = code[b] if not bi else b
                ptr = b-3 if a else ptr
                ptr += 3
            case 6:
                a = code[a] if not ai else a
                b = code[b] if not bi else b
                ptr = b-3 if not a else ptr
                ptr += 3
            case 7:
                a = code[a] if not ai else a
                b = code[b] if not bi else b
                code[c] = 1 if a < b else 0
                ptr += 4
            case 8:
                a = code[a] if not ai else a
                b = code[b] if not bi else b
                code[c] = 1 if a == b else 0
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
            print(io)

        if maxv is None or io[-1] > maxv:
            maxv = io[-1]

    return maxv


print(task1('input.txt'))
