from itertools import product


def task1(fn):
    with open(fn) as fh:
        data = fh.read().strip()

    data = data.split(': ')[-1]
    data = data.split(', ')
    data = [x.split('=')[-1] for x in data]
    rx, ry = [[int(n) for n in x.split('..')] for x in data]

    x_out = max(rx)
    y_out = min(ry)

    target = set()
    for x, y in product(range(rx[0], rx[1]+1), range(ry[0], ry[1]+1)):
        target.add((x, y))

    def test(x, y):
        pos = [0, 0]
        best_y = None
        while pos[0] < x_out and pos[1] > y_out:
            pos[0] += x
            pos[1] += y
            if x > 0:
                x -= 1
            elif x < 0:
                x += 1
            y -= 1
            if best_y is None or pos[1] > best_y:
                best_y = pos[1]
            if tuple(pos) in target:
                return True, best_y
        return False, best_y

    maxy = 0
    hits = 0
    for x, y in product(range(-500, 500), range(-500, 500)):
        hit, best_y = test(x, y)
        if hit:
            maxy = max(maxy, best_y)
            hits += 1

    return maxy, hits


assert task1('test_input0.txt') == (45, 112)
print(task1('input.txt'))
