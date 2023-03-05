from itertools import accumulate


def task1(fn):
    with open(fn) as fh:
        numbers = [int(n) for n in fh.read().split(',')]

    fuel = None
    for pos in range(min(numbers), max(numbers)+1):
        f = sum(map(lambda x: abs(x - pos), numbers))
        if not fuel:
            fuel = f
        fuel = min(fuel, f)

    return fuel


def task2(fn):
    with open(fn) as fh:
        numbers = [int(n) for n in fh.read().split(',')]

    fuel = None
    for pos in range(min(numbers), max(numbers)+1):
        f = sum(
            map(
                lambda x:
                list(accumulate(range(1, abs(x - pos)+1)))[-1] if abs(x - pos) > 0 else 0,
                numbers
            )
        )
        if not fuel:
            fuel = f
        fuel = min(fuel, f)

    return fuel


assert task1('test_input0.txt') == 37
print(task1('input.txt'))

assert task2('test_input0.txt') == 168
print(task2('input.txt'))
