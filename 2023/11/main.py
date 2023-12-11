from itertools import combinations


def task1(fn, expansion=2):
    positions = []
    with open(fn) as fh:
        for y, line in enumerate(fh.read().splitlines()):
            for x, char in enumerate(line):
                if char != '.':
                    positions.append((x, y))
    maxx, maxy = x, y

    empty_rows = {y for y in range(maxy + 1)} - {y for x, y in positions}
    empty_cols = {x for x in range(maxx + 1)} - {x for x, y in positions}

    result = 0
    for a, b in combinations(positions, 2):
        d = abs(a[0] - b[0]) + abs(a[1] - b[1])
        for x in range(min(a[0], b[0]), max(a[0], b[0])):
            if x in empty_cols:
                d += expansion-1
        for y in range(min(a[1], b[1]), max(a[1], b[1])):
            if y in empty_rows:
                d += expansion-1
        result += d

    return result


assert task1('test_input.txt') == 374
print(task1('input.txt'))

assert task1('test_input.txt', expansion=10) == 1030
assert task1('test_input.txt', expansion=100) == 8410
print(task1('input.txt', expansion=1000000))
