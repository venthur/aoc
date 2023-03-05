from collections import deque


def task1(fn, days):
    with open(fn) as fh:
        numbers = [int(n) for n in fh.read().split(',')]

    totals = deque(numbers.count(i) for i in range(9))
    for _ in range(days):
        totals.rotate(-1)
        totals[6] += totals[8]

    return sum(totals)

assert task1('test_input0.txt', 80) == 5934
print(task1('input.txt', 80))
print(task1('input.txt', 256))
