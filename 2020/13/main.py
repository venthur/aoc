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


assert task1('test_input0.txt') == 295
print(task1('input.txt'))
