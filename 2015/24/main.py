def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    weights = [int(i) for i in lines]
    target = sum(weights) // 3

    sets = [[[], 0, 0]]
    for w in weights[::-1]:
        sets2 = set()
        for a, b, c in sets:
            if sum(list(a) + [w]) <= target:
                sets2.add((tuple(list(a) + [w]), *sorted((b, c))))
            if b + w <= target:
                sets2.add((tuple(a), *sorted((b + w, c))))
            if c + w <= target:
                sets2.add((tuple(a), *sorted((b, c + w))))
        sets = list(sets2)

    candiates = [a for [a, b, c] in sets if sum(a) == b == c == target]

    minl = None
    for a in candiates:
        if minl is None or len(a) < minl:
            minl = len(a)
    candidates = [a for a in candiates if len(a) == minl]

    minp = None
    for a in candidates:
        p = 1
        for i in a:
            p *= i
        if minp is None or p < minp:
            minp = p

    return minp


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    weights = [int(i) for i in lines]
    target = sum(weights) // 4

    sets = [[[], 0, 0, 0]]
    for w in weights[::-1]:
        sets2 = set()
        for a, b, c, d in sets:
            if sum(list(a) + [w]) <= target:
                sets2.add((tuple(list(a) + [w]), *sorted((b, c, d))))
            if b + w <= target:
                sets2.add((tuple(a), *sorted((b + w, c, d))))
            if c + w <= target:
                sets2.add((tuple(a), *sorted((b, c + w, d))))
            if d + w <= target:
                sets2.add((tuple(a), *sorted((b, c, d + w))))
        sets = list(sets2)

    candiates = [a for [a, b, c, d] in sets if sum(a) == b == c == d == target]

    minl = None
    for a in candiates:
        if minl is None or len(a) < minl:
            minl = len(a)
    candidates = [a for a in candiates if len(a) == minl]

    minp = None
    for a in candidates:
        p = 1
        for i in a:
            p *= i
        if minp is None or p < minp:
            minp = p

    return minp

assert task1('test_input.txt') == 99
print(task1('input.txt'))

assert task2('test_input.txt') == 44
print(task2('input.txt'))
