def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    acc = 0
    ptr = 0
    seen = set()
    while True:
        if ptr in seen:
            return acc
        seen.add(ptr)
        instr, param = lines[ptr].split()
        match instr:
            case 'acc':
                acc += int(param)
            case 'jmp':
                ptr += int(param)-1
            case 'nop':
                pass
        ptr += 1


def run(code):
    acc = 0
    ptr = 0
    seen = set()
    while 0 <= ptr < len(code):
        if ptr in seen:
            return None
        seen.add(ptr)
        instr, param = code[ptr].split()
        match instr:
            case 'acc':
                acc += int(param)
            case 'jmp':
                ptr += int(param)-1
            case 'nop':
                pass
        ptr += 1
    return acc


def task2(fn):
    with open(fn) as fh:
        code = fh.read().splitlines()

    candidates = [i for i, d in enumerate(code) if d[:3] in ('nop', 'jmp')]
    for i in candidates:
        code2 = code[:]
        if code2[i].startswith('nop'):
            code2[i] = 'jmp' + code2[i][3:]
        else:
            code2[i] = 'nop' + code2[i][3:]
        res = run(code2)
        if res is not None:
            return res


print(task1('input.txt'))

print(task2('input.txt'))
