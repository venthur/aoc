def task1(fn):
    with open(fn) as fh:
        lines = fh.readlines()

    maze = dict()
    x, y = 0, 0
    length = 0
    for line in lines:
        d, n, _ = line.split()
        n = int(n)
        length += n
        if d == 'R':
            x += n
        elif d == 'L':
            x -= n
        elif d == 'U':
            y -= n
        elif d == 'D':
            y += n
        else:
            raise ValueError(d)
        maze[(x, y)] = '#'

    # calculate the area using the shoelace formula
    # https://en.wikipedia.org/wiki/Shoelace_formula
    area = 0
    for i in range(len(maze)):
        xi, yi = list(maze.keys())[i]
        xj, yj = list(maze.keys())[(i+1) % len(maze)]
        area += xi*yj - xj*yi
    area = area / 2

    return int(area - length / 2 + 1 + length)


def task2(fn):
    with open(fn) as fh:
        lines = fh.readlines()

    maze = dict()
    x, y = 0, 0
    length = 0
    for line in lines:
        _, _, color = line.split()
        dist, d = color[2:5+2], color[-2]
        n = int(dist, 16)
        d = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}[int(d)]
        length += n
        if d == 'R':
            x += n
        elif d == 'L':
            x -= n
        elif d == 'U':
            y -= n
        elif d == 'D':
            y += n
        else:
            raise ValueError(d)
        maze[(x, y)] = '#'

    # calculate the area using the shoelace formula
    # https://en.wikipedia.org/wiki/Shoelace_formula
    area = 0
    for i in range(len(maze)):
        xi, yi = list(maze.keys())[i]
        xj, yj = list(maze.keys())[(i+1) % len(maze)]
        area += xi*yj - xj*yi
    area = area / 2

    return int(area - length / 2 + 1 + length)


assert task1('test_input.txt') == 62
print(task1('input.txt'))

assert task2('test_input.txt') == 952408144115
print(task2('input.txt'))
