def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    x, y, d = 0, 0, 90
    for line in lines:
        cmd, n = line[:1], int(line[1:])
        match cmd:
            case 'N':
                y -= n
            case 'E':
                x += n
            case 'S':
                y += n
            case 'W':
                x -= n
            case 'L':
                d -= n
                d %= 360
            case 'R':
                d += n
                d %= 360
            case 'F':
                match d:
                    case 90:
                        x += n
                    case 180:
                        y += n
                    case 270:
                        x -= n
                    case 0:
                        y -= n

    return abs(x) + abs(y)


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    wx, wy = 10, -1
    x, y = 0, 0
    for line in lines:
        cmd, n = line[:1], int(line[1:])
        match cmd:
            case 'N':
                wy -= n
            case 'E':
                wx += n
            case 'S':
                wy += n
            case 'W':
                wx -= n
            case 'L':
                if n == 90:
                    wx, wy = wy, -wx
                elif n == 180:
                    wx, wy = -wx, -wy
                elif n == 270:
                    wx, wy = -wy, wx
            case 'R':
                if n == 90:
                    wx, wy = -wy, wx
                elif n == 180:
                    wx, wy = -wx, -wy
                elif n == 270:
                    wx, wy = wy, -wx
            case 'F':
                x += n*wx
                y += n*wy

    return abs(x) + abs(y)


print(task1('input.txt'))

assert task2('test_input.txt') == 286
print(task2('input.txt'))
