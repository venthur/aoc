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

    l = len(lines[0])
    n = ''.join(lines)
    print(n)

    for i in range(l):
        n[i::l]

    return ox * co


assert task1('test_input.txt') == 198
print(task1('input.txt'))

assert task2('test_input.txt') == 230
print(task2('input.txt'))