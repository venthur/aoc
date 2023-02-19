from collections import defaultdict, deque


def read_input(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    maze = defaultdict(lambda: '#')
    letters = defaultdict(lambda: ' ')
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char in '.#':
                maze[x, y] = char
            else:
                letters[x, y] = char

    portals = defaultdict(list)
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                for px, py in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                    if maze[px, py] == '.':
                        if px > x:
                            name = letters[x-1, y] + letters[x, y]
                        elif px < x:
                            name = letters[x, y] + letters[x+1, y]
                        elif py > y:
                            name = letters[x, y-1] + letters[x, y]
                        elif py < y:
                            name = letters[x, y] + letters[x, y+1]
                        portals[name].append((px, py))

    return maze, portals


def task1(fn):
    maze, portals = read_input(fn)
    start = portals.pop('AA')[0]
    end = portals.pop('ZZ')[0]

    pmap = dict()
    for (x1, y1), (x2, y2) in portals.values():
        pmap[x1, y1] = (x2, y2)
        pmap[x2, y2] = (x1, y1)

    # bfs
    dq = deque([(start, 0)])
    visited = {start}
    while dq:
        (x, y), d = dq.popleft()
        if (x, y) == end:
            return d
        for xi, yi in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            d2 = d+1
            if (xi, yi) in pmap:
                xi, yi = pmap[xi, yi]
                d2 += 1
            if (xi, yi) not in visited and maze[xi, yi] == '.':
                visited.add((xi, yi))
                dq.append(((xi, yi), d2))


def task2(fn):
    maze, portals = read_input(fn)
    start = (*portals.pop('AA')[0], 0)
    end = (*portals.pop('ZZ')[0], 0)

    pmap = dict()
    for (x1, y1), (x2, y2) in portals.values():
        pmap[x1, y1] = (x2, y2)
        pmap[x2, y2] = (x1, y1)

    xs, ys = zip(*pmap.keys())
    x_outer = (min(xs), max(xs))
    y_outer = (min(ys), max(ys))

    # bfs
    dq = deque([(*start, 0)])
    visited = {(*start, 0)}
    while dq:
        x, y, l, d = dq.popleft()
        if (x, y, l) == end:
            return d
        for xi, yi in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            d2 = d+1
            l2 = l
            if (xi, yi) in pmap:
                is_outer = xi in x_outer or yi in y_outer
                if l > 0 or not is_outer:
                    xi, yi = pmap[xi, yi]
                    d2 += 1
                    l2 = l2-1 if is_outer else l2+1
                else:
                    continue
            if (xi, yi, l2) not in visited and maze[xi, yi] == '.':
                visited.add((xi, yi, l2))
                dq.append((xi, yi, l2, d2))


assert task1('test_input0.txt') == 23
print(task1('input.txt'))

assert task2('test_input1.txt') == 396
print(task2('input.txt'))
