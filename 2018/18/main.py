from collections import defaultdict


def read_input(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    area = defaultdict(lambda: None)
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            area[x, y] = char

    return area


def count_neighbours(area, pos):

    result = defaultdict(lambda: 0)
    for x, y in (
        (pos[0]-1, pos[1]-1), (pos[0], pos[1]-1), (pos[0]+1, pos[1]-1),
        (pos[0]-1, pos[1]),                       (pos[0]+1, pos[1]),
        (pos[0]-1, pos[1]+1), (pos[0], pos[1]+1), (pos[0]+1, pos[1]+1),
    ):
        result[area[x, y]] += 1
    return result


def task1(fn, minutes):
    area = read_input(fn)

    seen = set()
    minute = 0
    second = False
    while minute < minutes:
        area_old = area.copy()

        for x, y in [k for k, v in area_old.items() if v is not None]:
            ns = count_neighbours(area_old, (x, y))
            if area_old[x, y] == '.' and ns['|'] >= 3:
                area[x, y] = '|'
            elif area_old[x, y] == '|' and ns['#'] >= 3:
                area[x, y] = '#'
            elif area_old[x, y] == '#':
                if ns['#'] >= 1 and ns['|'] >= 1:
                    area[x, y] = '#'
                else:
                    area[x, y] = '.'

        fp = list(area.items())
        fp.sort(key=lambda x: x[0][1])
        fp.sort(key=lambda x: x[0][0])
        fp = ''.join([v for k, v in fp])

        if fp in seen and not second:
            seen.clear()
            second = True
        elif fp in seen:
            x = (minutes - minute) // len(seen)
            minute += x * len(seen)
        seen.add(fp)
        minute += 1
    return list(area.values()).count('|') * list(area.values()).count('#')


assert task1('test_input.txt', 10) == 1147
print(task1('input.txt', 10))

print(task1('input.txt', 1000000000))

# < 194934
