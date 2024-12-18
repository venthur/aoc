from heapq import heappush, heappop


INF = 10**10


def read_input(fn):
    data = []
    with open(fn) as fh:
        for line in fh.read().split():
            data.append(tuple(map(int, line.split(','))))
    return data


def dijkstra(area, start):
    dist = {}
    prev = {}
    q = []

    # initialize
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


def task1(fn, space, steps):
    data = read_input(fn)
    data = data[:steps]
    area = {(x, y): '.' for x in range(space+1) for y in range(space+1)}
    for x, y in data:
        area[x, y] = '#'

    dist, prev = dijkstra(area, (0, 0))

    return dist[space, space]


def task2(fn, space, steps):
    data = read_input(fn)
    area = {(x, y): '.' for x in range(space+1) for y in range(space+1)}

    # skip the first steps, known to be reachable
    for i in range(steps):
        x, y = data.pop(0)
        area[x, y] = '#'

    for x, y in data:
        area[x, y] = '#'

        dist, prev = dijkstra(area, (0, 0))

        if dist[space, space] == INF:
            return f'{x},{y}'


assert task1('test_input.txt', 6, 12) == 22
print(task1('input.txt', 70, 1024))

assert task2('test_input.txt', 6, 12) == '6,1'
print(task2('input.txt', 70, 1024))
