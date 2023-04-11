from math import lcm
from heapq import heappush, heappop


def read_input(fn):
    with open(fn) as fh:
        data = fh.read().splitlines()

    rows = len(data)
    cols = len(data[0])

    states = lcm(rows-2, cols-2)

    grid = [dict() for _ in range(states)]
    for y, lines in enumerate(data):
        for x, char in enumerate(lines):
            grid[0][x, y] = char

            for t in range(1, states):
                grid[t][x, y] = '#' if char == '#' else '.'

    for y, lines in enumerate(data):
        for x, char in enumerate(lines):
            if char in '<>v^':
                xi, yi = x, y
                for t in range(1, states):
                    if char == '>':
                        xi = 1 if xi == cols-2 else xi + 1
                    elif char == '<':
                        xi = cols-2 if xi == 1 else xi - 1
                    elif char == '^':
                        yi = rows-2 if yi == 1 else yi - 1
                    elif char == 'v':
                        yi = 1 if yi == rows-2 else yi + 1
                    grid[t][xi, yi] = char

    start = (1, 0)
    end = (cols-2, rows-1)
    return grid, start, end


def dijkstra(start, end, t_start, grid):
    states = len(grid)

    visited = set()
    queue = []
    heappush(queue, (t_start, start))
    while queue:
        t, (x, y) = heappop(queue)
        if (x, y) == end:
            return t - t_start

        tnext = t+1
        tnext_wrapped = tnext % states
        if (t, x, y) not in visited:
            visited.add((t, x, y))
            # explode
            for xi, yi in ((x, y-1), (x+1, y), (x, y+1), (x-1, y), (x, y)):
                if (
                    (xi, yi) in grid[tnext_wrapped] and
                    grid[tnext_wrapped][xi, yi] == '.'
                ):
                    heappush(queue, (tnext, (xi, yi)))


def task1(fn):
    grid, start, end = read_input(fn)

    return dijkstra(start, end, 0, grid)


def task2(fn):
    grid, start, end = read_input(fn)

    t = dijkstra(start, end, 0, grid)
    t += dijkstra(end, start, t, grid)
    t += dijkstra(start, end, t, grid)

    return t


assert task1('test_input.txt') == 18
print(task1('input.txt'))

assert task2('test_input.txt') == 54
print(task2('input.txt'))
