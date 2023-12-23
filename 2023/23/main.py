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

    START = 1, 0
    END = x-1, y

    graph = dict()
    for pos, char in maze.items():
        if char == '#':
            continue
        graph[pos] = dict()
        for x, y in (
            (pos[0]-1, pos[1]), (pos[0]+1, pos[1]),
            (pos[0], pos[1]-1), (pos[0], pos[1]+1),
        ):
            tile = maze.get((x, y), '#')
            if tile == '#':
                continue
            graph[pos][(x, y)] = 1

    # removing nodes with exactly two neighbors
    while any(len(n) == 2 for n in graph.values()):
        for pos, neighbors in graph.items():
            if len(neighbors) != 2:
                continue
            (x1, y1), cost1 = list(neighbors.items())[0]
            (x2, y2), cost2 = list(neighbors.items())[1]
            graph[(x1, y1)][(x2, y2)] = cost1 + cost2
            graph[(x1, y1)].pop(pos)
            graph[(x2, y2)][(x1, y1)] = cost1 + cost2
            graph[(x2, y2)].pop(pos)
            graph.pop(pos)
            break

    paths = []
    queue = [(START, set(), 0)]
    while queue:
        pos, visited, steps = queue.pop()

        if pos == END:
            paths.append(steps)
            continue

        for (x, y), cost in graph[pos].items():
            if (x, y) in visited:
                continue
            else:
                v2 = visited.copy()
                v2.add((x, y))
                queue.append(((x, y), v2, steps+cost))

    return max(paths)


assert task1('test_input.txt') == 94
print(task1('input.txt'))

assert task2('test_input.txt') == 154
print(task2('input.txt'))
