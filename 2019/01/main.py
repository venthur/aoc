def task1(fn):
    with open(fn) as fh:
        numbers = [int(n) for n in fh.read().splitlines()]

    return sum([n // 3 - 2 for n in numbers])


def task2(fn):
    with open(fn) as fh:
        numbers = [int(n) for n in fh.read().splitlines()]

    total = 0
    for n in numbers:
        add = n // 3 - 2
        while add > 0:
            total += add
            add = add // 3 - 2

    return total


print(task1('input.txt'))

print(task2('input.txt'))
