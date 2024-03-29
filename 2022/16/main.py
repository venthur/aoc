from itertools import combinations
import re


def parse_input(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    flow = dict()
    conn = dict()
    for line in lines:
        name, rate, connects = re.match(
            r'^.*?([A-Z]{2,2}).*?(\d+).*?((?:[A-Z]{2,2}, )+[A-Z]{2,2}|[A-Z]{2,2})$',
            line
        ).groups()
        rate = int(rate)
        connects = [c.strip() for c in connects.split(',')]
        flow[name] = rate
        conn[name] = connects

    return flow, conn


def task1(fn):
    flow, conn = parse_input(fn)

    pressurized = set()
    # get the set of valves you'd want to open
    for n, r in flow.items():
        if r > 0:
            pressurized.add(n)

    # get the shortest distances between them
    dist = dict()
    for a in flow.keys():
        stack = [(a, 0)]
        visited = set()
        while stack:
            b, i = stack.pop(0)
            visited.add(b)
            i += 1
            for c in conn[b]:
                if (a, c) in dist:
                    d = dist[a, c]
                    if i < d:
                        dist[a, c] = i
                        dist[c, a] = i
                else:
                    dist[a, c] = i
                    dist[c, a] = i
                if c not in visited:
                    stack.append((c, i))

    best = 0
    todo = [['AA', set(), 30, 0]]
    while todo:
        todo.sort(key=lambda x: x[-1])
        pos, visited, seconds_left, pressure = todo.pop()

        if seconds_left <= 0 or visited == pressurized:
            best = max(best, pressure)
            continue

        for next in pressurized - visited:
            sl = seconds_left - dist[pos, next] - 1
            sl = 0 if sl < 0 else sl
            visited2 = visited.copy()
            visited2.add(next)
            pressure2 = pressure + sl * flow[next]
            for i, t in enumerate(todo):
                if visited2 <= t[1] and sl <= t[-2] and pressure2 <= t[-1]:
                    break
                elif visited2 >= t[1] and sl >= t[-2] and pressure2 >= t[-1]:
                    t[0] = next
                    t[1] = visited2
                    t[2] = sl
                    t[3] = pressure2
                    break
            else:
                todo.append([next, visited2, sl, pressure2])

    return best


def task2(fn):
    flow, conn = parse_input(fn)

    pressurized = set()
    # get the set of valves you'd want to open
    for n, r in flow.items():
        if r > 0:
            pressurized.add(n)

    # get the shortest distances between them
    dist = dict()
    for a in flow.keys():
        stack = [(a, 0)]
        visited = set()
        while stack:
            b, i = stack.pop(0)
            visited.add(b)
            i += 1
            for c in conn[b]:
                if (a, c) in dist:
                    d = dist[a, c]
                    if i < d:
                        dist[a, c] = i
                        dist[c, a] = i
                else:
                    dist[a, c] = i
                    dist[c, a] = i
                if c not in visited:
                    stack.append((c, i))

    best = dict()
    todo = [['AA', set(), 26, 0]]
    while todo:
        todo.sort(key=lambda x: x[-1])
        pos, visited, seconds_left, pressure = todo.pop()

        if seconds_left <= 0 or visited == pressurized:
            visited = tuple(sorted(list(visited)))
            if visited in best and best[visited] < pressure:
                best[visited] = pressure
            elif visited not in best:
                best[visited] = pressure

            continue

        for next in pressurized - visited:
            sl = seconds_left - dist[pos, next] - 1
            sl = 0 if sl < 0 else sl
            visited2 = visited.copy()
            visited2.add(next)
            pressure2 = pressure + sl * flow[next]
            todo.append([next, visited2, sl, pressure2])

    maxv = 0
    for (a, av), (b, bv) in combinations(best.items(), 2):
        if not set(a) & set(b):
            maxv = max(av + bv, maxv)

    return maxv


assert task1('test_input.txt') == 1651
print(task1('input.txt'))

print(task2('input.txt'))
