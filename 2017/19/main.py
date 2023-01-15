def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    map = dict()
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if row == 0 and char == '|':
                pos = col, row
                direction = 'd'
            if char.isalpha() or char in ('-', '|', '+'):
                map[col, row] = char

    collected = []
    col, row = pos
    while True:
        match direction:

            case 'd':
                row += 1
                if map.get((col, row)) is None:
                    break
                if map[col, row] == '+':
                    if map.get((col-1, row)) is not None:
                        direction = 'l'
                    elif map.get((col+1, row)) is not None:
                        direction = 'r'
                elif map[col, row].isalpha():
                    collected.append(map[col, row])

            case 'u':
                row -= 1
                if map.get((col, row)) is None:
                    break
                if map[col, row] == '+':
                    if map.get((col-1, row)) is not None:
                        direction = 'l'
                    elif map.get((col+1, row)) is not None:
                        direction = 'r'
                elif map[col, row].isalpha():
                    collected.append(map[col, row])

            case 'l':
                col -= 1
                if map.get((col, row)) is None:
                    break
                if map[col, row] == '+':
                    if map.get((col, row-1)) is not None:
                        direction = 'u'
                    elif map.get((col, row+1)) is not None:
                        direction = 'd'
                elif map[col, row].isalpha():
                    collected.append(map[col, row])

            case 'r':
                col += 1
                if map.get((col, row)) is None:
                    break
                if map[col, row] == '+':
                    if map.get((col, row-1)) is not None:
                        direction = 'u'
                    elif map.get((col, row+1)) is not None:
                        direction = 'd'
                elif map[col, row].isalpha():
                    collected.append(map[col, row])

    return ''.join(collected)


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    map = dict()
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if row == 0 and char == '|':
                pos = col, row
                direction = 'd'
            if char.isalpha() or char in ('-', '|', '+'):
                map[col, row] = char

    steps = 0
    col, row = pos
    while True:
        steps += 1
        match direction:

            case 'd':
                row += 1
                if map.get((col, row)) is None:
                    break
                if map[col, row] == '+':
                    if map.get((col-1, row)) is not None:
                        direction = 'l'
                    elif map.get((col+1, row)) is not None:
                        direction = 'r'

            case 'u':
                row -= 1
                if map.get((col, row)) is None:
                    break
                if map[col, row] == '+':
                    if map.get((col-1, row)) is not None:
                        direction = 'l'
                    elif map.get((col+1, row)) is not None:
                        direction = 'r'

            case 'l':
                col -= 1
                if map.get((col, row)) is None:
                    break
                if map[col, row] == '+':
                    if map.get((col, row-1)) is not None:
                        direction = 'u'
                    elif map.get((col, row+1)) is not None:
                        direction = 'd'

            case 'r':
                col += 1
                if map.get((col, row)) is None:
                    break
                if map[col, row] == '+':
                    if map.get((col, row-1)) is not None:
                        direction = 'u'
                    elif map.get((col, row+1)) is not None:
                        direction = 'd'

    return steps


assert task1('test_input.txt') == 'ABCDEF'
print(task1('input.txt'))

assert task2('test_input.txt') == 38
print(task2('input.txt'))
