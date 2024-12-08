import itertools


def read_input(fn):
    area = dict()
    with open(fn) as fh:
        for row, line in enumerate(fh):
            for col, char in enumerate(line.strip()):
                if char != '.':
                    coords = area.get(char, [])
                    coords.append((row, col))
                    area[char] = coords
    return area, col, row


def task1(fn):
    area, max_col, max_row = read_input(fn)
    antinodes = set()
    for _, coords in area.items():
        for a, b in itertools.permutations(coords, 2):
            c = [
                a[0] + a[0] - b[0],
                a[1] + a[1] - b[1]
            ]
            if 0 <= c[0] <= max_row and 0 <= c[1] <= max_col:
                antinodes.add(tuple(c))
    return len(antinodes)


def task2(fn):
    area, max_col, max_row = read_input(fn)
    antinodes = set()
    for _, coords in area.items():
        for a, b in itertools.permutations(coords, 2):
            antinodes.add(a)
            antinodes.add(b)
            i = 1
            while True:
                c = [
                    a[0] + i*(a[0] - b[0]),
                    a[1] + i*(a[1] - b[1])
                ]
                if 0 <= c[0] <= max_row and 0 <= c[1] <= max_col:
                    antinodes.add(tuple(c))
                    i += 1
                else:
                    break
    return len(antinodes)


assert task1('test_input.txt') == 14
print(task1('input.txt'))

assert task2('test_input.txt') == 34
print(task2('input.txt'))
