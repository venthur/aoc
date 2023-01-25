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


def task1(fn):
    cave, units = parse_input(fn)
    pprint(cave, units)


assert task1('test_input.txt') == 27730
print(task1('input.txt'))
