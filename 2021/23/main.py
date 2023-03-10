def parse(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    targets = set()
    maze = dict()
    agents = dict()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char in '#.':
                maze[x, y] = char
            if char in 'ABCD':
                maze[x, y] = '.'
                targets.add((x, y))
                agents.setdefault(char, [])
                agents[char].append((x, y))

    targets2 = list(targets)
    targets2.sort(key=lambda x: x[1])
    targets2.sort(key=lambda x: x[0])

    targets = dict()
    for t in 'ABCD':
        targets[t] = (targets2.pop(0), targets2.pop(0))

    return maze, agents, targets


def pp(maze, agents):
    maze = maze.copy()
    for a, pos in agents.items():
        for (x, y) in pos:
            maze[x, y] = a

    xs, ys = zip(*maze)
    s = ''
    for y in range(min(ys), max(ys)+1):
        for x in range(min(xs), max(xs)+1):
            s += maze.get((x, y), ' ')
        s += '\n'
    print(s)


def task1(fn):
    maze, agents, targets = parse(fn)
    pp(maze, agents)


assert task1('test_input0.txt') == 12521
print(task1('input.txt'))
