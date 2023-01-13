def task1(fn):
    with open(fn) as fh:
        data = fh.read().strip()

    steps = data.split(',')

    # n/s, nw/se, sw/ne
    q, r, s = 0, 0, 0
    for step in steps:
        match step:
            case 'n':
                r -= 1
                s += 1
            case 's':
                r += 1
                s -= 1
            case 'ne':
                q += 1
                r -= 1
            case 'sw':
                q -= 1
                r += 1
            case 'nw':
                q -= 1
                s += 1
            case 'se':
                q += 1
                s -= 1
            case _:
                raise ValueError(step)

    return (abs(q) + abs(r) + abs(s)) // 2


def task2(fn):
    with open(fn) as fh:
        data = fh.read().strip()

    steps = data.split(',')

    # n/s, nw/se, sw/ne
    q, r, s = 0, 0, 0
    max_d = 0
    for step in steps:
        match step:
            case 'n':
                r -= 1
                s += 1
            case 's':
                r += 1
                s -= 1
            case 'ne':
                q += 1
                r -= 1
            case 'sw':
                q -= 1
                r += 1
            case 'nw':
                q -= 1
                s += 1
            case 'se':
                q += 1
                s -= 1
            case _:
                raise ValueError(step)
        d = (abs(q) + abs(r) + abs(s)) // 2
        if d > max_d:
            max_d = d

    return max_d


print(task1('input.txt'))
print(task2('input.txt'))
