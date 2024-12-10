def read_input(fn):
    area = dict()
    with open(fn) as fh:
        for row, line in enumerate(fh):
            for col, char in enumerate(line.strip()):
                area[(row, col)] = int(char)
    return area


def get_reachable_ends(pos, area):
    current = area[pos]
    if current == 9:
        return {pos}
    reachable = set()
    for new_pos in (
        (pos[0]-1, pos[1]),
        (pos[0]+1, pos[1]),
        (pos[0], pos[1]-1),
        (pos[0], pos[1]+1),
    ):
        if area.get(new_pos, 0) == current + 1:
            reachable |= get_reachable_ends(new_pos, area)
    return reachable


def task1(fn):
    area = read_input(fn)
    trailheads = [pos for pos, val in area.items() if val == 0]
    score = 0
    for pos in trailheads:
        score += len(get_reachable_ends(pos, area))
    return score


def get_distinct_trails(pos, area):
    current = area[pos]
    if current == 9:
        return 1
    paths = 0
    for new_pos in (
        (pos[0]-1, pos[1]),
        (pos[0]+1, pos[1]),
        (pos[0], pos[1]-1),
        (pos[0], pos[1]+1),
    ):
        if area.get(new_pos, 0) == current + 1:
            paths += get_distinct_trails(new_pos, area)
    return paths


def task2(fn):
    area = read_input(fn)
    trailheads = [pos for pos, val in area.items() if val == 0]
    score = 0
    for pos in trailheads:
        score += get_distinct_trails(pos, area)
    return score


assert task1('test_input.txt') == 36
print(task1('input.txt'))


assert task2('test_input.txt') == 81
print(task2('input.txt'))
