def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    horiz, depth = 0, 0
    for line in lines:
        cmd, v = line.split()
        v = int(v)
        match cmd:
            case 'forward':
                horiz += v
            case 'down':
                depth += v
            case 'up':
                depth -= v

    return horiz * depth


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    horiz, depth, aim = 0, 0, 0
    for line in lines:
        cmd, v = line.split()
        v = int(v)
        match cmd:
            case 'forward':
                horiz += v
                depth += aim * v
            case 'down':
                aim += v
            case 'up':
                aim -= v

    return horiz * depth


print(task1('input.txt'))

print(task2('input.txt'))
