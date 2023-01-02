def task1(fn, a=0, b=0, c=0, d=0):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    pos = 0
    registers = dict(a=a, b=b, c=c, d=d)
    while True:
        code = lines[pos]
        print(f'\n{code:<10} {pos=} {registers=}')
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
            if dst.startswith('-') or dst.isnumeric():
                pass
            else:
                registers[dst] = src
            pos += 1
        elif code.startswith('jnz'):
            _, x, value = code.split()
            if x.startswith('-') or x.isnumeric():
                x = int(x)
            else:
                x = registers[x]
            if value.startswith('-') or value.isnumeric():
                value = int(value)
            else:
                value = registers[value]
            if x != 0:
                pos += value
            else:
                pos += 1
        elif code.startswith('tgl'):
            value = code.split()[-1]
            if value.startswith('-') or value.isnumeric():
                value = int(value)
            else:
                value = registers[value]
            linenr = pos + value
            if linenr < 0 or linenr >= len(lines):
                pass
            elif lines[linenr].startswith('inc'):
                lines[linenr] = lines[linenr].replace('inc', 'dec')
            elif len(lines[linenr].split()) == 2:
                token = lines[linenr].split()[0]
                lines[linenr] = lines[linenr].replace(token, 'inc')
            elif lines[linenr].startswith('jnz'):
                lines[linenr] = lines[linenr].replace('jnz', 'cpy')
            elif len(lines[linenr].split()) == 3:
                token = lines[linenr].split()[0]
                lines[linenr] = lines[linenr].replace(token, 'jnz')
            pos += 1
        else:
            raise ValueError(code)
        if pos >= len(lines):
            break
    return registers['a']


#assert task1('test_input.txt') == 3
#print(task1('input.txt', a=7))

print(task1('input.txt', a=12))
