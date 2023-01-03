def task1(fn):
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

    def run(lines, registers, maxlen):
        pos = 0
        registers = registers.copy()
        out = []
        while True:
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
            elif code[0] == 'out':
                value = code[-1] if isinstance(code[-1], int) else registers[code[-1]]
                if value not in (0, 1):
                    return False
                if not out and value != 0:
                    return False
                elif not out and value == 0:
                    out.append(value)
                elif value == out[-1]:
                    return False
                else:
                    out.append(value)
                if len(out) == maxlen:
                    print(out)
                    return True
                pos += 1
            if pos >= len(lines):
                break
        return registers['a']

    from itertools import count
    for i in count():
        print(f'Trying {i}...')
        if run(lines, dict(a=i, b=0, c=0, d=0), 1000):
            return i

print(task1('input.txt'))
