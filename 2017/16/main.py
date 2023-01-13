def task1(fn):
    with open(fn) as fh:
        data = fh.read().strip()

    programs = list('abcdefghijklmnop')
    data = data.split(',')
    for move in data:
        c, p = move[0], move[1:]
        if c == 's':
            p = int(p)
            programs = programs[-p:] + programs[:-p]
        elif c == 'x':
            a, b = [int(i) for i in p.split('/')]
            c = programs[a]
            programs[a] = programs[b]
            programs[b] = c
        elif c == 'p':
            a, b = [i for i in p.split('/')]
            ai = programs.index(a)
            bi = programs.index(b)
            programs[ai] = b
            programs[bi] = a
    return ''.join(programs)


def task2(fn):
    with open(fn) as fh:
        data = fh.read().strip()

    programs = list('abcdefghijklmnop')
    data = data.split(',')
    data2 = []
    for move in data:
        c, p = move[0], move[1:]
        if c == 's':
            data2.append((c, int(p)))
        elif c == 'x':
            data2.append((c, [int(i) for i in p.split('/')]))
        elif c == 'p':
            data2.append((c, [i for i in p.split('/')]))
    data = data2[:]

    # check when we have the first repetition...
    for i in range(1000000000):
        for cmd, params in data:
            if cmd == 's':
                programs = programs[-params:] + programs[:-params]
            elif cmd == 'x':
                c = programs[params[0]]
                programs[params[0]] = programs[params[1]]
                programs[params[1]] = c
            elif cmd == 'p':
                ai = programs.index(params[0])
                bi = programs.index(params[1])
                programs[ai] = params[1]
                programs[bi] = params[0]
        if programs == list('abcdefghijklmnop'):
            break

    # ... and shorten
    for i in range(1000000000 % (i+1)):
        for cmd, params in data:
            if cmd == 's':
                programs = programs[-params:] + programs[:-params]
            elif cmd == 'x':
                c = programs[params[0]]
                programs[params[0]] = programs[params[1]]
                programs[params[1]] = c
            elif cmd == 'p':
                ai = programs.index(params[0])
                bi = programs.index(params[1])
                programs[ai] = params[1]
                programs[bi] = params[0]

    return ''.join(programs)


print(task1('input.txt'))
print(task2('input.txt'))
