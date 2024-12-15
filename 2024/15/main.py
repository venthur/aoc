from itertools import count


def read_input1(fn):
    with open(fn) as fh:
        area_raw, routes_raw = fh.read().split('\n\n')

    area = dict()
    robot = None, None
    for y, row in enumerate(area_raw.splitlines()):
        for x, char in enumerate(row):
            if char == '@':
                robot = (x, y)
                area[x, y] = '.'
            else:
                area[x, y] = char

    routes = routes_raw.split()
    return area, routes, robot


def pprint(area, robot, route):
    maxx = max([x for x, _ in area.keys()])
    maxy = max([y for _, y in area.keys()])
    for y in range(maxy+1):
        for x in range(maxx+1):
            if (x, y) == robot:
                print('@', end='')
            else:
                print(area[x, y], end='')
        print()
    print(route)


def move1(area, robot, direction):
    x, y = robot
    if direction == '^':
        if area[x, y-1] == '#':
            return area, robot
        elif area[x, y-1] == '.':
            robot = robot[0], robot[1]-1
            return area, robot
        elif area[x, y-1] == 'O':
            for steps in count(1):
                if area[x, y-steps] == '.':
                    area[x, y-steps] = 'O'
                    area[x, y-1] = '.'
                    robot = robot[0], robot[1]-1
                    break
                elif area[x, y-steps] == '#':
                    break
            return area, robot
    elif direction == '>':
        if area[x+1, y] == '#':
            return area, robot
        elif area[x+1, y] == '.':
            robot = robot[0]+1, robot[1]
            return area, robot
        elif area[x+1, y] == 'O':
            for steps in count(1):
                if area[x+steps, y] == '.':
                    area[x+steps, y] = 'O'
                    area[x+1, y] = '.'
                    robot = robot[0]+1, robot[1]
                    break
                elif area[x+steps, y] == '#':
                    break
            return area, robot
    if direction == 'v':
        if area[x, y+1] == '#':
            return area, robot
        elif area[x, y+1] == '.':
            robot = robot[0], robot[1]+1
            return area, robot
        elif area[x, y+1] == 'O':
            for steps in count(1):
                if area[x, y+steps] == '.':
                    area[x, y+steps] = 'O'
                    area[x, y+1] = '.'
                    robot = robot[0], robot[1]+1
                    break
                elif area[x, y+steps] == '#':
                    break
            return area, robot
    elif direction == '<':
        if area[x-1, y] == '#':
            return area, robot
        elif area[x-1, y] == '.':
            robot = robot[0]-1, robot[1]
            return area, robot
        elif area[x-1, y] == 'O':
            for steps in count(1):
                if area[x-steps, y] == '.':
                    area[x-steps, y] = 'O'
                    area[x-1, y] = '.'
                    robot = robot[0]-1, robot[1]
                    break
                elif area[x-steps, y] == '#':
                    break
            return area, robot


def task1(fn):
    area, routes, robot = read_input1(fn)
    route = ''.join(routes)

    for direction in route:
        area, robot = move1(area, robot, direction)

    s = 0
    for (x, y), char in area.items():
        if char == 'O':
            s += 100 * y + x
    return s


def read_input2(fn):
    with open(fn) as fh:
        area_raw, routes_raw = fh.read().split('\n\n')

    area = dict()
    robot = None, None
    for y, row in enumerate(area_raw.splitlines()):
        for x, char in enumerate(row):
            if char == '@':
                robot = (x*2, y)
                area[x*2, y] = '.'
                area[x*2+1, y] = '.'
            elif char == '#':
                area[x*2, y] = '#'
                area[x*2+1, y] = '#'
            elif char == 'O':
                area[x*2, y] = '['
                area[x*2+1, y] = ']'
            elif char == '.':
                area[x*2, y] = '.'
                area[x*2+1, y] = '.'

    routes = routes_raw.split()
    return area, routes, robot


def move2(area, robot, direction):
    # find connected blocks
    blocks = set()
    if direction == '<':
        if area[(robot[0]-1, robot[1])] == '#':
            return area, robot
        for steps in count(1):
            if area[(robot[0]-steps, robot[1])] in '[]':
                blocks.add((robot[0]-steps, robot[1]))
            else:
                break
        for x, y in blocks:
            if area[(x-1, y)] == '#':
                return area, robot
    elif direction == '>':
        if area[(robot[0]+1, robot[1])] == '#':
            return area, robot
        for steps in count(1):
            if area[(robot[0]+steps, robot[1])] in '[]':
                blocks.add((robot[0]+steps, robot[1]))
            else:
                break
        for x, y in blocks:
            if area[(x+1, y)] == '#':
                return area, robot
    elif direction == '^':
        if area[(robot[0], robot[1]-1)] == '#':
            return area, robot
        if area[(robot[0], robot[1]-1)] in '[]':
            queue = []
            blocks.add((robot[0], robot[1]-1))
            queue.append((robot[0], robot[1]-1))
            if area[(robot[0], robot[1]-1)] == '[':
                blocks.add((robot[0]+1, robot[1]-1))
                queue.append((robot[0]+1, robot[1]-1))
            else:
                blocks.add((robot[0]-1, robot[1]-1))
                queue.append((robot[0]-1, robot[1]-1))
            while queue:
                x, y = queue.pop(0)
                if area[(x, y-1)] == '[':
                    blocks.add((x, y-1))
                    queue.append((x, y-1))
                    blocks.add((x+1, y-1))
                    queue.append((x+1, y-1))
                elif area[(x, y-1)] == ']':
                    blocks.add((x, y-1))
                    queue.append((x, y-1))
                    blocks.add((x-1, y-1))
                    queue.append((x-1, y-1))
            for x, y in blocks:
                if area[(x, y-1)] == '#':
                    return area, robot
    elif direction == 'v':
        if area[(robot[0], robot[1]+1)] == '#':
            return area, robot
        if area[(robot[0], robot[1]+1)] in '[]':
            queue = []
            blocks.add((robot[0], robot[1]+1))
            queue.append((robot[0], robot[1]+1))
            if area[(robot[0], robot[1]+1)] == '[':
                blocks.add((robot[0]+1, robot[1]+1))
                queue.append((robot[0]+1, robot[1]+1))
            else:
                blocks.add((robot[0]-1, robot[1]+1))
                queue.append((robot[0]-1, robot[1]+1))
            while queue:
                x, y = queue.pop(0)
                if area[(x, y+1)] == '[':
                    blocks.add((x, y+1))
                    queue.append((x, y+1))
                    blocks.add((x+1, y+1))
                    queue.append((x+1, y+1))
                elif area[(x, y+1)] == ']':
                    blocks.add((x, y+1))
                    queue.append((x, y+1))
                    blocks.add((x-1, y+1))
                    queue.append((x-1, y+1))
            for x, y in blocks:
                if area[(x, y+1)] == '#':
                    return area, robot

    # move the blocks
    blocks = [(x, y, area[(x, y)]) for x, y in blocks]
    for x, y, _ in blocks:
        area[(x, y)] = '.'
    for x, y, char in blocks:
        if direction == '<':
            area[(x-1, y)] = char
        elif direction == '>':
            area[(x+1, y)] = char
        elif direction == '^':
            area[(x, y-1)] = char
        elif direction == 'v':
            area[(x, y+1)] = char

    # move the robot
    if direction == '<':
        robot = robot[0]-1, robot[1]
    elif direction == '>':
        robot = robot[0]+1, robot[1]
    elif direction == '^':
        robot = robot[0], robot[1]-1
    elif direction == 'v':
        robot = robot[0], robot[1]+1

    return area, robot


def task2(fn):
    area, routes, robot = read_input2(fn)
    route = ''.join(routes)

    for direction in route:
        area, robot = move2(area, robot, direction)

    s = 0
    for (x, y), char in area.items():
        if char == '[':
            s += 100 * y + x
    return s


assert task1('test_input.txt') == 10092
print(task1('input.txt'))

assert task2('test_input.txt') == 9021
print(task2('input.txt'))
