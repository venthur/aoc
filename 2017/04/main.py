from itertools import combinations


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    n_valid = 0
    for line in lines:
        valid = True
        for a, b in combinations(line.split(), 2):
            if a == b:
                valid = False
                break
        if valid:
            n_valid += 1

    return n_valid


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    n_valid = 0
    for line in lines:
        valid = True
        for a, b in combinations(line.split(), 2):
            if sorted(list(a)) == sorted(list(b)):
                valid = False
                break
        if valid:
            n_valid += 1

    return n_valid


print(task1('input.txt'))

print(task2('input.txt'))
