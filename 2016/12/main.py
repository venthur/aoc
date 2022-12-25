def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    pos = 0
    registers = dict(a=0, b=0, c=0, d=0)
    while True:
        code = lines[pos]
        print(f'{code:<10} {pos=} {registers=}')
        if code.startswith('inc'):
            register = code.split()[-1]
            registers[register] += 1
            pos += 1
        elif code.startswith('dec'):
            register = code.split()[-1]
            registers[register] -= 1
            pos += 1
        elif code.startswith('cpy'):
            _, src, dst = code.split()
            if src.startswith('-') or src.isnumeric():
                src = int(src)
            else:
                src = int(registers[src])
            registers[dst] = src
            pos += 1
        elif code.startswith('jnz'):
            _, x, value = code.split()
            if x.startswith('-') or x.isnumeric():
                x = int(x)
            else:
                x = registers[x]
            if x != 0:
                pos += int(value)
            else:
                pos += 1
        if pos >= len(lines):
            break
    return registers['a']


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    pos = 0
    registers = dict(a=0, b=0, c=1, d=0)
    while True:
        code = lines[pos]
        print(f'{code:<10} {pos=} {registers=}')
        if code.startswith('inc'):
            register = code.split()[-1]
            registers[register] += 1
            pos += 1
        elif code.startswith('dec'):
            register = code.split()[-1]
            registers[register] -= 1
            pos += 1
        elif code.startswith('cpy'):
            _, src, dst = code.split()
            if src.startswith('-') or src.isnumeric():
                src = int(src)
            else:
                src = int(registers[src])
            registers[dst] = src
            pos += 1
        elif code.startswith('jnz'):
            _, x, value = code.split()
            if x.startswith('-') or x.isnumeric():
                x = int(x)
            else:
                x = registers[x]
            if x != 0:
                pos += int(value)
            else:
                pos += 1
        if pos >= len(lines):
            break
    return registers['a']


assert task1('test_input.txt') == 42
print(task1('input.txt'))

print(task2('input.txt'))
