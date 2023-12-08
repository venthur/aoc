from math import lcm


def task1(fn):
    with open(fn) as fh:
        blocks = fh.read().split('\n\n')
        instructions = blocks[0]

        cells = dict()
        for line in blocks[1].splitlines():
            node, neighbors = line.split(' = ')
            neighbors = neighbors[1:-1].split(', ')
            cells[node] = neighbors

    pos = 'AAA'
    steps = 0
    while pos != 'ZZZ':
        direction = instructions[steps % len(instructions)]
        if direction == 'L':
            pos = cells[pos][0]
        elif direction == 'R':
            pos = cells[pos][1]
        steps += 1

    return steps


def task2(fn):
    with open(fn) as fh:
        blocks = fh.read().split('\n\n')
        instructions = blocks[0]

        cells = dict()
        for line in blocks[1].splitlines():
            node, neighbors = line.split(' = ')
            neighbors = neighbors[1:-1].split(', ')
            cells[node] = neighbors

    # find starting positions
    starts = (k for k in cells.keys() if k.endswith('A'))

    all_steps = []
    for pos in starts:
        steps = 0
        while not pos.endswith('Z'):
            direction = instructions[steps % len(instructions)]
            if direction == 'L':
                pos = cells[pos][0]
            elif direction == 'R':
                pos = cells[pos][1]
            steps += 1
        all_steps.append(steps)

    return lcm(*all_steps)


assert task1('test_input.txt') == 6
print(task1('input.txt'))

assert task2('test_input2.txt') == 6
print(task2('input.txt'))
