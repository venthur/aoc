from collections import defaultdict
from copy import deepcopy


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


def task2(fn, minutes):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    tiles = dict()
    empty_tiles = dict()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            tiles[x, y] = char
            empty_tiles[x, y] = '.'
    tiles.pop((2, 2))
    empty_tiles.pop((2, 2))

    levels = defaultdict(lambda: empty_tiles.copy())
    levels[0] = tiles

    for minute in range(minutes):
        levels_old = deepcopy(levels)
        # levels with bugs
        lwb = [k for k, v in levels.items() if list(v.values()).count('#') > 0]
        for l in range(min(lwb)-1, max(lwb)+2):
            for (x, y), v in levels_old[l].items():
                n_bugs = 0

                # outer ring
                if y == 0 and levels_old[l-1][2, 1] == '#':
                    n_bugs += 1
                if y == 4 and levels_old[l-1][2, 3] == '#':
                    n_bugs += 1
                if x == 0 and levels_old[l-1][1, 2] == '#':
                    n_bugs += 1
                if x == 4 and levels_old[l-1][3, 2] == '#':
                    n_bugs += 1

                # inner ring
                if (x, y) == (2, 1):  # up
                    n_bugs += sum([1 if yi == 0 and val == '#' else 0 for (xi, yi), val in levels_old[l+1].items()])
                if (x, y) == (3, 2):  # right
                    n_bugs += sum([1 if xi == 4 and val == '#' else 0 for (xi, yi), val in levels_old[l+1].items()])
                if (x, y) == (2, 3):  # down
                    n_bugs += sum([1 if yi == 4 and val == '#' else 0 for (xi, yi), val in levels_old[l+1].items()])
                if (x, y) == (1, 2):  # left
                    n_bugs += sum([1 if xi == 0 and val == '#' else 0 for (xi, yi), val in levels_old[l+1].items()])

                # others
                for xi, yi in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                    if levels_old[l].get((xi, yi), '.') == '#':
                        n_bugs += 1

                if levels_old[l][x, y] == '#' and n_bugs != 1:
                    levels[l][x, y] = '.'
                elif levels_old[l][x, y] == '.' and n_bugs in (1, 2):
                    levels[l][x, y] = '#'

    return sum([list(v.values()).count('#') for v in levels.values()])


assert task1('test_input1.txt') == 2129920
print(task1('input.txt'))

assert task2('test_input1.txt', 10) == 99
print(task2('input.txt', 200))
