from collections import defaultdict


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()
    lines.sort()

    current_guard = None
    guards = defaultdict(lambda: [])
    for line in lines:
        if line.endswith('begins shift'):
            current_guard = int(line.split()[-3][1:])
        else:
            time = line.split()[1][:-1]
            hour, mins = [int(i) for i in time.split(':')]
            assert hour == 0
            guards[current_guard].append(mins)

    max_hours = 0
    g = None
    for guard, mins in guards.items():
        s = sum(map(lambda even, odd: odd-even, mins[0::2], mins[1::2]))
        if s > max_hours:
            max_hours = s
            g = guard

    counter = [0 for i in range(60)]
    start = guards[g][0::2]
    end = guards[g][1::2]
    for s, e in zip(start, end):
        for i in range(s, e):
            counter[i] += 1

    longest = None
    for i, c in enumerate(counter):
        if longest is None or c > counter[longest]:
            longest = i

    return longest * g


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()
    lines.sort()

    current_guard = None
    guards = defaultdict(lambda: [])
    for line in lines:
        if line.endswith('begins shift'):
            current_guard = int(line.split()[-3][1:])
        else:
            time = line.split()[1][:-1]
            hour, mins = [int(i) for i in time.split(':')]
            assert hour == 0
            guards[current_guard].append(mins)

    maxg = None
    max_ = [0]
    for g, mins in guards.items():

        counter = [0 for i in range(60)]
        start = mins[0::2]
        end = mins[1::2]
        for s, e in zip(start, end):
            for i in range(s, e):
                counter[i] += 1

        guards[g] = counter
        if max(counter) > max(max_):
            max_ = counter[:]
            maxg = g

    return maxg * max_.index(max(max_))


print(task1('input.txt'))

print(task2('input.txt'))
