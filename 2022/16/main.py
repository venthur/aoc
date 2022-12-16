from itertools import permutations, pairwise
import re


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    flow = dict()
    conn = dict()
    for line in lines:
        print(line)
        name, rate, connects = re.match(
            r'^.*?([A-Z]{2,2}).*?(\d+).*?((?:[A-Z]{2,2}, )+[A-Z]{2,2}|[A-Z]{2,2})$',
            line
        ).groups()
        rate = int(rate)
        connects = [c.strip() for c in connects.split(',')]
        flow[name] = rate
        conn[name] = connects

    pressurized = set()
    # get the set of valves you'd want to open
    for n, r in flow.items():
        if r > 0:
            pressurized.add(n)
    print(pressurized)

    # get the shortest distances between them
    dist = dict()
    for a in flow.keys():
        stack = [(a, 0)]
        visited = set()
        while True:
            try:
                b, i = stack.pop(0)
                visited.add(b)
                i += 1
            except IndexError:
                break
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
    print(dist)

    best_pressure = 0
    # i suspect we don't need to go through all 15! permutations as we need
    # some valves in between as well
    for i, p in enumerate(permutations(pressurized, min(len(pressurized), 8))):
        s_left = 30
        pressure = 0

        d = dist['AA', p[0]]
        s_left -= d + 1
        pressure += flow[p[0]] * s_left

        jumps = 1
        for a, b in pairwise(p):
            jumps += 1
            d = dist[a, b]
            if d + 1 <= s_left:
                s_left -= d + 1
            else:
                break
            if s_left >= 1:
                pressure += flow[b] * s_left
            else:
                break
        print(f'Permutation: {i} {p} ({best_pressure=} {jumps=})')

        if pressure > best_pressure:
            best_pressure = pressure

    return best_pressure


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    flow = dict()
    conn = dict()
    for line in lines:
        print(line)
        name, rate, connects = re.match(
            r'^.*?([A-Z]{2,2}).*?(\d+).*?((?:[A-Z]{2,2}, )+[A-Z]{2,2}|[A-Z]{2,2})$',
            line
        ).groups()
        rate = int(rate)
        connects = [c.strip() for c in connects.split(',')]
        flow[name] = rate
        conn[name] = connects

    pressurized = set()
    # get the set of valves you'd want to open
    for n, r in flow.items():
        if r > 0:
            pressurized.add(n)
    print(pressurized)

    # get the shortest distances between them
    dist = dict()
    for a in flow.keys():
        stack = [(a, 0)]
        visited = set()
        while True:
            try:
                b, i = stack.pop(0)
                visited.add(b)
                i += 1
            except IndexError:
                break
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
    print(dist)

    best_pressure = 0
    # i suspect we don't need to go through all 15! permutations as we need
    # some valves in between as well
    for p in permutations(pressurized, len(pressurized) // 2):

        s_left = 26
        pressure = 0

        d = dist['AA', p[0]]
        s_left -= d + 1
        pressure += flow[p[0]] * s_left

        jumps = 1
        for a, b in pairwise(p):
            jumps += 1
            d = dist[a, b]
            if d + 1 <= s_left:
                s_left -= d + 1
            else:
                break
            if s_left >= 1:
                pressure += flow[b] * s_left
            else:
                break

        rest = pressurized - set(p)
        for p2 in permutations(rest):

            s_left = 26
            pressure2 = 0

            d = dist['AA', p2[0]]
            s_left -= d + 1
            pressure2 += flow[p2[0]] * s_left

            jumps = 1
            for a, b in pairwise(p2):
                jumps += 1
                d = dist[a, b]
                if d + 1 <= s_left:
                    s_left -= d + 1
                else:
                    break
                if s_left >= 1:
                    pressure2 += flow[b] * s_left
                else:
                    break
            print(f'Permutation: {p} {p2} ({best_pressure=})')

            if pressure + pressure2 > best_pressure:
                best_pressure = pressure + pressure2

    print(best_pressure)
    return best_pressure


#assert task1('test_input.txt') == 1651
#print(task1('input.txt'))


assert task2('test_input.txt') == 1707
print(task2('input.txt'))
