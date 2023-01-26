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

    units = units[:]
    units.sort()
    units.sort(key=lambda x: x[1])
    for u in units:
        img[u[1]].append(f' | {u[-1]}: {u[2]}')

    print('\n'.join([''.join(row) for row in img]))


def task1(fn):
    cave, units = parse_input(fn)
    pprint(cave, units)

    for round_ in count(1):

        # sort units in "reading order"
        units.sort()
        units.sort(key=lambda x: x[1])

        full_round = True
        for unit in units:

            if len({race for _, _, hp, _, race in units if hp >= 0}) == 1:
                full_round = False
                break

            if unit[2] <= 0:
                continue

            # targets
            enemies = [u for u in units if u[-1] != unit[-1] and u[2] > 0]

            # in range
            in_range = set()
            for x, y, _, _, _ in enemies:
                for xi, yi in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                    if cave[xi, yi] == '.':
                        in_range.add((xi, yi))

            for x, y, hp, _, _ in units:
                if [x, y] == unit[:2] or hp <= 0:
                    continue
                in_range.discard((x, y))

            dist = dict()
            seen = set()
            queue = [[x, y, 0] for x, y in in_range]
            for x, y, _ in queue:
                seen.add((x, y))
            unit_pos = {tuple(u[:2]) for u in units if u != unit and u[2] > 0}
            while queue:
                x, y, d = queue.pop(0)
                dist[x, y] = d
                for xi, yi in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                    if cave[xi, yi] == '.' and (xi, yi) not in unit_pos and (xi, yi) not in seen:
                        queue.append((xi, yi, d+1))
                        seen.add((xi, yi))

            # move
            if tuple(unit[:2]) in dist and dist[*unit[:2]] > 0:
                # x, y, dist
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
            if tuple(unit[:2]) in dist and dist[*unit[:2]] == 0:
                to_attack = []
                x, y = unit[:2]
                for e in enemies:
                    if e[:2] in ([x+1, y], [x-1, y], [x, y+1], [x, y-1]):
                        to_attack.append(e)

                to_attack.sort()
                to_attack.sort(key=lambda x: x[1])
                to_attack.sort(key=lambda x: x[2])

                e = to_attack[0]
                i = units.index(e)
                units[i][2] -= unit[3]

        # remove dead units
        units = [u for u in units if u[2] > 0]

        print(f'\nRound {round_}:')
        pprint(cave, units)

        if len({race for _, _, _, _, race in units}) == 1:
            if full_round:
                pass
            else:
                round_ -= 1
            break

    return round_ * sum([hp for _, _, hp, _, _ in units])


def task2(fn):
    cave_orig, units_orig = parse_input(fn)

    for ap in count(4):

        cave = cave_orig.copy()
        units = units_orig[:]
        units = [
            [x, y, hp, ap, r] if r == 'E' else [x, y, hp, a, r]
            for [x, y, hp, a, r]
            in units
        ]

        for round_ in count(1):

            # sort units in "reading order"
            units.sort()
            units.sort(key=lambda x: x[1])

            full_round = True
            for unit in units:

                if len({race for _, _, hp, _, race in units if hp >= 0}) == 1:
                    full_round = False
                    break

                if unit[2] <= 0:
                    continue

                # targets
                enemies = [u for u in units if u[-1] != unit[-1] and u[2] > 0]

                # in range
                in_range = set()
                for x, y, _, _, _ in enemies:
                    for xi, yi in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                        if cave[xi, yi] == '.':
                            in_range.add((xi, yi))

                for x, y, hp, _, _ in units:
                    if [x, y] == unit[:2] or hp <= 0:
                        continue
                    in_range.discard((x, y))

                dist = dict()
                seen = set()
                queue = [[x, y, 0] for x, y in in_range]
                for x, y, _ in queue:
                    seen.add((x, y))
                unit_pos = {tuple(u[:2]) for u in units if u != unit and u[2] > 0}
                while queue:
                    x, y, d = queue.pop(0)
                    dist[x, y] = d
                    for xi, yi in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                        if cave[xi, yi] == '.' and (xi, yi) not in unit_pos and (xi, yi) not in seen:
                            queue.append((xi, yi, d+1))
                            seen.add((xi, yi))

                # move
                if tuple(unit[:2]) in dist and dist[*unit[:2]] > 0:
                    # x, y, dist
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
                if tuple(unit[:2]) in dist and dist[*unit[:2]] == 0:
                    to_attack = []
                    x, y = unit[:2]
                    for e in enemies:
                        if e[:2] in ([x+1, y], [x-1, y], [x, y+1], [x, y-1]):
                            to_attack.append(e)

                    to_attack.sort()
                    to_attack.sort(key=lambda x: x[1])
                    to_attack.sort(key=lambda x: x[2])

                    e = to_attack[0]
                    i = units.index(e)
                    units[i][2] -= unit[3]

            # remove dead units
            units = [u for u in units if u[2] > 0]

            print(f'\nRound {round_}:')
            pprint(cave, units)

            if len({race for _, _, _, _, race in units}) == 1:
                if full_round:
                    pass
                else:
                    round_ -= 1
                break

        elves = len(list(filter(lambda x: x[-1] == 'E', units)))
        elves_start = len(list(filter(lambda x: x[-1] == 'E', units_orig)))
        if elves != elves_start:
            continue

        return round_ * sum([hp for _, _, hp, _, _ in units])


assert task1('test_input.txt') == 27730
assert task1('test_input2.txt') == 36334
assert task1('test_input3.txt') == 39514
assert task1('test_input4.txt') == 28944
assert task1('test_input5.txt') == 18740
print(task1('input.txt'))

assert task2('test_input.txt') == 4988
print(task2('input.txt'))
