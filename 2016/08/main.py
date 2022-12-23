def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    screen = [[0 for i in range(50)] for j in range(6)]
    for line in lines:
        if line.startswith('rect'):
            x, y = [int(i) for i in line.split()[-1].split('x')]
            for xi in range(x):
                for yi in range(y):
                    screen[yi][xi] = 1
        else:
            n, by = int(line.split()[-3][2:]), int(line.split()[-1])
            if 'x=' in line:
                # col
                screen2 = [row[:] for row in screen]
                for i in range(by):
                    screen2 = [screen2[-1]] + screen2[:-1]
                for i in range(len(screen)):
                    screen[i][n] = screen2[i][n]
            else:
                # row
                screen[n] = screen[n][-by:] + screen[n][:-by]

    return sum([sum(row) for row in screen])


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    screen = [[0 for i in range(50)] for j in range(6)]
    for line in lines:
        if line.startswith('rect'):
            x, y = [int(i) for i in line.split()[-1].split('x')]
            for xi in range(x):
                for yi in range(y):
                    screen[yi][xi] = 1
        else:
            n, by = int(line.split()[-3][2:]), int(line.split()[-1])
            if 'x=' in line:
                # col
                screen2 = [row[:] for row in screen]
                for i in range(by):
                    screen2 = [screen2[-1]] + screen2[:-1]
                for i in range(len(screen)):
                    screen[i][n] = screen2[i][n]
            else:
                # row
                screen[n] = screen[n][-by:] + screen[n][:-by]

    s = ''
    for row in screen:
        s += '\n'
        for c in row:
            if c:
                s += '#'
            else:
                s += ' '
    return s


assert task1('test_input.txt') == 6
print(task1('input.txt'))

print(task2('input.txt'))
