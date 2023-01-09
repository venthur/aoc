from itertools import pairwise


def task1(fn_or_data):
    if isinstance(fn_or_data, int):
        data = str(fn_or_data)
    else:
        with open(fn_or_data) as fh:
            data = fh.read().strip()

    sum = 0
    for a, b in pairwise(data):
        if a == b:
            sum += int(a)
    if data[-1] == data[0]:
        sum += int(data[-1])

    return sum


def task2(fn_or_data):
    if isinstance(fn_or_data, int):
        data = str(fn_or_data)
    else:
        with open(fn_or_data) as fh:
            data = fh.read().strip()

    sum = 0
    for i, a in enumerate(data):
        b = data[(i + len(data) // 2) % len(data)]
        if a == b:
            sum += int(a)

    return sum


assert task1(1122) == 3
assert task1(1111) == 4
assert task1(1234) == 0
assert task1(91212129) == 9
print(task1('input.txt'))

assert task2(1212) == 6
assert task2(1221) == 0
assert task2(123425) == 4
assert task2(123123) == 12
assert task2(12131415) == 4
print(task2('input.txt'))
