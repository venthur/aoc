def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    s = ''
    s2 = ''
    for i in range(len(lines[0])):
        l = [line[i] for line in lines]
        if l.count('1') > l.count('0'):
            s += str(1)
            s2 += str(0)
        else:
            s += str(0)
            s2 += str(1)

    v = int(s, 2)
    v2 = int(s2, 2)
    return v * v2


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    cols = len(lines[0])

    lines_o = lines[:]
    for i in range(cols):
        col = list(zip(*lines_o))[i]
        v = '1' if col.count('1') >= col.count('0') else '0'
        lines_bak = lines_o[:]
        for line in lines_bak:
            if line[i] != v:
                lines_o.remove(line)
            if len(lines_o) == 1:
                break
        if len(lines_o) == 1:
            break
    ox = lines_o[0]

    lines_c = lines[:]
    for i in range(cols):
        col = list(zip(*lines_c))[i]
        v = '0' if col.count('0') <= col.count('1') else '1'
        lines_bak = lines_c[:]
        for line in lines_bak:
            if line[i] != v:
                lines_c.remove(line)
            if len(lines_c) == 1:
                break
        if len(lines_c) == 1:
            break
    co = lines_c[0]

    ox = int(ox, 2)
    co = int(co, 2)

    return ox * co


assert task1('test_input.txt') == 198
print(task1('input.txt'))

assert task2('test_input.txt') == 230
print(task2('input.txt'))
