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

            if unit[2] <= 0:
                continue

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

            # reachable
            # nearest
            # choose
            # distance
            # step

            dist = dict()
            seen = set()
            queue = [[x, y, 0] for x, y in in_range]
            for x, y, _ in queue:
                seen.add((x, y))
            unit_pos = {tuple(u[:2]) for u in units if u != unit}
            while queue:
                x, y, d = queue.pop(0)
                dist[x, y] = d
                for xi, yi in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                    if cave[xi, yi] == '.' and (xi, yi) not in unit_pos and (xi, yi) not in seen:
                        queue.append((xi, yi, d+1))
                        seen.add((xi, yi))

            # move
            if dist[*unit[:2]] > 1:
                possible = []
                x, y = unit[:2]
                for xi, yi in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                    if (xi, yi) in dist:
                        possible.append([xi, yi, dist[xi, yi]])

                possible.sort()
                possible.sort(key=lambda x: x[1])
                possible.sort(key=lambda x: x[2])

                unit[:2] = possible[0][:2]

            # attack
            if dist[*unit[:2]] == 1:
                to_attack = []
                x, y = unit[:2]
                for e in enemies:
                    if e[:2] in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                        to_attack.append(e)

                to_attack.sort()
                to_attack.sort(key=lambda x: x[1])
                to_attack.sort(key=lambda x: x[2])

                e = to_attack.pop(0)
                i = units.index(e)
                units[i][2] -= unit[3]

        units = [u for u in units if u[2] > 0]

        print(f'Round {round_}:')
        pprint(cave, units)

        if len({race for _, _, _, _, race in units}) == 1:
            break

    return round_ * sum([hp for _, _, hp, _, _ in units])


assert task1('test_input.txt') == 27730
print(task1('input.txt'))
