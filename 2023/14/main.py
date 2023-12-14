from copy import deepcopy


def task1(fn):
    with open(fn) as fh:
        platform = []
        for line in fh.read().splitlines():
            platform.append(list(line))

    for row, line in enumerate(platform):
        for col, char in enumerate(line):
            if char == 'O':
                for row2 in range(row-1, -1, -1):
                    if platform[row2][col] != '.':
                        break
                    platform[row2][col] = 'O'
                    platform[row2+1][col] = '.'

    result = 0
    for i, line in enumerate(platform):
        result += (len(platform) - i) * line.count('O')

    return result


def spin(platform):

    platform = deepcopy(platform)

    # north
    for row, line in enumerate(platform):
        for col, char in enumerate(line):
            if char == 'O':
                for row2 in range(row-1, -1, -1):
                    if platform[row2][col] != '.':
                        break
                    platform[row2][col] = 'O'
                    platform[row2+1][col] = '.'

    # west
    for row, line in enumerate(platform):
        for col, char in enumerate(line):
            if char == 'O':
                for col2 in range(col-1, -1, -1):
                    if platform[row][col2] != '.':
                        break
                    platform[row][col2] = 'O'
                    platform[row][col2+1] = '.'

    # south
    for row, line in enumerate(reversed(platform)):
        row = len(platform) - row - 1
        for col, char in enumerate(line):
            if char == 'O':
                for row2 in range(row+1, len(platform)):
                    if platform[row2][col] != '.':
                        break
                    platform[row2][col] = 'O'
                    platform[row2-1][col] = '.'

    # east
    for row, line in enumerate(platform):
        for col, char in enumerate(reversed(line)):
            col = len(line) - col - 1
            if char == 'O':
                for col2 in range(col+1, len(line)):
                    if platform[row][col2] != '.':
                        break
                    platform[row][col2] = 'O'
                    platform[row][col2-1] = '.'

    return platform


def task2(fn):
    with open(fn) as fh:
        platform = []
        for line in fh.read().splitlines():
            platform.append(list(line))

    SPINS = 1000000000
    cache = {}
    cycle = 0
    while cycle < SPINS:
        cycle += 1
        platform = spin(platform)
        platform_str = ''.join([''.join(line) for line in platform])
        if platform_str in cache:
            cycle_len = cycle - cache[platform_str]
            jumps = (SPINS - cycle) // cycle_len
            cycle += jumps * cycle_len
        cache[platform_str] = cycle

    result = 0
    for i, line in enumerate(platform):
        result += (len(platform) - i) * line.count('O')

    return result


assert task1('test_input.txt') == 136
print(task1('input.txt'))

assert task2('test_input.txt') == 64
print(task2('input.txt'))
