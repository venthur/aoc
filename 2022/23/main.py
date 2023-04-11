from itertools import count


def read_input(fn):
    with open(fn) as fh:
        data = fh.read().splitlines()

    maze = dict()
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == '#':
                maze[x, y] = char

    return maze


def task1(fn, rounds):
    maze = read_input(fn)

    DIRECTIONS = (
        ( 0, -1),  # north
        (+1, -1),
        (+1,  0),  # east
        (+1, +1),
        ( 0, +1),  # south
        (-1, +1),
        (-1,  0),  # west
        (-1, -1),
    )

    next_directions = [0, 4, 6, 2]
    for round in range(rounds):

        to_move = list()
        targets = set()

        for (x, y) in maze:
            # check for no neighbours
            for dx, dy in DIRECTIONS:
                if (x+dx, y+dy) in maze:
                    break
            else:
                # no neighbours found, skip this one
                continue

            # find direction to walk
            for di in next_directions:
                if all(
                    (
                        (x+DIRECTIONS[(di+i) % 8][0], y+DIRECTIONS[(di+i) % 8][1]) not in maze
                        for i in (-1, 0, +1)
                    )
                ):
                    # found a direction to walk!
                    xi = x + DIRECTIONS[di][0]
                    yi = y + DIRECTIONS[di][1]
                    if (xi, yi) not in targets:
                        to_move.append(((x, y), (xi, yi)))
                        targets.add((xi, yi))
                        break
                    else:
                        # collision! remove.
                        to_move = [
                            (pos, pos2)
                            for (pos, pos2) in to_move
                            if pos2 != (xi, yi)
                        ]
                        break

        for pos, pos2 in to_move:
            maze.pop(pos)
            maze[pos2] = '#'

        next_directions.append(next_directions.pop(0))

    xs, ys = zip(*maze.keys())
    area = (max(xs)-min(xs)+1) * (max(ys)-min(ys)+1)

    return area - len(maze)


def task2(fn):
    maze = read_input(fn)

    DIRECTIONS = (
        ( 0, -1),  # north
        (+1, -1),
        (+1,  0),  # east
        (+1, +1),
        ( 0, +1),  # south
        (-1, +1),
        (-1,  0),  # west
        (-1, -1),
    )

    next_directions = [0, 4, 6, 2]
    for round in count(1):

        to_move = list()
        targets = set()

        for (x, y) in maze:
            # check for no neighbours
            for dx, dy in DIRECTIONS:
                if (x+dx, y+dy) in maze:
                    break
            else:
                # no neighbours found, skip this one
                continue

            # find direction to walk
            for di in next_directions:
                if all(
                    (
                        (x+DIRECTIONS[(di+i) % 8][0], y+DIRECTIONS[(di+i) % 8][1]) not in maze
                        for i in (-1, 0, +1)
                    )
                ):
                    # found a direction to walk!
                    xi = x + DIRECTIONS[di][0]
                    yi = y + DIRECTIONS[di][1]
                    if (xi, yi) not in targets:
                        to_move.append(((x, y), (xi, yi)))
                        targets.add((xi, yi))
                        break
                    else:
                        # collision! remove.
                        to_move = [
                            (pos, pos2)
                            for (pos, pos2) in to_move
                            if pos2 != (xi, yi)
                        ]
                        break

        if not targets:
            return round

        for pos, pos2 in to_move:
            maze.pop(pos)
            maze[pos2] = '#'

        next_directions.append(next_directions.pop(0))


assert task1('test_input.txt', 10) == 110
print(task1('input.txt', 10))

assert task2('test_input.txt') == 20
print(task2('input.txt'))
