def parse_input(fn):
    with open(fn) as fh:
        maze_str, directions_str = fh.read().split('\n\n')

    maze = dict()
    for y, line in enumerate(maze_str.splitlines(), start=1):
        for x, char in enumerate(line, start=1):
            if char != ' ':
                maze[x, y] = char

    directions_str = directions_str.strip()
    directions = []
    i = 0
    while i < len(directions_str):
        if directions_str[i] in 'LR':
            directions.append(directions_str[i])
        else:
            steps = int(directions_str[i])
            while (
                i+1 < len(directions_str) and
                directions_str[i+1].isnumeric()
            ):
                i += 1
                steps *= 10
                steps += int(directions_str[i])
            directions.append(steps)

        i += 1

    return maze, directions


def move(maze, x, y, d):
    match d:
        case 0:
            xi, yi = x+1, y
        case 1:
            xi, yi = x, y+1
        case 2:
            xi, yi = x-1, y
        case 3:
            xi, yi = x, y-1

    if (xi, yi) in maze and maze[xi, yi] == '#':
        # wall
        return None
    if (xi, yi) in maze and maze[xi, yi] == '.':
        # good
        return xi, yi
    if (xi, yi) not in maze:
        if d == 0:
            tmp = [(x, char) for (x, y), char in list(maze.items()) if yi == y]
            tmp.sort()
            if tmp[0][1] == '.':
                xi = tmp[0][0]
                return xi, yi
            else:
                return None
        elif d == 1:
            tmp = [(y, char) for (x, y), char in list(maze.items()) if xi == x]
            tmp.sort()
            if tmp[0][1] == '.':
                yi = tmp[0][0]
                return xi, yi
            else:
                return None
        if d == 2:
            tmp = [(x, char) for (x, y), char in list(maze.items()) if yi == y]
            tmp.sort(reverse=True)
            if tmp[0][1] == '.':
                xi = tmp[0][0]
                return xi, yi
            else:
                return None
        elif d == 3:
            tmp = [(y, char) for (x, y), char in list(maze.items()) if xi == x]
            tmp.sort(reverse=True)
            if tmp[0][1] == '.':
                yi = tmp[0][0]
                return xi, yi
            else:
                return None


def task1(fn):
    maze, directions = parse_input(fn)

    positions = list(maze.keys())
    positions.sort(key=lambda x: x[0])
    positions.sort(key=lambda x: x[1])

    x, y = positions[0]
    # 0: right, 1: down, 2: left, 3: up
    d = 0
    for direction in directions:
        if direction == 'L':
            d -= 1
            d %= 4
        elif direction == 'R':
            d += 1
            d %= 4
        else:
            for i in range(direction):
                new_pos = move(maze, x, y, d)
                if new_pos is None:
                    break
                x, y = new_pos

    return 1000 * y + 4 * x + d


def move_cube(maze, x, y, d):

    # length of the side of a face
    L_FACE = 50

    # layout of our specific problem

    #  -------\  /----
    # |  ----[0][1]-  |
    # | |   /[2]/   | |
    # |  -[3][4]----  |
    #  ---[5]/        |
    #      \----------

    # directions
    #     ^
    #     3
    # < 2 + 0 >
    #     1
    #     v

    # face positions defined by top-left coordinates
    FACES = [
        (51, 1), (101, 1),
        (51, 51),
        (1, 101), (51, 101),
        (1, 151),
    ]

    # transitions from (face, dir) -> (face_new, dir_new)
    FACE_TRANS = {
        (0, 3): (5, 0),
        (5, 2): (0, 1),

        (5, 1): (1, 1),
        (1, 3): (5, 3),

        (5, 0): (4, 3),
        (4, 1): (5, 2),

        (4, 0): (1, 2),
        (1, 0): (4, 2),

        (0, 2): (3, 0),
        (3, 2): (0, 0),

        (1, 1): (2, 2),
        (2, 0): (1, 3),

        (3, 3): (2, 0),
        (2, 2): (3, 1),
    }

    # x, y transformation relative to origin of face
    REL_TRANS = {
        # clockwise
        # up -> right
        (3, 0): lambda x, y: (-y-1, x),
        # down -> left
        (1, 2): lambda x, y: (2*L_FACE-y-1, x),

        # counter clockwise
        # right -> up
        (0, 3): lambda x, y: (y, 2*L_FACE-x-1),
        # left -> down
        (2, 1): lambda x, y: (y, -x-1),

        # same direction
        # down -> down
        (1, 1): lambda x, y: (x, y-L_FACE),
        # up -> up
        (3, 3): lambda x, y: (x, y+L_FACE),

        # switch direction
        # right -> left
        (0, 2): lambda x, y: (2*L_FACE-x-1, L_FACE-y-1),
        # left -> right
        (2, 0): lambda x, y: (-x-1, L_FACE-y-1),
    }

    # up -> right
    assert REL_TRANS[3, 0](0, 0) == (-1, 0)
    assert REL_TRANS[3, 0](49, 0) == (-1, 49)
    # down -> left
    assert REL_TRANS[1, 2](0, 49) == (50, 0)
    assert REL_TRANS[1, 2](49, 49) == (50, 49)
    # right -> up
    assert REL_TRANS[0, 3](49, 0) == (0, 50)
    assert REL_TRANS[0, 3](49, 49) == (49, 50)
    # left -> down
    assert REL_TRANS[2, 1](0, 0) == (0, -1)
    assert REL_TRANS[2, 1](0, 49) == (49, -1)
    # down -> down
    assert REL_TRANS[1, 1](0, 49) == (0, -1)
    assert REL_TRANS[1, 1](49, 49) == (49, -1)
    # up -> up
    assert REL_TRANS[3, 3](0, 0) == (0, 50)
    assert REL_TRANS[3, 3](49, 0) == (49, 50)
    # right -> left
    assert REL_TRANS[0, 2](49, 0) == (50, 49)
    assert REL_TRANS[0, 2](49, 49) == (50, 0)
    # left -> right
    assert REL_TRANS[2, 0](0, 0) == (-1, 49)
    assert REL_TRANS[2, 0](0, 49) == (-1, 0)

    match d:
        case 0:
            xi, yi = x+1, y
        case 1:
            xi, yi = x, y+1
        case 2:
            xi, yi = x-1, y
        case 3:
            xi, yi = x, y-1

    if (xi, yi) in maze and maze[xi, yi] == '#':
        # wall
        return None
    if (xi, yi) in maze and maze[xi, yi] == '.':
        # good
        return xi, yi, d

    if (xi, yi) not in maze:
        # which face are we leaving?
        for fid, (xf, yf) in enumerate(FACES):
            if xf <= x < xf+L_FACE and yf <= y < yf+L_FACE:
                # where to: new face new direction, new pos
                fidi, di = FACE_TRANS[fid, d]
                # shift pos relative to face origin
                xi -= FACES[fid][0]
                yi -= FACES[fid][1]
                xi, yi = REL_TRANS[d, di](xi, yi)
                # shift back to global pos
                xi += FACES[fidi][0]
                yi += FACES[fidi][1]
                break
        else:
            raise ValueError(f'Position {x, y} not in known FACES.')

        if (xi, yi) in maze and maze[xi, yi] == '#':
            return None
        elif (xi, yi) in maze and maze[xi, yi] == '.':
            return xi, yi, di

        ValueError(f'{xi, yi, di}')


def task2(fn):
    maze, directions = parse_input(fn)

    positions = list(maze.keys())
    positions.sort(key=lambda x: x[0])
    positions.sort(key=lambda x: x[1])

    x, y = positions[0]
    # 0: right, 1: down, 2: left, 3: up
    d = 0

    for direction in directions:
        if direction == 'L':
            d -= 1
            d %= 4
        elif direction == 'R':
            d += 1
            d %= 4
        else:
            for i in range(direction):
                new_pos = move_cube(maze, x, y, d)
                if new_pos is None:
                    break
                x, y, d = new_pos

    return 1000 * y + 4 * x + d


assert task1('test_input0.txt') == 6032
print(task1('input.txt'))

# assert task2('test_input0.txt') == 5031
print(task2('input.txt'))
