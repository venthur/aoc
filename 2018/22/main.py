from functools import cache


@cache
def el(x, y, depth, xt, yt):
    if (x, y) in ((0, 0), (xt, yt)):
        index = 0
    elif y == 0:
        index = x * 16807
    elif x == 0:
        index = y * 48271
    else:
        index = el(x-1, y, depth, xt, yt) * el(x, y-1, depth, xt, yt)
    return (index + depth) % 20183


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    depth = int(lines[0].split()[-1])
    xt, yt = [int(n) for n in lines[1].split()[-1].split(',')]

    erosion_level = dict()
    for y in range(0, yt+1):
        for x in range(0, xt+1):
            erosion_level[x, y] = el(x, y, depth, xt, yt)

    #s = ''
    #for y in range(0, yt+1):
    #    for x in range(0, xt+1):
    #        match erosion_level[x, y] % 3:
    #            case 0:
    #                s += '.'
    #            case 1:
    #                s += '='
    #            case 2:
    #                s += '|'
    #    s += '\n'
    #print(s)

    return sum(map(lambda x: x % 3, erosion_level.values()))


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    depth = int(lines[0].split()[-1])
    xt, yt = [int(n) for n in lines[1].split()[-1].split(',')]

    import heapq

    pq = heapq([])
    pq.heappush((f, t, x, y, g

assert task1('test_input.txt') == 114
print(task1('input.txt'))

assert task2('test_input.txt') == 45
print(task2('input.txt'))
