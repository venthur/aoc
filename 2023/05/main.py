from sys import maxsize


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
    ranges = list(zip(seed_line[::2], seed_line[1::2]))

    maps = []
    for block in blocks[1:]:
        block = block.splitlines()[1:]
        map_ = []
        for line in block:
            numbers = [int(i) for i in line.split()]
            map_.append(numbers)
        maps.append(map_)

    # find endpoints
    endpoints = {0, maxsize}
    for map_ in reversed(maps):

        new_endpoints = set()
        for dst_start, src_start, range_len in map_:
            new_endpoints.add(src_start)
            new_endpoints.add(src_start + range_len)
            new_endpoints.add(src_start-1)
            new_endpoints.add(src_start + range_len-1)

        # remap endpoints
        for p in endpoints:
            for dst_start, src_start, range_len in map_:
                if dst_start <= p < dst_start + range_len:
                    p = src_start + (p - dst_start)
                    break
            new_endpoints.add(p)
        endpoints = new_endpoints

    endpoints = sorted(endpoints)

    # remap seeds
    candidate_endpoints = set()
    for start, r in ranges:
        for p in (start, start+r-1):
            points = set(filter(lambda x: start <= x <= start+r-1, endpoints))
            points.add(start)
            points.add(start+r-1)
            candidate_endpoints = candidate_endpoints.union(points)

    min_loc = None
    for seed in candidate_endpoints:
        for map_ in maps:
            for dst_start, src_start, range_len in map_:
                if src_start <= seed < src_start + range_len:
                    seed = dst_start + (seed - src_start)
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
