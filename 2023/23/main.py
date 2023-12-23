def task1(fn):
    maze = {}
    with open(fn) as fh:
        for y, line in enumerate(fh.read().splitlines()):
            for x, char in enumerate(line):
                maze[x, y] = char

    start = 1, 0
    end = x-1, y

    paths = []

    queue = [(start, set())]
    while queue:

        pos, visited = queue.pop(0)

        if pos == end:
            paths.append(len(visited))
            continue

        for x, y in (
            (pos[0]-1, pos[1]), (pos[0]+1, pos[1]),
            (pos[0], pos[1]-1), (pos[0], pos[1]+1),
        ):
            tile = maze.get((x, y), '#')
            if tile == '#':
                continue
            elif tile == '.':
                if (x, y) not in visited:
                    v2 = visited.copy()
                    v2.add((x, y))
                    queue.append(((x, y), v2))
            elif tile == '>':
                if (x, y) not in visited and (x+1, y) not in visited:
                    v2 = visited.copy()
                    v2.add((x, y))
                    v2.add((x+1, y))
                    queue.append(((x+1, y), v2))
            elif tile == '<':
                if (x, y) not in visited and (x-1, y) not in visited:
                    v2 = visited.copy()
                    v2.add((x, y))
                    v2.add((x-1, y))
                    queue.append(((x-1, y), v2))
            elif tile == '^':
                if (x, y) not in visited and (x, y-1) not in visited:
                    v2 = visited.copy()
                    v2.add((x, y))
                    v2.add((x, y-1))
                    queue.append(((x, y-1), v2))
            elif tile == 'v':
                if (x, y) not in visited and (x, y+1) not in visited:
                    v2 = visited.copy()
                    v2.add((x, y))
                    v2.add((x, y+1))
                    queue.append(((x, y+1), v2))
            else:
                raise ValueError(tile)

    return max(paths)


def task2(fn):
    maze = {}
    with open(fn) as fh:
        for y, line in enumerate(fh.read().splitlines()):
            for x, char in enumerate(line):
                if char in "<>^v":
                    char = '.'
                maze[x, y] = char

    start = 1, 0
    end = x-1, y

    paths = []
    queue = [(start, set())]
    while queue:
        pos, visited = queue.pop()

        if pos == end:
            paths.append(len(visited))
            print(f'found a path with len {len(visited)}, current best {max(paths)}')
            continue

        for x, y in (
            (pos[0]-1, pos[1]), (pos[0]+1, pos[1]),
            (pos[0], pos[1]-1), (pos[0], pos[1]+1),
        ):
            tile = maze.get((x, y), '#')
            if tile == '#' or (x, y) in visited:
                continue
            else:
                v2 = visited.copy()
                v2.add((x, y))
                queue.append(((x, y), v2))

    return max(paths)


#assert task1('test_input.txt') == 94
#print(task1('input.txt'))

assert task2('test_input.txt') == 154
print(task2('input.txt'))
