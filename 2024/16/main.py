from heapq import heappush, heappop


INF = 10**100


def read_input(fn):
    area = dict()
    with open(fn) as fh:
        for row, line in enumerate(fh):
            for col, char in enumerate(line.strip()):
                area[col, row] = char
    return area


def dijkstra(area, start):
    previous = dict()
    distance = dict()
    q = []

    # initialize
    for (x, y), char in area.items():
        if char == '#':
            continue
        for i in range(4):
            distance[x, y, i] = INF
            previous[x, y, i] = None
    distance[start] = 0
    heappush(q, (0, *start))

    while q:
        dist, x, y, d = heappop(q)
        # rotate or move one step
        for dd in ((d-1) % 4, (d+1) % 4):
            if distance[x, y, d] + 1000 < distance[x, y, dd]:
                distance[x, y, dd] = distance[x, y, d] + 1000
                previous[x, y, dd] = (x, y, d)
                heappush(q, (distance[x, y, dd], x, y, dd))
        dx, dy = [(0, -1), (1, 0), (0, 1), (-1, 0)][d]
        nx, ny = x + dx, y + dy
        if area[nx, ny] == '#':
            continue
        if distance[x, y, d] + 1 < distance[nx, ny, d]:
            distance[nx, ny, d] = distance[x, y, d] + 1
            previous[nx, ny, d] = (x, y, d)
            heappush(q, (distance[nx, ny, d], nx, ny, d))

    return distance, previous


def task1(fn):
    area = read_input(fn)

    start = [k for k, v in area.items() if v == 'S'][0]
    end = [k for k, v in area.items() if v == 'E'][0]

    distance, previous = dijkstra(area, (*start, 1))

    return min(distance[*end, i] for i in range(4))


def task2(fn):
    area = read_input(fn)

    start = [k for k, v in area.items() if v == 'S'][0]
    end = [k for k, v in area.items() if v == 'E'][0]

    distance, previous = dijkstra(area, (*start, 1))

    # final direction
    d = sorted([(distance[*end, i], i) for i in range(4)])[0][-1]
    d = (d+2) % 4
    distance2, previous2 = dijkstra(area, (*end, d))

    min_distance = min(distance[*end, i] for i in range(4))

    tiles = set()
    for x, y, d in distance.keys():
        if distance[x, y, d] + distance2[x, y, (d+2) % 4] == min_distance:
            tiles.add((x, y))
    return len(tiles)


assert task1('test_input1.txt') == 7036
assert task1('test_input2.txt') == 11048
print(task1('input.txt'))

assert task2('test_input1.txt') == 45
assert task2('test_input2.txt') == 64
print(task2('input.txt'))
