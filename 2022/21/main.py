def read_input(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    return lines


def task1(fn):
    lines = read_input(fn)

    known = dict()
    while 'root' not in known:
        for i, line in enumerate(lines):
            name, val = line.split(': ')
            if val.isnumeric():
                known[name] = int(val)
                lines.pop(i)
                break
            else:
                op1, o, op2 = val.split()
                if op1 in known and op2 in known:
                    v = {
                        '+': lambda a, b: a + b,
                        '-': lambda a, b: a - b,
                        '*': lambda a, b: a * b,
                        '/': lambda a, b: a // b,
                    }[o](known[op1], known[op2])
                    known[name] = v
                    lines.pop(i)
                    break

    return known['root']


def task2(fn):
    lines = read_input(fn)
    # change root to subtraction and remove humn
    for i, line in enumerate(lines):
        if line.startswith('root'):
            l = line.replace('+', '-').replace('*', '-').replace('/', '-')
            lines.pop(i)
            lines.append(l)
            break
    for i, line in enumerate(lines):
        if line.startswith('humn'):
            lines.pop(i)
            break

    def cmp(humn, lines):
        known = dict(humn=humn)
        while 'root' not in known:
            for i, line in enumerate(lines):
                name, val = line.split(': ')
                if val.isnumeric():
                    known[name] = int(val)
                    lines.pop(i)
                    break
                else:
                    op1, o, op2 = val.split()
                    if op1 in known and op2 in known:
                        v = {
                            '+': lambda a, b: a + b,
                            '-': lambda a, b: a - b,
                            '*': lambda a, b: a * b,
                            '/': lambda a, b: a // b,
                        }[o](known[op1], known[op2])
                        known[name] = v
                        lines.pop(i)
                        break

        if known['root'] > 0:
            return 1
        elif known['root'] < 0:
            return -1
        else:
            return 0


    lo, hi = -int(1e32), int(1e32)
    while lo < hi:
        i = (lo + hi) // 2
        res = cmp(i, lines[:])
        if res == 0:
            return i
        elif res > 0:
            hi = i
        else:
            lo = i

    lo, hi = -int(1e32), int(1e32)
    while lo < hi:
        i = (lo + hi) // 2
        res = cmp(i, lines[:])
        if res == 0:
            return i
        elif res < 0:
            hi = i
        else:
            lo = i


assert task1('test_input0.txt') == 152
print(task1('input.txt'))

assert task2('test_input0.txt') == 301
print(task2('input.txt'))
