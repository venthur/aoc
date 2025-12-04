def task1(fn):
    with open(fn) as fh:
        maze = dict()
        for row, line in enumerate(fh):
            for col, c in enumerate(line.strip()):
                maze[(row, col)] = c

    counter = 0
    for (row, col), value in maze.items():
        if value == '.':
            continue
        neighbors = 0
        for r2, c2 in (
            (row-1, col-1),
            (row-1, col),
            (row-1, col+1),
            (row, col-1),
            (row, col+1),
            (row+1, col-1),
            (row+1, col),
            (row+1, col+1),
        ):
            if maze.get((r2, c2), '.') == '@':
                neighbors += 1
                if neighbors >= 4:
                    break
        else:
            counter += 1

    return counter


def task2(fn):
    with open(fn) as fh:
        maze = dict()
        for row, line in enumerate(fh):
            for col, c in enumerate(line.strip()):
                maze[(row, col)] = c

    initial_count = list(maze.values()).count('@')

    while True:
        for (row, col), value in maze.items():
            if value == '.':
                continue
            neighbors = 0
            for r2, c2 in (
                (row-1, col-1),
                (row-1, col),
                (row-1, col+1),
                (row, col-1),
                (row, col+1),
                (row+1, col-1),
                (row+1, col),
                (row+1, col+1),
            ):
                if maze.get((r2, c2), '.') == '@':
                    neighbors += 1
                    if neighbors >= 4:
                        break
            else:
                maze[row, col] = '.'
                break
        else:
            break

    return initial_count - list(maze.values()).count('@')


assert task1('test_input.txt') == 13
print(task1('input.txt'))

assert task2('test_input.txt') == 43
print(task2('input.txt'))
