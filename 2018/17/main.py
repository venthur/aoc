from collections import defaultdict


def pprint(clay, settled, flowing):
    ymin = min(clay, key=lambda p: p[1])[1]
    ymax = max(clay, key=lambda p: p[1])[1]
    xmin = min(clay, key=lambda p: p[0])[0]
    xmax = max(clay, key=lambda p: p[0])[0]

    s = ''
    for y in range(ymin, ymax+1):
        for x in range(xmin, xmax+1):
            if clay[x, y]:
                s += '#'
            elif (x, y) in settled:
                s += '~'
            elif (x, y) in flowing:
                s += '|'
            else:
                s += ' '
        s += '\n'
    print()
    print(s)


def task1(fn):

    with open(fn) as fh:
        lines = fh.read().splitlines()

    clay = defaultdict(lambda: False)
    for line in lines:
        x, y = [n.split('=')[-1] for n in sorted(line.split(', '))]

        xrange = int(x.split('..')[0]), int(x.split('..')[-1]) + 1
        yrange = int(y.split('..')[0]), int(y.split('..')[-1]) + 1

        for x in range(xrange[0], xrange[1]):
            for y in range(yrange[0], yrange[1]):
                clay[x, y] = True

    ymin = min(clay, key=lambda p: p[1])[1]
    ymax = max(clay, key=lambda p: p[1])[1]

    settled = set()
    flowing = set()
    queue = [(500, 0)]
    while queue:
        pos = queue.pop(0)
        flowing.add(pos)

        below = (pos[0], pos[1]+1)
        if not clay[below] and below not in flowing and 1 <= below[1] <= ymax:
            queue.append(below)
            continue

        if not clay[below] and below not in settled:
            continue

        left = (pos[0]-1, pos[1])
        right = (pos[0]+1, pos[1])

        left_border = False
        right_border = False

        fill = set()
        fill.add(pos)
        while True:
            if clay[left]:
                left_border = True
                break
            left_below = (left[0], left[1]+1)
            if clay[left_below] or left_below in settled:
                fill.add(left)
            else:
                queue.append(left)
                break
            left = (left[0]-1, left[1])

        while True:
            if clay[right]:
                right_border = True
                break
            right_below = (right[0], right[1]+1)
            if clay[right_below] or right_below in settled:
                fill.add(right)
            else:
                queue.append(right)
                break
            right = (right[0]+1, right[1])

        if left_border and right_border:
            for x, y in fill:
                settled.add((x, y))
            queue.append((pos[0], pos[1]-1))
        else:
            for x, y in fill:
                flowing.add((x, y))

    return len([pos for pos in flowing | settled if ymin <= pos[1] <= ymax])


def task2(fn):

    with open(fn) as fh:
        lines = fh.read().splitlines()

    clay = defaultdict(lambda: False)
    for line in lines:
        x, y = [n.split('=')[-1] for n in sorted(line.split(', '))]

        xrange = int(x.split('..')[0]), int(x.split('..')[-1]) + 1
        yrange = int(y.split('..')[0]), int(y.split('..')[-1]) + 1

        for x in range(xrange[0], xrange[1]):
            for y in range(yrange[0], yrange[1]):
                clay[x, y] = True

    ymin = min(clay, key=lambda p: p[1])[1]
    ymax = max(clay, key=lambda p: p[1])[1]

    settled = set()
    flowing = set()
    queue = [(500, 0)]
    while queue:
        pos = queue.pop(0)
        flowing.add(pos)

        below = (pos[0], pos[1]+1)
        if not clay[below] and below not in flowing and 1 <= below[1] <= ymax:
            queue.append(below)
            continue

        if not clay[below] and below not in settled:
            continue

        left = (pos[0]-1, pos[1])
        right = (pos[0]+1, pos[1])

        left_border = False
        right_border = False

        fill = set()
        fill.add(pos)
        while True:
            if clay[left]:
                left_border = True
                break
            left_below = (left[0], left[1]+1)
            if clay[left_below] or left_below in settled:
                fill.add(left)
            else:
                queue.append(left)
                break
            left = (left[0]-1, left[1])

        while True:
            if clay[right]:
                right_border = True
                break
            right_below = (right[0], right[1]+1)
            if clay[right_below] or right_below in settled:
                fill.add(right)
            else:
                queue.append(right)
                break
            right = (right[0]+1, right[1])

        if left_border and right_border:
            for x, y in fill:
                settled.add((x, y))
            queue.append((pos[0], pos[1]-1))
        else:
            for x, y in fill:
                flowing.add((x, y))

    return len(settled)


assert task1('test_input.txt') == 57
print(task1('input.txt'))


assert task2('test_input.txt') == 29
print(task2('input.txt'))
