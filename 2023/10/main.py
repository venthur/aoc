def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    maze = dict()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            maze[(x, y)] = char

    start = None
    for (x, y), val in maze.items():
        if val == 'S':
            start = (x, y)

    x, y = start
    for direction in range(4):
        if direction == 0 and maze.get((x, y-1), '.') in '|7F':
            y -= 1
            break
        elif direction == 1 and maze.get((x+1, y), '.') in '-7J':
            x += 1
            break
        elif direction == 2 and maze.get((x, y+1), '.') in '|LJ':
            y += 1
            break
        elif direction == 3 and maze.get((x-1, y), '.') in '-FL':
            x -= 1
            break
    else:
        raise ValueError

    steps = 1
    while (x, y) != start:
        tile = maze[(x, y)]
        if tile == '-':
            if direction == 1:
                x += 1
            elif direction == 3:
                x -= 1
            else:
                raise ValueError(direction)
        elif tile == '|':
            if direction == 0:
                y -= 1
            elif direction == 2:
                y += 1
            else:
                raise ValueError(direction)
        elif tile == 'L':
            if direction == 2:
                x += 1
                direction = 1
            elif direction == 3:
                y -= 1
                direction = 0
            else:
                raise ValueError(direction)
        elif tile == 'J':
            if direction == 2:
                x -= 1
                direction = 3
            elif direction == 1:
                y -= 1
                direction = 0
            else:
                raise ValueError(direction)
        elif tile == '7':
            if direction == 0:
                x -= 1
                direction = 3
            elif direction == 1:
                y += 1
                direction = 2
            else:
                raise ValueError(direction)
        elif tile == 'F':
            if direction == 0:
                x += 1
                direction = 1
            elif direction == 3:
                y += 1
                direction = 2
            else:
                raise ValueError(direction)
        else:
            raise ValueError(tile)
        steps += 1

    return steps // 2


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    maze = dict()
    maze2 = dict()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            maze[(x, y)] = char
            maze2[(x, y)] = char

    start = None
    for (x, y), val in maze.items():
        if val == 'S':
            start = (x, y)

    x, y = start
    maze2[(x, y)] = '#'
    for direction in range(4):
        if direction == 0 and maze.get((x, y-1), '.') in '|7F':
            maze[(x, y)] = '|'
            y -= 1
            break
        elif direction == 1 and maze.get((x+1, y), '.') in '-7J':
            x += 1
            break
        elif direction == 2 and maze.get((x, y+1), '.') in '|LJ':
            maze[(x, y)] = '|'
            y += 1
            break
        elif direction == 3 and maze.get((x-1, y), '.') in '-FL':
            x -= 1
            break
    else:
        raise ValueError

    while (x, y) != start:
        tile = maze[(x, y)]
        maze2[(x, y)] = '#'
        if tile == '-':
            if direction == 1:
                x += 1
            elif direction == 3:
                x -= 1
            else:
                raise ValueError(direction)
        elif tile == '|':
            if direction == 0:
                y -= 1
            elif direction == 2:
                y += 1
            else:
                raise ValueError(direction)
        elif tile == 'L':
            if direction == 2:
                x += 1
                direction = 1
            elif direction == 3:
                y -= 1
                direction = 0
            else:
                raise ValueError(direction)
        elif tile == 'J':
            if direction == 2:
                x -= 1
                direction = 3
            elif direction == 1:
                y -= 1
                direction = 0
            else:
                raise ValueError(direction)
        elif tile == '7':
            if direction == 0:
                x -= 1
                direction = 3
            elif direction == 1:
                y += 1
                direction = 2
            else:
                raise ValueError(direction)
        elif tile == 'F':
            if direction == 0:
                x += 1
                direction = 1
            elif direction == 3:
                y += 1
                direction = 2
            else:
                raise ValueError(direction)
        else:
            raise ValueError(tile)

    # make all junk parts, ground
    for (x, y), v in maze2.items():
        if v != '#':
            maze[(x, y)] = '.'

    xs, ys = zip(*maze.keys())
    for y in range(max(ys)+1):
        out = True
        for x in range(max(xs)+1):
            if maze[(x, y)] == '.' and out:
                maze[(x, y)] = 'X'
            if maze[(x, y)] in '|JL':
                out = not out

    return list(maze.values()).count('.')


assert task1('test_input.txt') == 8
print(task1('input.txt'))

assert task2('test_input2.txt') == 10
print(task2('input.txt'))
