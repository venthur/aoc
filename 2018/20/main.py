from collections import defaultdict


def task1(fn):
    with open(fn) as fh:
        data = fh.read().strip()[1:-1]

    area = defaultdict(lambda: '#')
    x, y = 0, 0
    stack = []
    area[x, y] = '.'
    for char in data:
        match char:
            case 'N':
                area[x, y-1] = '-'
                y -= 2
                area[x, y] = '.'
            case 'W':
                area[x-1, y] = '|'
                x -= 2
                area[x, y] = '.'
            case 'S':
                area[x, y+1] = '-'
                y += 2
                area[x, y] = '.'
            case 'E':
                area[x+1, y] = '|'
                x += 2
                area[x, y] = '.'
            case '|':
                x, y = stack[-1]
            case '(':
                stack.append((x, y))
            case ')':
                x, y = stack.pop()

    stack = [(0, 0, 0)]
    seen = set()
    seen.add((0, 0))
    while stack:
        d, x, y = stack.pop(0)
        for xd, yd, xi, yi in (
            (x, y-1, x, y-2),
            (x, y+1, x, y+2),
            (x-1, y, x-2, y),
            (x+1, y, x+2, y),
        ):
            if area[xd, yd] in '-|' and (xi, yi) not in seen:
                seen.add((xi, yi))
                stack.append((d+1, xi, yi))
                area[xi, yi] = d+1

    return max(filter(lambda x: isinstance(x, int), area.values()))


def task2(fn):
    with open(fn) as fh:
        data = fh.read().strip()[1:-1]

    area = defaultdict(lambda: '#')
    x, y = 0, 0
    stack = []
    area[x, y] = '.'
    for char in data:
        match char:
            case 'N':
                area[x, y-1] = '-'
                y -= 2
                area[x, y] = '.'
            case 'W':
                area[x-1, y] = '|'
                x -= 2
                area[x, y] = '.'
            case 'S':
                area[x, y+1] = '-'
                y += 2
                area[x, y] = '.'
            case 'E':
                area[x+1, y] = '|'
                x += 2
                area[x, y] = '.'
            case '|':
                x, y = stack[-1]
            case '(':
                stack.append((x, y))
            case ')':
                x, y = stack.pop()

    stack = [(0, 0, 0)]
    seen = set()
    seen.add((0, 0))
    while stack:
        d, x, y = stack.pop(0)
        for xd, yd, xi, yi in (
            (x, y-1, x, y-2),
            (x, y+1, x, y+2),
            (x-1, y, x-2, y),
            (x+1, y, x+2, y),
        ):
            if area[xd, yd] in '-|' and (xi, yi) not in seen:
                seen.add((xi, yi))
                stack.append((d+1, xi, yi))
                area[xi, yi] = d+1

    return len(list(filter(lambda x: isinstance(x, int) and x >= 1000, area.values())))


assert task1('test_input0.txt') == 3
assert task1('test_input1.txt') == 23
assert task1('test_input2.txt') == 31
print(task1('input.txt'))

print(task2('input.txt'))
