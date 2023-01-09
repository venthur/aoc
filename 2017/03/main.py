from collections import defaultdict
from itertools import count


def task1(n):

    direction = 'r'
    used = set()
    x, y = 0, 0
    used.add((x, y))
    for i in range(2, n+1):
        if direction == 'r' and (x, y-1) not in used:
            direction = 'u'
        elif direction == 'u' and (x-1, y) not in used:
            direction = 'l'
        elif direction == 'l' and (x, y+1) not in used:
            direction = 'd'
        elif direction == 'd' and (x+1, y) not in used:
            direction = 'r'

        if direction == 'r':
            x += 1
        elif direction == 'u':
            y -= 1
        elif direction == 'l':
            x -= 1
        elif direction == 'd':
            y += 1

        used.add((x, y))

    return abs(x) + abs(y)


def task2(n):

    direction = 'r'
    used = set()
    x, y = 0, 0
    used.add((x, y))
    values = defaultdict(lambda: 0)
    values[x, y] = 1
    for i in count(2):
        if direction == 'r' and (x, y-1) not in used:
            direction = 'u'
        elif direction == 'u' and (x-1, y) not in used:
            direction = 'l'
        elif direction == 'l' and (x, y+1) not in used:
            direction = 'd'
        elif direction == 'd' and (x+1, y) not in used:
            direction = 'r'

        if direction == 'r':
            x += 1
        elif direction == 'u':
            y -= 1
        elif direction == 'l':
            x -= 1
        elif direction == 'd':
            y += 1

        values[x, y] = (
            values[x+1, y] +
            values[x-1, y] +
            values[x, y+1] +
            values[x, y-1] +
            values[x+1, y+1] +
            values[x+1, y-1] +
            values[x-1, y+1] +
            values[x-1, y-1]
        )
        used.add((x, y))
        if values[x, y] > n:
            return values[x, y]

    return values[x, y]


assert task1(1) == 0
assert task1(12) == 3
assert task1(23) == 2
assert task1(1024) == 31
print(task1(361527))


print(task2(361527))
