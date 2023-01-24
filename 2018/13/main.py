from itertools import combinations


def parse_file(fn):
    track = dict()
    carts = []

    with open(fn) as fh:
        lines = fh.read().splitlines()

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            match c:
                case '^':
                    carts.append((x, y, 0))
                    track[x, y] = '|'
                case '>':
                    carts.append((x, y, 1))
                    track[x, y] = '-'
                case 'v':
                    carts.append((x, y, 2))
                    track[x, y] = '|'
                case '<':
                    carts.append((x, y, 3))
                    track[x, y] = '-'
                case '|' | '-' | '+' | '\\' | '/':
                    track[x, y] = c

    return track, carts


def pprint(track, carts):
    xs = [x for x, y in track.keys()]
    ys = [y for x, y in track.keys()]

    s = ''
    for y in range(min(ys), max(ys)+1):
        for x in range(min(xs), max(xs)+1):
            if (x, y) in track:
                s += '#'
            else:
                s += ' '
        s += '\n'

    s = [list(l) for l in s.splitlines()]
    for i, (x, y, d, _) in enumerate(carts):
        s[y][x] = str(i)
    s = '\n'.join([''.join(l) for l in s])

    print(s)
    print()


def task1(fn):
    track, carts = parse_file(fn)

    carts = [[x, y, d, 0] for x, y, d in carts]
    while True:
        for i, (x, y, d, counter) in enumerate(carts):
            match d:
                case 0:
                    y -= 1
                    if track[x, y] == '/':
                        d += 1
                    if track[x, y] == '\\':
                        d -= 1
                case 1:
                    x += 1
                    if track[x, y] == '/':
                        d -= 1
                    if track[x, y] == '\\':
                        d += 1
                case 2:
                    y += 1
                    if track[x, y] == '/':
                        d += 1
                    if track[x, y] == '\\':
                        d -= 1
                case 3:
                    x -= 1
                    if track[x, y] == '/':
                        d -= 1
                    if track[x, y] == '\\':
                        d += 1

            if track[x, y] == '+':
                counter += 1
                counter %= 3
                if counter == 1:
                    d -= 1
                elif counter == 0:
                    d += 1

            d %= 4

            carts[i] = [x, y, d, counter]

        for a, b in combinations(carts, 2):
            if a[:2] == b[:2]:
                return tuple(a[:2])


def task2(fn):
    track, carts = parse_file(fn)

    carts = [[x, y, d, 0] for x, y, d in carts]
    while True:
        for i, (x, y, d, counter) in enumerate(carts):
            match d:
                case 0:
                    y -= 1
                    if track[x, y] == '/':
                        d += 1
                    if track[x, y] == '\\':
                        d -= 1
                case 1:
                    x += 1
                    if track[x, y] == '/':
                        d -= 1
                    if track[x, y] == '\\':
                        d += 1
                case 2:
                    y += 1
                    if track[x, y] == '/':
                        d += 1
                    if track[x, y] == '\\':
                        d -= 1
                case 3:
                    x -= 1
                    if track[x, y] == '/':
                        d -= 1
                    if track[x, y] == '\\':
                        d += 1

            if track[x, y] == '+':
                counter += 1
                counter %= 3
                if counter == 1:
                    d -= 1
                elif counter == 0:
                    d += 1

            d %= 4

            carts[i] = [x, y, d, counter]

        to_remove = []
        for a, b in combinations(carts, 2):
            if a[:2] == b[:2]:
                to_remove.append(a)
                to_remove.append(b)

        for a in to_remove:
            carts.remove(a)

        if len(carts) == 1:
            return tuple(carts[0][:2])


assert task1('test_input.txt') == (7, 3)
print(task1('input.txt'))

assert task2('test_input2.txt') == (6, 4)
print(task2('input.txt'))
