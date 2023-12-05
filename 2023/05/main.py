from itertools import combinations


def task1(fn):
    with open(fn) as fh:
        blocks = fh.read().split('\n\n')

    seeds = [int(i) for i in blocks[0].split(':')[-1].strip().split()]

    maps = []
    for block in blocks[1:]:
        block = block.splitlines()[1:]
        map_ = []
        for line in block:
            numbers = [int(i) for i in line.split()]
            map_.append(numbers)
        maps.append(map_)

    min_loc = None
    for seed in seeds:
        for map_ in maps:
            for dst_start, src_start, range_len in map_:
                if src_start <= seed < src_start + range_len:
                    gap = seed - src_start
                    seed = dst_start + gap
                    break
        if min_loc is None:
            min_loc = seed
        else:
            min_loc = min(min_loc, seed)

    return min_loc


def task2(fn):
    with open(fn) as fh:
        blocks = fh.read().split('\n\n')

    seed_line = [int(i) for i in blocks[0].split(':')[-1].strip().split()]

    print(f'naive: {sum(seed_line[1::2])}')

    # merge ranges overlapping ranges until no more overlaps
    ranges = list(zip(seed_line[::2], seed_line[1::2]))
    while True:
        for a, b in combinations(ranges, 2):
            print(f'trying {a, b}')
            if b[0] <= a[0] < b[0] + b[1]:
                c = [b[0], max(b[1], a[0] + a[1] - b[0])]
                ranges.remove(a)
                ranges.remove(b)
                ranges.append(c)
                print(c)
                break
            if a[0] <= b[0] < a[0] + a[1]:
                c = [a[0], max(a[1], b[0] + b[1] - a[0])]
                ranges.remove(a)
                ranges.remove(b)
                ranges.append(c)
                print(c)
                break
        else:
            break
    print(f'final ranges: {ranges}')
    print(f'merged: {sum(r[1] for r in ranges)}')
    return

    maps = []
    for block in blocks[1:]:
        block = block.splitlines()[1:]
        map_ = []
        for line in block:
            numbers = [int(i) for i in line.split()]
            map_.append(numbers)
        maps.append(map_)

    min_loc = None
    for a, b in zip(seed_line[::2], seed_line[1::2]):
        for i in range(b):
            seed = a + i
            for map_ in maps:
                for dst_start, src_start, range_len in map_:
                    if src_start <= seed < src_start + range_len:
                        gap = seed - src_start
                        seed = dst_start + gap
                        break
            if min_loc is None:
                min_loc = seed
            else:
                min_loc = min(min_loc, seed)

    return min_loc


assert task1('test_input.txt') == 35
print(task1('input.txt'))

assert task2('test_input.txt') == 46
print(task2('input.txt'))
