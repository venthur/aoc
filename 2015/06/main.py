with open('input.txt') as fh:
    input_ = fh.read().splitlines()


def switch(grid, how, x0, y0, x1, y1):
    for x in range(x0, x1+1):
        for y in range(y0, y1+1):
            if how == 'toggle':
                grid[y][x] = not grid[y][x]
            elif how == 'on':
                grid[y][x] = True
            elif how == 'off':
                grid[y][x] = False
            else:
                raise ValueError(how)
    return grid


def switch2(grid, how, x0, y0, x1, y1):
    for x in range(x0, x1+1):
        for y in range(y0, y1+1):
            if how == 'toggle':
                grid[y][x] += 2
            elif how == 'on':
                grid[y][x] += 1
            elif how == 'off':
                grid[y][x] -= 1
                if grid[y][x] < 0:
                    grid[y][x] = 0
            else:
                raise ValueError(how)
    return grid


def task1(input_):
    grid = [[False for x in range(1000)] for y in range(1000)]

    for line in input_:
        # parse line:
        tokens = line.split()
        if line.startswith('turn'):
            x0, y0 = [int(i) for i in tokens[2].split(',')]
            x1, y1 = [int(i) for i in tokens[4].split(',')]
            grid = switch(grid, tokens[1], x0, y0, x1, y1)
        else:
            x0, y0 = [int(i) for i in tokens[1].split(',')]
            x1, y1 = [int(i) for i in tokens[3].split(',')]
            grid = switch(grid, tokens[0], x0, y0, x1, y1)

    total = 0
    for row in grid:
        total += sum(row)
    return total


def task2(input_):
    grid = [[0 for x in range(1000)] for y in range(1000)]

    for line in input_:
        # parse line:
        tokens = line.split()
        if line.startswith('turn'):
            x0, y0 = [int(i) for i in tokens[2].split(',')]
            x1, y1 = [int(i) for i in tokens[4].split(',')]
            grid = switch2(grid, tokens[1], x0, y0, x1, y1)
        else:
            x0, y0 = [int(i) for i in tokens[1].split(',')]
            x1, y1 = [int(i) for i in tokens[3].split(',')]
            grid = switch2(grid, tokens[0], x0, y0, x1, y1)

    total = 0
    for row in grid:
        total += sum(row)
    return total


print(task1(input_))

print(task2(input_))
