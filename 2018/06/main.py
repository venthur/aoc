from collections import Counter


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    data = [list(map(int, line.split(', '))) for line in lines]

    xs = list(zip(*data))[0]
    ys = list(zip(*data))[1]

    grid = dict()
    for x in range(min(xs), max(xs)+1):
        for y in range(min(ys), max(ys)+1):
            mind = min(abs(x-xi) + abs(y-yi) for xi, yi in data)
            for i, (xi, yi) in enumerate(data):
                if abs(x-xi) + abs(y-yi) == mind:
                    if grid.get((x, y), -1) != -1:
                        grid[x, y] = -1
                        break
                    grid[x, y] = i

    # remove the edges
    to_remove = set()
    for x in range(min(xs), max(xs)+1):
        to_remove.add(grid[x, min(ys)])
        to_remove.add(grid[x, max(ys)])

    for y in range(min(ys), max(ys)+1):
        to_remove.add(grid[min(xs), y])
        to_remove.add(grid[max(xs), y])

    grid = dict(filter(lambda x: x[-1] not in to_remove, grid.items()))

    c = Counter(grid.values())
    return c.most_common()[0][-1]


def task2(fn, thresh):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    data = [list(map(int, line.split(', '))) for line in lines]

    xs = list(zip(*data))[0]
    ys = list(zip(*data))[1]

    grid = dict()
    for x in range(min(xs), max(xs)+1):
        for y in range(min(ys), max(ys)+1):
            for i, (xi, yi) in enumerate(data):
                grid[x, y] = grid.get((x, y), 0) + abs(x-xi) + abs(y-yi)

    grid = dict(filter(lambda x: x[-1] < thresh, grid.items()))

    return len(grid)


assert task1('test_input.txt') == 17
print(task1('input.txt'))


assert task2('test_input.txt', 32) == 16
print(task2('input.txt', 10000))
