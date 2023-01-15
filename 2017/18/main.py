from collections import defaultdict


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    code = []
    for line in lines:
        cmd, *params = line.split()
        params = [
            int(param) if param.startswith('-') or param.isnumeric()
            else param
            for param in params
        ]
        code.append((cmd, *params))

    registers = defaultdict(lambda: 0)
    ptr = 0
    while 0 <= ptr < len(code):
        match code[ptr]:
            case 'snd', v:
                if isinstance(v, str):
                    v = registers[v]
                registers['snd'] = v
            case 'set', r, v:
                if isinstance(v, str):
                    v = registers[v]
                registers[r] = v
            case 'add', r, v:
                if isinstance(v, str):
                    v = registers[v]
                registers[r] += v
            case 'mul', r, v:
                if isinstance(v, str):
                    v = registers[v]
                registers[r] *= v
            case 'mod', r, v:
                if isinstance(v, str):
                    v = registers[v]
                registers[r] %= v
            case 'rcv', v if isinstance(v, int):
                if v == 0:
                    pass
                else:
                    return registers['snd']
            case 'rcv', v if isinstance(v, str):
                v = registers[v]
                if v == 0:
                    pass
                else:
                    return registers['snd']
            case 'jgz', v, offset:
                if isinstance(offset, str):
                    offset = registers[offset]
                if isinstance(v, str):
                    v = registers[v]
                if v > 0:
                    ptr += offset - 1
        ptr += 1


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    code = []
    for line in lines:
        cmd, *params = line.split()
        params = [
            int(param) if param.startswith('-') or param.isnumeric()
            else param
            for param in params
        ]
        code.append((cmd, *params))

    registers = [defaultdict(lambda: 0) for i in range(2)]
    registers[0]['p'] = 0
    registers[1]['p'] = 1
    ptr = [0 for i in range(2)]
    ptr_old = [None, None]
    queue = [[] for i in range(2)]
    counter = 0
    while 0 <= ptr[0] < len(code) or 0 <= ptr[1] < len(code):
        if ptr_old == ptr:
            return counter
        else:
            ptr_old = ptr[:]
        for i in range(2):
            match code[ptr[i]]:
                case 'snd', v:
                    if isinstance(v, str):
                        v = registers[i][v]
                    queue[(i+1) % 2].append(v)
                    if i == 1:
                        counter += 1
                case 'set', r, v:
                    if isinstance(v, str):
                        v = registers[i][v]
                    registers[i][r] = v
                case 'add', r, v:
                    if isinstance(v, str):
                        v = registers[i][v]
                    registers[i][r] += v
                case 'mul', r, v:
                    if isinstance(v, str):
                        v = registers[i][v]
                    registers[i][r] *= v
                case 'mod', r, v:
                    if isinstance(v, str):
                        v = registers[i][v]
                    registers[i][r] %= v
                case 'rcv', v:
                    if queue[i]:
                        registers[i][v] = queue[i].pop(0)
                    else:
                        continue
                case 'jgz', v, offset:
                    if isinstance(offset, str):
                        offset = registers[i][offset]
                    if isinstance(v, str):
                        v = registers[i][v]
                    if v > 0:
                        ptr[i] += offset - 1
            ptr[i] += 1


assert task1('test_input.txt') == 4
print(task1('input.txt'))

print(task2('input.txt'))
