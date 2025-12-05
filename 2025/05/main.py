from itertools import combinations

def task1(fn):
    with open(fn) as fh:
        data = fh.read()

    rangeblock, numberblock = data.split('\n\n')

    ranges = []
    for line in rangeblock.splitlines():
        lo, hi = line.split('-')
        ranges.append([int(lo), int(hi)])

    numbers = []
    for line in numberblock.splitlines():
        numbers.append(int(line))

    fresh = 0
    for n in numbers:
        for lo, hi in ranges:
            if lo <= n <= hi:
                fresh += 1
                break

    return fresh


def task2(fn):
    with open(fn) as fh:
        data = fh.read()

    rangeblock, _ = data.split('\n\n')

    ranges = []
    for line in rangeblock.splitlines():
        lo, hi = line.split('-')
        ranges.append([int(lo), int(hi)])

    while True:
        for (l1, h1), (l2, h2) in combinations(ranges, 2):
            if (h1 < l2 or h2 < l1):
                continue
            l = min(l1, l2)
            h = max(h1, h2)

            new_ranges = [[l, h]]
            for c in ranges:
                if c in ([l1, h1], [l2, h2]):
                    continue
                new_ranges.append(c)
            ranges = new_ranges[:]
            break
        else:
            break

    count = 0
    for l, h in ranges:
        count += h-l+1

    return count


assert task1('test_input.txt') == 3
print(task1('input.txt'))

assert task2('test_input.txt') == 14
print(task2('input.txt'))
