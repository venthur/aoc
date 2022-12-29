def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    ranges = []
    for line in lines:
        a, b = line.split('-')
        ranges.append((int(a), int(b)))
    ranges.sort()

    candidate = 0
    for a, b in ranges:
        print(a, b, candidate)
        if candidate >= a and candidate <= b:
            candidate = b + 1

    return candidate


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    ranges = []
    for line in lines:
        a, b = line.split('-')
        ranges.append((int(a), int(b)))
    ranges.sort()

    valid = 0
    i = 0
    while i < 2**32:
        for a, b in ranges:
            if i >= a and i <= b:
                i = b
                break
        else:
            valid += 1
        i += 1
    return valid


assert task1('test_input.txt') == 3
print(task1('input.txt'))

print(task2('input.txt'))
