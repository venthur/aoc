from collections import defaultdict


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    direction = ""
    # axial coordiantes q, s
    pos = [0, 0]
    floor = defaultdict(lambda: 'w')
    for line in lines:
        for char in line:
            direction += char
            if direction not in ('e', 'se', 'sw', 'w', 'nw', 'ne'):
                continue
            match direction:
                case 'e':
                    pos[0] += 1
                case 'w':
                    pos[0] -= 1
                case 'ne':
                    pos[0] += 1
                    pos[1] -= 1
                case 'sw':
                    pos[0] -= 1
                    pos[1] += 1
                case 'se':
                    pos[1] += 1
                case 'nw':
                    pos[1] -= 1

            direction = ''
        floor[*pos] = 'w' if floor[*pos] == 'b' else 'b'
        pos = [0, 0]

    pt1 = list(floor.values()).count('b')

    for i in range(100):
        tiles = set()
        for q, s in floor.keys():
            tiles.add((q, s))
            for dq, ds in (
                (1, 0), (-1, 0), (1, -1), (-1, 1), (0, 1), (0, -1)
            ):
                tiles.add((q+dq, s+ds))

        floor_old = floor.copy()
        for q, s in tiles:
            # find black neighbor tiles
            black = 0
            for dq, ds in (
                    (1, 0), (-1, 0), (1, -1), (-1, 1), (0, 1), (0, -1)
            ):
                if floor_old[q+dq, s+ds] == 'b':
                    black += 1
            if floor_old[q, s] == 'b' and (black == 0 or black > 2):
                floor[q, s] = 'w'
            if floor_old[q, s] == 'w' and black == 2:
                floor[q, s] = 'b'

    pt2 = list(floor.values()).count('b')
    return pt1, pt2


assert task1('test_input0.txt') == (10, 2208)
print(task1('input.txt'))
