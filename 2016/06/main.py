def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    nchars = len(lines[0])
    l = [dict() for i in range(nchars)]
    for line in lines:
        for i, c in enumerate(line):
            l[i][c] = l[i].get(c, 0) + 1

    result = []
    for i in range(nchars):
        l[i] = list(l[i].items())
        l[i].sort(key=lambda x: x[1], reverse=True)
        result.append(l[i][0][0])

    return ''.join(result)


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    nchars = len(lines[0])
    l = [dict() for i in range(nchars)]
    for line in lines:
        for i, c in enumerate(line):
            l[i][c] = l[i].get(c, 0) + 1

    result = []
    for i in range(nchars):
        l[i] = list(l[i].items())
        l[i].sort(key=lambda x: x[1])
        result.append(l[i][0][0])

    return ''.join(result)

assert task1('test_input.txt') == 'easter'
print(task1('input.txt'))

assert task2('test_input.txt') == 'advent'
print(task2('input.txt'))
