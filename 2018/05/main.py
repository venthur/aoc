def task1(fn):
    with open(fn) as fh:
        data = fh.read().strip()

    len_old = None
    while len_old != len(data):
        len_old = len(data)
        for c2 in 'abcdefghijklmnopqrstuvwxyz':
            data = data.replace(''.join([c2, c2.upper()]), '', -1)
            data = data.replace(''.join([c2.upper(), c2]), '', -1)

    return len(data)


def task2(fn):
    with open(fn) as fh:
        data = fh.read().strip()

    minl = None
    for c in 'abcdefghijklmnopqrstuvwxyz':
        data2 = data.replace(c, '', -1).replace(c.upper(), '', -1)

        len_old = None
        while len_old != len(data2):
            len_old = len(data2)
            for c2 in 'abcdefghijklmnopqrstuvwxyz':
                data2 = data2.replace(''.join([c2, c2.upper()]), '', -1)
                data2 = data2.replace(''.join([c2.upper(), c2]), '', -1)

        if minl is None or len(data2) < minl:
            minl = len(data2)

    return minl


assert task1('test_input.txt') == 10
print(task1('input.txt'))

assert task2('test_input.txt') == 4
print(task2('input.txt'))
