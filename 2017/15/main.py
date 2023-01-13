def generator_a(seed):
    while True:
        seed *= 16807
        seed %= 2147483647
        yield seed


def generator_b(seed):
    while True:
        seed *= 48271
        seed %= 2147483647
        yield seed


def task1(fn_or_data):

    if isinstance(fn_or_data, list):
        seed_a, seed_b = fn_or_data
    else:
        with open(fn_or_data) as fh:
            lines = fh.read().splitlines()
        seed_a, seed_b = [int(line.split()[-1]) for line in lines]

    count = 0
    a = generator_a(seed_a)
    b = generator_b(seed_b)
    for i in range(40_000_000):
        sa = f'{next(a):0>32b}'
        sb = f'{next(b):0>32b}'
        if sa[16:] == sb[16:]:
            count += 1

    return count


def generator_a2(seed):
    while True:
        seed *= 16807
        seed %= 2147483647
        if seed % 4 == 0:
            yield seed


def generator_b2(seed):
    while True:
        seed *= 48271
        seed %= 2147483647
        if seed % 8 == 0:
            yield seed


def task2(fn_or_data):

    if isinstance(fn_or_data, list):
        seed_a, seed_b = fn_or_data
    else:
        with open(fn_or_data) as fh:
            lines = fh.read().splitlines()
        seed_a, seed_b = [int(line.split()[-1]) for line in lines]

    count = 0
    a = generator_a2(seed_a)
    b = generator_b2(seed_b)
    for i in range(5_000_000):
        sa = f'{next(a):0>32b}'
        sb = f'{next(b):0>32b}'
        if sa[16:] == sb[16:]:
            count += 1

    return count


assert task1([65, 8921]) == 588
print(task1('input.txt'))

assert task2([65, 8921]) == 309
print(task2('input.txt'))
