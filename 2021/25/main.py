def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    floor = dict()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            floor[x, y] = char

    xs, ys = zip(*floor)
    maxx = max(xs)
    maxy = max(ys)

    floor_previous = None
    i = 0
    while floor_previous != floor:
        floor_previous = floor.copy()

        floor_bak = floor.copy()
        for (x, y), tile in floor_bak.items():
            if tile != '>':
                continue
            if floor_bak[(x+1) % (maxx+1), y] == '.':
                floor[x, y] = '.'
                floor[(x+1) % (maxx+1), y] = '>'

        floor_bak = floor.copy()
        for (x, y), tile in floor_bak.items():
            if tile != 'v':
                continue
            if floor_bak[x, (y+1) % (maxy+1)] == '.':
                floor[x, y] = '.'
                floor[x, (y+1) % (maxy+1)] = 'v'

        i += 1

    return i


assert task1('test_input.txt') == 58
print(task1('input.txt'))
