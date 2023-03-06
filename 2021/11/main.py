from itertools import count


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    grid = dict()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            grid[x, y] = int(char)

    flashes = 0
    for round_ in range(100):
        flashed = set()
        todo = []
        for pos, v in grid.items():
            grid[pos] += 1
            if grid[pos] > 9:
                todo.append(pos)
                flashed.add(pos)

        while todo:
            x, y = todo.pop()
            flashes += 1
            for dx, dy in (
                (-1, -1), (0, -1), (1, -1),
                (-1, 0), (1, 0),
                (-1, 1), (0, 1), (1, 1),
            ):
                xi = x + dx
                yi = y + dy
                if xi < 0 or xi > 9 or yi < 0 or yi > 9:
                    continue
                grid[xi, yi] += 1
                if grid[xi, yi] > 9 and (xi, yi) not in flashed:
                    todo.append((xi, yi))
                    flashed.add((xi, yi))
        for x, y in flashed:
            grid[x, y] = 0

    return flashes


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    grid = dict()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            grid[x, y] = int(char)

    flashes = 0
    for round_ in count(1):
        flashed = set()
        todo = []
        for pos, v in grid.items():
            grid[pos] += 1
            if grid[pos] > 9:
                todo.append(pos)
                flashed.add(pos)

        while todo:
            x, y = todo.pop()
            flashes += 1
            for dx, dy in (
                (-1, -1), (0, -1), (1, -1),
                (-1, 0), (1, 0),
                (-1, 1), (0, 1), (1, 1),
            ):
                xi = x + dx
                yi = y + dy
                if xi < 0 or xi > 9 or yi < 0 or yi > 9:
                    continue
                grid[xi, yi] += 1
                if grid[xi, yi] > 9 and (xi, yi) not in flashed:
                    todo.append((xi, yi))
                    flashed.add((xi, yi))
        for x, y in flashed:
            grid[x, y] = 0

        if sum(grid.values()) == 0:
            return round_


assert task1('test_input0.txt') == 1656
print(task1('input.txt'))

assert task2('test_input0.txt') == 195
print(task2('input.txt'))
