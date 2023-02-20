def hash(tiles):
    pattern = tiles.items()
    pattern = sorted(pattern, key=lambda x: x[0][0])
    pattern = sorted(pattern, key=lambda x: x[0][1])
    return ''.join(map(lambda x: x[-1], pattern))


def diversity(h):
    s = 0
    for i, c in enumerate(h):
        if c == '#':
            s += 2**i
    return s


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    tiles = dict()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            tiles[x, y] = char

    seen = {hash(tiles)}
    while True:
        tiles_old = tiles.copy()
        for (x, y), v in tiles_old.items():
            n_bugs = 0
            for xi, yi in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                if tiles_old.get((xi, yi), '.') == '#':
                    n_bugs += 1
            if tiles_old[x, y] == '#' and n_bugs != 1:
                tiles[x, y] = '.'
            elif tiles_old[x, y] == '.' and n_bugs in (1, 2):
                tiles[x, y] = '#'

        h = hash(tiles)
        if h in seen:
            break
        seen.add(h)

    return diversity(h)


assert task1('test_input1.txt') == 2129920
print(task1('input.txt'))
