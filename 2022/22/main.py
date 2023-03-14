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


assert task1('test_input0.txt') == 6032
print(task1('input.txt'))
