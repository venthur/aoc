from functools import cache


@cache
def get_arrangements(conditions, groups):

    if not groups:
        if '#' not in conditions:
            return 1
        else:
            return 0

    if not conditions:
        return 0

    next_group = groups[0]

    if conditions[0] == '.':
        return get_arrangements(conditions[1:], groups)
    elif conditions[0] == '#':
        this_group = conditions[:next_group]
        this_group = this_group.replace('?', '#')
        if this_group != next_group * '#':
            return 0

        if len(conditions) == next_group:
            if len(groups) == 1:
                return 1
            else:
                return 0

        if conditions[next_group] in '?.':
            return get_arrangements(conditions[next_group+1:], groups[1:])

        return 0
    elif conditions[0] == '?':
        return (
            get_arrangements(conditions.replace('?', '.', 1), groups) +
            get_arrangements(conditions.replace('?', '#', 1), groups)
        )


def task1(fn):
    arrangements = 0
    with open(fn) as fh:
        for line in fh.read().splitlines():
            conditions, groups = line.split()
            groups = tuple([int(x) for x in groups.split(',')])
            arrangements += get_arrangements(conditions, groups)

    return arrangements


def task2(fn):
    arrangements = 0
    with open(fn) as fh:
        for i, line in enumerate(fh.read().splitlines()):
            conditions, groups = line.split()
            conditions = '?'.join([conditions] * 5)
            groups = ','.join([groups] * 5)
            groups = tuple([int(x) for x in groups.split(',')])
            arrangements += get_arrangements(conditions, groups)

    return arrangements


assert task1('test_input.txt') == 21
print(task1('input.txt'))

assert task2('test_input.txt') == 525152
print(task2('input.txt'))
