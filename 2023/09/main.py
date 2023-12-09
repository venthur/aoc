from itertools import pairwise


def predict_next(numbers):
    if all(v == 0 for v in numbers):
        return 0

    diffs = [b - a for a, b in pairwise(numbers)]

    return numbers[-1] + predict_next(diffs)


def task1(fn):
    report = []
    with open(fn) as fh:
        for line in fh.read().splitlines():
            numbers = list(map(int, line.split()))
            report.append(numbers)

    result = 0
    for numbers in report:
        result += predict_next(numbers)

    return result


def predict_first(numbers):
    if all(v == 0 for v in numbers):
        return 0

    diffs = [b - a for a, b in pairwise(numbers)]

    return numbers[0] - predict_first(diffs)


def task2(fn):
    report = []
    with open(fn) as fh:
        for line in fh.read().splitlines():
            numbers = list(map(int, line.split()))
            report.append(numbers)

    result = 0
    for numbers in report:
        result += predict_first(numbers)

    return result


assert task1('test_input.txt') == 114
print(task1('input.txt'))

assert task2('test_input.txt') == 2
print(task2('input.txt'))
