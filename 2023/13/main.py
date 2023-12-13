def get_reflection_value(maze, rows, cols):
    # check for horizontal reflection
    for row in range(rows-1):
        found_reflection = True
        for i in range(min(row+1, rows-row-1)):
            for col in range(cols):
                if maze[(row-i, col)] != maze[(row+i+1, col)]:
                    found_reflection = False
                    break
            if not found_reflection:
                break
        if found_reflection:
            return 100 * (row + 1)

    # check for vertical reflection
    for col in range(cols-1):
        found_reflection = True
        for i in range(min(col+1, cols-col-1)):
            for row in range(rows):
                if maze[(row, col-i)] != maze[(row, col+i+1)]:
                    found_reflection = False
                    break
            if not found_reflection:
                break
        if found_reflection:
            return col + 1


def task1(fn):
    with open(fn) as fh:
        blocks = fh.read().split('\n\n')

    result = 0
    for block in blocks:
        maze = dict()
        for row, line in enumerate(block.splitlines()):
            for col, char in enumerate(line):
                maze[(row, col)] = char
        rows = row + 1
        cols = col + 1

        result += get_reflection_value(maze, rows, cols)

    return result


def task2(fn):
    with open(fn) as fh:
        blocks = fh.read().split('\n\n')

    result = 0
    for block in blocks:
        print(block)
        maze = dict()
        for row, line in enumerate(block.splitlines()):
            for col, char in enumerate(line):
                maze[(row, col)] = char
        rows = row + 1
        cols = col + 1

        old_value = get_reflection_value(maze, rows, cols)

        for (y, x), v in maze.items():
            maze2 = maze.copy()
            if v == '#':
                maze2[(y, x)] = '.'
            else:
                maze2[(y, x)] = '#'

            value = get_reflection_value(maze2, rows, cols)
            if value and value != old_value:
                result += value
                break
        else:
            raise ValueError('No solution found')

    return result


assert task1('test_input.txt') == 405
print(task1('input.txt'))

assert task2('test_input.txt') == 400
print(task2('input.txt'))
