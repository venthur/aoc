from math import sqrt
from itertools import permutations
import heapq


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    grid = dict()
    for line in lines:
        if line.startswith('root') or line.startswith('Filesystem'):
            continue
        dev, size, used, avail, use = line.split()
        x, y = dev.split('-')[-2:]
        x = int(x[1:])
        y = int(y[1:])
        node = {
            'size': int(size[:-1]),
            'used': int(used[:-1]),
            'avail': int(avail[:-1]),
            'use': int(use[:-1]),
        }
        grid[(x, y)] = node

    pairs = 0
    for a, b in permutations(list(grid.values()), 2):
        if a['used'] > 0 and a['used'] <= b['avail']:
            pairs += 1
    return pairs


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    grid = dict()
    goal = [0, 0]
    empty = []
    for line in lines:
        if line.startswith('root') or line.startswith('Filesystem'):
            continue
        dev, size, used, avail, use = line.split()
        x, y = dev.split('-')[-2:]
        x = int(x[1:])
        y = int(y[1:])
        if y == 0 and x > goal[0]:
            goal[0] = x
        node = {
            'size': int(size[:-1]),
            'used': int(used[:-1]),
        }
        if node['used'] == 0:
            empty = [x, y]
        grid[(x, y)] = node

    # get the boundaries
    maxx, maxy = 0, 0
    for x, y in grid.keys():
        if x > maxx:
            maxx = x
        if y > maxy:
            maxy = y

    def d(a, b):
        # distance
        return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

    def h(grid, goal, empty):
        # heuristik
        if goal == [0, 0]:
            return 0
        return d(goal, [0, 0]) + d(goal, empty)

    pq = []
    i = 0
    heapq.heappush(pq, [h(grid, goal, empty), i, grid.copy(), goal, empty, 0])
    seen = set()
    seen.add((*goal, *empty))
    while pq:
        f, _, grid, goal, empty, steps = heapq.heappop(pq)
        seen.add((*goal, *empty))
        if goal == [0, 0]:
            return steps
        # generate next steps
        ex, ey = empty

        xu, yu = ex, ey-1
        if ey > 0 and grid[xu, yu]['used'] <= grid[ex, ey]['size']:
            grid2 = grid.copy()
            tmp = grid2[xu, yu]
            grid2[xu, yu] = grid2[ex, ey]
            grid2[ex, ey] = tmp
            empty2 = [xu, yu]
            goal2 = goal[:]
            if goal2 == [xu, yu]:
                goal2 = [ex, ey]
            if (*goal2, *empty2) not in seen:
                i += 1
                heapq.heappush(pq, [h(grid2, goal2, empty2), i, grid2.copy(), goal2, empty2, steps+1])
                seen.add((*goal2, *empty2))

        xd, yd = ex, ey+1
        if ey < maxy and grid[xd, yd]['used'] <= grid[ex, ey]['size']:
            grid2 = grid.copy()
            tmp = grid2[xd, yd]
            grid2[xd, yd] = grid2[ex, ey]
            grid2[ex, ey] = tmp
            empty2 = [xd, yd]
            goal2 = goal[:]
            if goal2 == [xd, yd]:
                goal2 = [ex, ey]
            if (*goal2, *empty2) not in seen:
                i += 1
                heapq.heappush(pq, [h(grid2, goal2, empty2), i, grid2.copy(), goal2, empty2, steps+1])
                seen.add((*goal2, *empty2))

        xl, yl = ex-1, ey
        if ex > 0 and grid[xl, yl]['used'] <= grid[ex, ey]['size']:
            grid2 = grid.copy()
            tmp = grid2[xl, yl]
            grid2[xl, yl] = grid2[ex, ey]
            grid2[ex, ey] = tmp
            empty2 = [xl, yl]
            goal2 = goal[:]
            if goal2 == [xl, yl]:
                goal2 = [ex, ey]
            if (*goal2, *empty2) not in seen:
                i += 1
                heapq.heappush(pq, [h(grid2, goal2, empty2), i, grid2.copy(), goal2, empty2, steps+1])
                seen.add((*goal2, *empty2))

        xr, yr = ex+1, ey
        if ex < maxx and grid[xr, yr]['used'] <= grid[ex, ey]['size']:
            grid2 = grid.copy()
            tmp = grid2[xr, yr]
            grid2[xr, yr] = grid2[ex, ey]
            grid2[ex, ey] = tmp
            empty2 = [xr, yr]
            goal2 = goal[:]
            if goal2 == [xr, yr]:
                goal2 = [ex, ey]
            if (*goal2, *empty2) not in seen:
                i += 1
                heapq.heappush(pq, [h(grid2, goal2, empty2), i, grid2.copy(), goal2, empty2, steps+1])
                seen.add((*goal2, *empty2))



print(task1('input.txt'))

assert task2('test_input.txt') == 7
print(task2('input.txt'))
