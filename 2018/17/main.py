from collections import defaultdict


def task1(fn):

    with open(fn) as fh:
        lines = fh.read().splitlines()

    clay = defaultdict(lambda: False)
    for line in lines:
        x, y = [n.split('=')[-1] for n in sorted(line.split(', '))]

        xrange = int(x.split('..')[0]), int(x.split('..')[-1]) + 1
        yrange = int(y.split('..')[0]), int(y.split('..')[-1]) + 1
        print(line, xrange, yrange)

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

        # TODO


    return len([pos for pos in flowing | settled if ymin <= pos[1] <= ymax])


assert task1('test_input.txt') == 57
print(task1('input.txt'))
