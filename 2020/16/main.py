def task1(fn):
    with open(fn) as fh:
        rules, ours, others = fh.read().split('\n\n')

    valid = set()
    for rule in rules.splitlines():
        r = ''.join([c if c.isnumeric() else ' ' for c in rule])
        r = [int(n) for n in r.split()]
        for i in range(r[0], r[1]+1):
            valid.add(i)
        for i in range(r[2], r[3]+1):
            valid.add(i)

    others = others.splitlines()[1:]
    error_rate = 0
    for line in others:
        for n in line.split(','):
            if int(n) not in valid:
                error_rate += int(n)

    return error_rate


def task2(fn):
    with open(fn) as fh:
        rules, our, others = fh.read().split('\n\n')

    # all valid values per field
    valids = []
    for rule in rules.splitlines():
        r = ''.join([c if c.isnumeric() else ' ' for c in rule])
        r = [int(n) for n in r.split()]
        valid = set()
        for i in range(r[0], r[1]+1):
            valid.add(i)
        for i in range(r[2], r[3]+1):
            valid.add(i)
        valids.append(valid)

    our = our.splitlines()[-1]
    our = [int(n) for n in our.split(',')]

    others = others.splitlines()[1:]
    others = [[int(n) for n in line.split(',')] for line in others]
    others = list(filter(lambda n: set(n) <= set.union(*valids), others))

    by_id = list(zip(*(others + [our])))

    possible_ids = []
    for i, ids in enumerate(by_id):
        p = []
        for j, v in enumerate(valids):
            if set(ids) <= v:
                p.append(j)
        possible_ids.append(p)

    removed = True
    while removed:
        removed = False
        for i, pids in enumerate(possible_ids):
            if len(pids) == 1:
                for j, pids2 in enumerate(possible_ids):
                    if j == i:
                        continue
                    if pids[0] in pids2:
                        pids2.remove(pids[0])
                        removed = True

    ids = [int(n[0]) for n in possible_ids]
    prod = 1
    for i, id_ in enumerate(ids):
        if id_ <= 5:
            prod *= our[i]

    return prod


print(task1('input.txt'))
print(task2('input.txt'))
