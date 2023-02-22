def task1(fn):
    with open(fn) as fh:
        blocks = [b.split() for b in fh.read().split('\n\n')]

    qs = 0
    for block in blocks:
        qs += len(set(list(''.join(block))))

    # pt 1
    print(qs)

    qs = 0
    for block in blocks:
        sets = [set(list(b)) for b in block]
        s = sets[0]
        for i in range(1, len(sets)):
            s.intersection_update(sets[i])
        qs += len(s)

    # pt 2
    print(qs)


task1('input.txt')
