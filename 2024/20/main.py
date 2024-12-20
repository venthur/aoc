from heapq import heappush, heappop
from copy import deepcopy


INF = 10**10


def read_input(fn):
    area = {}
    start, end = None, None
    with open(fn) as fh:
        for row, line in enumerate(fh):
            for col, char in enumerate(line.strip()):
                if char == 'S':
                    start = (col, row)
                    area[(col, row)] = '.'
                    continue
                elif char == 'E':
                    end = (col, row)
                    area[(col, row)] = '.'
                    continue
                area[(col, row)] = char
    return area, start, end


def dijkstra(area, start):
    dist = {}
    prev = {}
    q = []

    for pos, char in area.items():
        if char == '#':
            continue
        dist[pos] = INF
        prev[pos] = None
    dist[start] = 0
    heappush(q, (0, start))

    while q:
        d, (x, y) = heappop(q)
        for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)):
            nx, ny = x + dx, y + dy
            if area.get((nx, ny), '#') == '#':
                continue
            if d + 1 < dist[nx, ny]:
                dist[nx, ny] = d + 1
                prev[nx, ny] = (x, y)
                heappush(q, (dist[nx, ny], (nx, ny)))

    return dist, prev


def task1(fn):
    area, start, end = read_input(fn)
    dist, prev = dijkstra(area, start)

    pos = end
    path = []
    while pos != start:
        path.append(pos)
        pos = prev[pos]
    path.append(start)

    count = 0
    for x, y in path:
        for x2, y2 in (x-2, y), (x+2, y), (x, y-2), (x, y+2):
            d2 = dist.get((x2, y2), INF)
            if d2 < INF and dist[x, y] - d2 > 2:
                dd = dist[x, y] - d2 - 2
                if dd >= 100:
                    count += 1

    return count


def task2(fn):
    pass


print(task1('test_input.txt'))
print(task1('input.txt'))
