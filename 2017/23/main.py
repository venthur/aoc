def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    def convert_int(s):
        if s.startswith('-') or s.isnumeric():
            return int(s)
        return s

    lines = [list(map(convert_int, line.split())) for line in lines]

    ptr = 0
    register = dict(a=0, b=0, c=0, d=0, e=0, f=0, g=0, h=0)
    multiplications = 0
    while 0 <= ptr < len(lines):
        match lines[ptr]:
            case 'set', reg, val:
                if isinstance(val, str):
                    val = register[val]
                register[reg] = val
            case 'sub', reg, val:
                if isinstance(val, str):
                    val = register[val]
                register[reg] -= val
            case 'mul', reg, val:
                if isinstance(val, str):
                    val = register[val]
                register[reg] *= val
                multiplications += 1
            case 'jnz', val, offset:
                if isinstance(val, str):
                    val = register[val]
                if val != 0:
                    ptr += offset - 1
        ptr += 1

    return multiplications


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    def convert_int(s):
        if s.startswith('-') or s.isnumeric():
            return int(s)
        return s

    lines = [list(map(convert_int, line.split())) for line in lines]

    ptr = 0
    i = 0
    register = dict(a=1, b=0, c=0, d=0, e=0, f=0, g=0, h=0)
    while 0 <= ptr < len(lines):
        if i % 10000000 == 0:
            print(f'{register}')
            i = 0
        i += 1
        match lines[ptr]:
            case 'set', reg, val:
                if isinstance(val, str):
                    val = register[val]
                register[reg] = val
            case 'sub', reg, val:
                if isinstance(val, str):
                    val = register[val]
                register[reg] -= val
            case 'mul', reg, val:
                if isinstance(val, str):
                    val = register[val]
                register[reg] *= val
            case 'jnz', val, offset:
                if isinstance(val, str):
                    val = register[val]
                if val != 0:
                    ptr += offset - 1
        ptr += 1

    return register['h']


print(task1('input.txt'))

print(task2('input.txt'))
