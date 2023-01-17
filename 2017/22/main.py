from collections import defaultdict


def task1(fn, nbursts):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    # infected -> True
    grid = defaultdict(lambda: False)
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == '#':
                grid[col, row] = True

    x, y = len(lines) // 2, len(lines) // 2
    direction = 0
    infections = 0
    for burst in range(nbursts):
        if grid[x, y]:
            direction += 1
            direction %= 4
            grid[x, y] = False
        else:
            direction -= 1
            direction %= 4
            grid[x, y] = True
            infections += 1
        if direction == 0:
            y -= 1
        elif direction == 1:
            x += 1
        elif direction == 2:
            y += 1
        elif direction == 3:
            x -= 1

    return infections


def task2(fn, nbursts):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    # infected -> True
    grid = defaultdict(lambda: 'clean')
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == '#':
                grid[col, row] = 'infected'

    x, y = len(lines) // 2, len(lines) // 2
    direction = 0
    infections = 0
    for burst in range(nbursts):
        if grid[x, y] == 'clean':
            direction -= 1
            direction %= 4
            grid[x, y] = 'weak'
        elif grid[x, y] == 'weak':
            infections += 1
            grid[x, y] = 'infected'
        elif grid[x, y] == 'infected':
            direction += 1
            direction %= 4
            grid[x, y] = 'flagged'
        elif grid[x, y] == 'flagged':
            direction += 2
            direction %= 4
            grid[x, y] = 'clean'

        if direction == 0:
            y -= 1
        elif direction == 1:
            x += 1
        elif direction == 2:
            y += 1
        elif direction == 3:
            x -= 1

    return infections


assert task1('test_input.txt', 10000) == 5587
print(task1('input.txt', 10000))

assert task2('test_input.txt', 10000000) == 2511944
print(task2('input.txt', 10000000))
