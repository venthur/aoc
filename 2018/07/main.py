def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    lines = [(line.split()[1], line.split()[-3]) for line in lines]

    rules = dict()
    for a, b in lines:
        if b not in rules:
            rules[b] = [a]
        else:
            rules[b].append(a)
        if a not in rules:
            rules[a] = []

    order = []
    available = []

    for target, dependencies in rules.items():
        if all(True if d in order else False for d in dependencies):
            available.append(target)
    for a in available:
        if a in rules:
            rules.pop(a)

    while available:
        available.sort()
        current = available.pop(0)
        order.append(current)

        for target, dependencies in rules.items():
            if all(True if d in order else False for d in dependencies):
                available.append(target)
        for a in available:
            if a in rules:
                rules.pop(a)

    return ''.join(order)


def task2(fn, nworkers, seconds):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    lines = [(line.split()[1], line.split()[-3]) for line in lines]

    rules = dict()
    for a, b in lines:
        if b not in rules:
            rules[b] = [a]
        else:
            rules[b].append(a)
        if a not in rules:
            rules[a] = []

    order = []
    available = []
    workers = [0 for i in range(nworkers)]
    processing = []
    t = 0

    for target, dependencies in rules.items():
        if all(True if d in order else False for d in dependencies):
            available.append(target)
    for a in available:
        if a in rules:
            rules.pop(a)

    while available or processing or rules:

        ready = list(filter(lambda x: x[0] <= t, processing))
        processing = list(filter(lambda x: x[0] > t, processing))

        order += [c for _, c in ready]
        workers = [t if i < t else i for i in workers]

        for target, dependencies in rules.items():
            if all(True if d in order else False for d in dependencies):
                available.append(target)
        for a in available:
            if a in rules:
                rules.pop(a)

        while available:
            available.sort()
            current = available.pop(0)

            w = workers.index(min(workers))
            dt = ord(current) - ord('A') + 1 + seconds

            workers[w] += dt
            processing.append((workers[w], current))

        t += 1

    return t-1


assert task1('test_input.txt') == 'CABDFE'
print(task1('input.txt'))

assert task2('test_input.txt', 2, 0) == 15
print(task2('input.txt', 5, 60))
