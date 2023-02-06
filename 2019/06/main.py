def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    pairs = [line.split(')') for line in lines]

    def len_(obj, pairs):
        if obj == 'COM':
            return 0
        for a, b in pairs:
            if b == obj:
                if a == 'COM':
                    return 1
                else:
                    return 1 + len_(a, pairs)

    objects = {a for a, _ in pairs} | {b for _, b in pairs}
    orbits = 0
    for o in objects:
        orbits += len_(o, pairs)

    return orbits


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    pairs = [line.split(')') for line in lines]

    def path(obj, pairs):
        if obj == 'COM':
            return [obj]
        for a, b in pairs:
            if b == obj:
                if a == 'COM':
                    return [a, b]
                else:
                    return path(a, pairs) + [b]

    p1 = path('YOU', pairs)
    p2 = path('SAN', pairs)
    while p1[0] == p2[0]:
        p1.pop(0)
        p2.pop(0)

    return len(p1) + len(p2) - 2


assert task1('test_input0.txt') == 42
print(task1('input.txt'))

assert task2('test_input1.txt') == 4
print(task2('input.txt'))
