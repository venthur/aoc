def task1(fn):
    with open(fn) as fh:
        left, right = [], []
        for line in fh.read().splitlines():
            a, b = line.split()
            a = int(a)
            b = int(b)
            left.append(a)
            right.append(b)
        left.sort()
        right.sort()

    return sum(map(lambda x, y: abs(x - y), left, right))


def task2(fn):
    with open(fn) as fh:
        left, right = [], []
        for line in fh.read().splitlines():
            a, b = line.split()
            a = int(a)
            b = int(b)
            left.append(a)
            right.append(b)

    return sum(map(lambda x: x * right.count(x), left))


assert task1('test_input.txt') == 11
print(task1('input.txt'))

assert task2('test_input.txt') == 31
print(task2('input.txt'))
