from heapq import heappush, heappop
from itertools import combinations


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


def task1(fn, d, thresh):
    area, start, end = read_input(fn)
    dist, prev = dijkstra(area, start)

    pos = end
    path = []
    while pos != start:
        path.append(pos)
        pos = prev[pos]
    path.append(start)

    count = 0
    for (x, y), (x2, y2) in combinations(path, 2):
        if abs(x - x2) + abs(y - y2) <= d and dist[x, y] - dist[x2, y2] > d:
            dd = dist[x, y] - dist[x2, y2] - (abs(x - x2) + abs(y - y2))
            if dd >= thresh:
                count += 1
    return count


assert task1('test_input.txt', 2, 2) == sum([14, 14, 2, 4, 2, 3, 1, 1, 1, 1, 1])
print(task1('input.txt', 2, 100))

assert task1('test_input.txt', 20, 50) == sum([32, 31, 29, 39, 25, 23, 20, 19, 12, 14, 12, 22, 4, 3])
print(task1('input.txt', 20, 100))
