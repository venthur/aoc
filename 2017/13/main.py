from itertools import count


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    layer = dict()
    for line in lines:
        depth, range_ = [int(i.strip()) for i in line.split(':')]
        layer[depth] = range_

    severity = 0
    for depth, range_ in layer.items():
        e = range_ * 2 - 2
        if depth % e == 0:
            severity += depth * range_

    return severity


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    layer = dict()
    for line in lines:
        depth, range_ = [int(i.strip()) for i in line.split(':')]
        layer[depth] = range_

    for delay in count():
        for depth, range_ in layer.items():
            e = range_ * 2 - 2
            if (depth + delay) % e == 0:
                break
        else:
            return delay


assert task1('test_input.txt') == 24
print(task1('input.txt'))

assert task2('test_input.txt') == 10
print(task2('input.txt'))
