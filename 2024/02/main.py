def read_input(fn):
    with open(fn) as fh:
        for line in fh:
            yield [int(n) for n in line.split()]


def is_increasing(l):
    return all(a <= b and 1 <= b - a <=3 for a, b in zip(l, l[1:]))


def task1(fn):
    count = 0
    for report in read_input(fn):
        if is_increasing(report) or is_increasing(report[::-1]):
            count += 1
    return count


def task2(fn):
    count = 0
    for report in read_input(fn):
        if is_increasing(report) or is_increasing(report[::-1]):
            count += 1
            continue
        for i in range(len(report)):
            r2 = report[:i] + report[i+1:]
            if is_increasing(r2) or is_increasing(r2[::-1]):
                count += 1
                break
    return count


assert task1('test_input.txt') == 2
print(task1('input.txt'))

assert task2('test_input.txt') == 4
print(task2('input.txt'))
