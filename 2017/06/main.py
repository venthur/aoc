from itertools import count


def task1(fn_or_data):
    if isinstance(fn_or_data, list):
        banks = fn_or_data[:]
    else:
        with open(fn_or_data) as fh:
            banks = [int(data.strip()) for data in fh.read().split()]

    seen = set()
    seen.add(tuple(banks))
    for round in count(1):
        v = max(banks)
        i = banks.index(v)
        banks[i] = 0
        for j in range(v):
            banks[(i+j+1) % len(banks)] += 1
        if tuple(banks) not in seen:
            seen.add(tuple(banks))
        else:
            return round


def task2(fn_or_data):
    if isinstance(fn_or_data, list):
        banks = fn_or_data[:]
    else:
        with open(fn_or_data) as fh:
            banks = [int(data.strip()) for data in fh.read().split()]

    seen = set()
    seen.add(tuple(banks))
    when = dict()
    when[tuple(banks)] = 0
    for round in count(1):
        v = max(banks)
        i = banks.index(v)
        banks[i] = 0
        for j in range(v):
            banks[(i+j+1) % len(banks)] += 1
        if tuple(banks) not in seen:
            seen.add(tuple(banks))
            when[tuple(banks)] = round
        else:
            return round - when[tuple(banks)]


assert task1([0, 2, 7, 0]) == 5
print(task1('input.txt'))

assert task2([0, 2, 7, 0]) == 4
print(task2('input.txt'))
