def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    bots = []
    for line in lines:
        pos, r = line.split(', ')

        pos = pos.split('=')[-1][1:-1]
        pos = [int(n) for n in pos.split(',')]

        r = int(r.split('=')[-1])

        bots.append((*pos, r))

    maxbot = max(bots, key=lambda x: x[-1])

    in_range = list(filter(
        lambda x: abs(x[0] - maxbot[0]) + abs(x[1] - maxbot[1]) + abs(x[2] - maxbot[2]) <= maxbot[-1],
        bots
    ))
    return len(in_range)


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    bots = []
    for line in lines:
        pos, r = line.split(', ')

        pos = pos.split('=')[-1][1:-1]
        pos = [int(n) for n in pos.split(',')]

        r = int(r.split('=')[-1])

        bots.append((*pos, r))

    for scale in 100, 10, 1:
        xs, ys, zs, rs = zip(*bots)
        count = dict()
        to_remove = set()
        for x in range((min(xs)-max(rs))//scale, (max(xs)+max(rs))//scale+1):
            for y in range((min(ys)-max(rs))//scale, (max(ys)+max(rs))//scale+1):
                for z in range((min(zs)-max(rs))//scale, (max(zs)+max(rs))//scale+1):
                    for bot in bots:
                        if abs(bot[0]//scale - x) + abs(bot[1]//scale - y) + abs(bot[2]//scale - z) <= bot[-1]//scale:
                            count[x,y,z] = count.get((x, y, z), 0) + 1
                        else:
                            to_remove.add(bot)
        for bot in to_remove:
            print(f'removing {bot}')
            bots.remove(bot)
        return


assert task1('test_input.txt') == 7
print(task1('input.txt'))

assert task2('test_input2.txt') == 36
print(task2('input.txt'))
