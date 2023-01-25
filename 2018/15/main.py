from itertools import count


def parse_input(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    cave = dict()
    # x, y, HP, AP, G|E
    units = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            match c:
                case '#' | '.':
                    cave[x, y] = c
                case 'G' | 'E':
                    cave[x, y] = '.'
                    unit = [x, y, 200, 3]
                    if c == 'G':
                        unit.append('G')
                    else:
                        unit.append('E')
                    units.append(unit)

    return cave, units


def pprint(cave, units):
    img = []
    for y in range(max(list(zip(*cave.keys()))[1])+1):
        row = []
        for x in range(max(list(zip(*cave.keys()))[0])+1):
            row.append(cave[x, y])
        img.append(row)

    for x, y, _, _, t in units:
        img[y][x] = t

    print('\n'.join([''.join(row) for row in img]))
    print(units)


def task1(fn):
    cave, units = parse_input(fn)
    pprint(cave, units)

    for round_ in count(1):

        # sort units in "reading order"
        units.sort()
        units.sort(key=lambda x: x[1])

        for unit in units:

            # targets
            enemies = [u for u in units if u[-1] != unit[-1]]

            # in range
            in_range = set()
            for x, y, _, _, _ in enemies:
                for xi, yi in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                    if cave[xi, yi] == '.':
                        in_range.add((xi, yi))

            for x, y, _, _, _ in units:
                if [x, y] == unit[:2]:
                    continue
                in_range.discard((x, y))

            if unit[:2] not in in_range:

            # reachable

            # nearest

            # choose

            # distance

            # step

        print(f'Round {round_}:')
        pprint(cave, units)

        if len({race for _, _, _, _, race in units}) == 1:
            break

    return round_ * sum([hp for _, _, hp, _, _ in units])


assert task1('test_input.txt') == 27730
print(task1('input.txt'))
