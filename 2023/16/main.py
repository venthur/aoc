def move(x, y, d):
    if d == 0:
        return x, y-1
    if d == 1:
        return x+1, y
    if d == 2:
        return x, y+1
    if d == 3:
        return x-1, y
    raise ValueError(x, y, d)


def get_energized_tiles(maze, x, y, d):
    beams = [
        (x, y, d),
    ]
    visited = set((x, y, d))
    energized = set()
    while beams:
        x, y, d = beams.pop(0)
        tile = maze.get((x, y))
        if not tile:
            continue
        visited.add((x, y, d))
        energized.add((x, y))

        if (
            (d in (0, 2) and tile == '|') or
            (d in (1, 3) and tile == '-') or
            tile == '.'
        ):
            x, y = move(x, y, d)
            if (x, y, d) not in visited:
                beams.append((x, y, d))
        elif (
            (d in (0, 2) and tile == '-') or
            (d in (1, 3) and tile == '|')
        ):
            for d in (d-1) % 4, (d+1) % 4:
                x2, y2 = move(x, y, d)
                if (x2, y2, d) not in visited:
                    beams.append((x2, y2, d))

        elif (
            d in (1, 3) and tile == '\\' or
            d in (0, 2) and tile == '/'
        ):
            d += 1
            d %= 4
            x, y = move(x, y, d)
            if (x, y, d) not in visited:
                beams.append((x, y, d))

        elif (
            d in (0, 2) and tile == '\\' or
            d in (1, 3) and tile == '/'
        ):
            d -= 1
            d %= 4
            x, y = move(x, y, d)
            if (x, y, d) not in visited:
                beams.append((x, y, d))

        else:
            raise ValueError(d, tile)

    return len(energized)


def task1(fn):
    maze = dict()
    with open(fn) as fh:
        for y, line in enumerate(fh.read().splitlines()):
            for x, char in enumerate(line):
                maze[(x, y)] = char

    return get_energized_tiles(maze, 0, 0, 1)


def task2(fn):
    maze = dict()
    with open(fn) as fh:
        for y, line in enumerate(fh.read().splitlines()):
            for x, char in enumerate(line):
                maze[(x, y)] = char

    e = []
    for row in range(0, y+1):
        e.append(get_energized_tiles(maze, 0, row, 1))
        e.append(get_energized_tiles(maze, x, row, 3))

    for col in range(0, x+1):
        e.append(get_energized_tiles(maze, col, 0, 2))
        e.append(get_energized_tiles(maze, col, y, 0))

    return max(e)


assert task1('test_input.txt') == 46
print(task1('input.txt'))

assert task2('test_input.txt') == 51
print(task2('input.txt'))
