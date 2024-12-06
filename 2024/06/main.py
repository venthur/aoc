def read_input(fn):
    map_ = {}
    pos = None
    direction = 0
    with open(fn) as fh:
        for row, line in enumerate(fh):
            for col, char in enumerate(line):
                map_[row, col] = char
                if char == '^':
                    map_[row, col] = '.'
                    pos = (row, col)
    return map_, pos, direction


def task1(fn):
    map_, pos, direction = read_input(fn)
    visited = set()
    while True:
        visited.add(pos)

        if direction == 0:
            next_pos = (pos[0] - 1, pos[1])
        elif direction == 1:
            next_pos = (pos[0], pos[1] + 1)
        elif direction == 2:
            next_pos = (pos[0] + 1, pos[1])
        elif direction == 3:
            next_pos = (pos[0], pos[1] - 1)

        try:
            next_char = map_[next_pos]
        except KeyError:
            break

        if next_char == '#':
            direction = (direction + 1) % 4
        else:
            pos = next_pos

    return len(visited)


def has_loop(map_, pos, direction):
    visited = set()
    while True:
        if (pos, direction) in visited:
            return True
        visited.add((pos, direction))

        if direction == 0:
            next_pos = (pos[0] - 1, pos[1])
        elif direction == 1:
            next_pos = (pos[0], pos[1] + 1)
        elif direction == 2:
            next_pos = (pos[0] + 1, pos[1])
        elif direction == 3:
            next_pos = (pos[0], pos[1] - 1)

        try:
            next_char = map_[next_pos]
        except KeyError:
            return False

        if next_char == '#':
            direction = (direction + 1) % 4
        else:
            pos = next_pos


def walk(map_, pos, direction):
    visited = set()
    while True:
        visited.add(pos)

        if direction == 0:
            next_pos = (pos[0] - 1, pos[1])
        elif direction == 1:
            next_pos = (pos[0], pos[1] + 1)
        elif direction == 2:
            next_pos = (pos[0] + 1, pos[1])
        elif direction == 3:
            next_pos = (pos[0], pos[1] - 1)

        try:
            next_char = map_[next_pos]
        except KeyError:
            return visited

        if next_char == '#':
            direction = (direction + 1) % 4
        else:
            pos = next_pos


def task2(fn):
    map_, pos, direction = read_input(fn)

    path = walk(map_, pos, direction)

    loops = 0
    for y, x in path:
        map2 = map_.copy()
        map2[y, x] = '#'
        if has_loop(map2, pos, direction):
            loops += 1

    return loops


assert task1('test_input.txt') == 41
print(task1('input.txt'))

assert task2('test_input.txt') == 6
print(task2('input.txt'))
