def task1(fn):
    with open(fn) as fh:
        ts, ids = fh.read().splitlines()

    ts = int(ts)
    ids = [int(n) for n in ids.split(',') if n.isnumeric()]

    earliest, id_ = None, None
    for i in ids:
        t = ((ts // i) + 1) * i
        if earliest is None or t < earliest:
            earliest = t
            id_ = i
    return (earliest - ts) * id_


def task2(fn):
    with open(fn) as fh:
        ts, ids = fh.read().splitlines()

    busses = [(i, int(n)) for i, n in enumerate(ids.split(',')) if n.isnumeric()]

    d = 1
    i = 0
    for offset, bus in busses:
        while True:
            i += d
            if (i + offset) % bus == 0:
                d *= bus
                break

    return i


assert task1('test_input0.txt') == 295
print(task1('input.txt'))

assert task2('test_input0.txt') == 1068781
print(task2('input.txt'))
