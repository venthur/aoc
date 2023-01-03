import time


def task1(fn, a=0, b=0, c=0, d=0):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    code = []
    for line in lines:
        tokens = line.split()
        loc = []
        for t in tokens:
            if t.startswith('-') or t.isnumeric():
                loc.append(int(t))
            else:
                loc.append(t)
        code.append(loc)
    lines = code[:]

    i = 0
    t = time.time()
    pos = 0
    registers = dict(a=a, b=b, c=c, d=d)
    while True:
        i += 1
        if (t2 := time.time()) > (t + 10):
            print(f'{i / (t2 - t):.1e} loc/s')
            i = 0
            t = t2
        code = lines[pos]
        #print(f'{str(code):<20} {pos=} {registers=}')
        if code[0] == 'inc':
            registers[code[1]] += 1
            pos += 1
        elif code[0] =='dec':
            registers[code[1]] -= 1
            pos += 1
        elif code[0] == 'cpy':
            if isinstance(code[-1], int):
                pass
            value = code[-2] if isinstance(code[-2], int) else registers[code[-2]]
            registers[code[-1]] = value
            pos += 1
        elif code[0] == 'jnz' :
            x = code[-2] if isinstance(code[-2], int) else registers[code[-2]]
            value = code[-1] if isinstance(code[-1], int) else registers[code[-1]]
            if x != 0:
                pos += value
            else:
                pos += 1
        elif code[0] == 'tgl':
            value = code[-1] if isinstance(code[-1], int) else registers[code[-1]]
            linenr = pos + value
            if linenr < 0 or linenr >= len(lines):
                pass
            elif lines[linenr][0] == 'inc':
                lines[linenr][0] = 'dec'
            elif len(lines[linenr]) == 2:
                lines[linenr][0] = 'inc'
            elif lines[linenr][0] == 'jnz':
                lines[linenr][0] = 'cpy'
            elif len(lines[linenr]) == 3:
                lines[linenr][0] = 'jnz'
            pos += 1
        else:
            raise ValueError(code)
        if pos >= len(lines):
            break
    return registers['a']


assert task1('test_input.txt') == 3
print(task1('input.txt', a=7))

print(task1('input.txt', a=12))
