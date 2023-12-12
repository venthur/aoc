def is_valid(conditions, groups):
    conditions = [c for c in conditions.split('.') if c]
    if len(conditions) != len(groups):
        return False
    for c, g in zip(conditions, groups):
        if len(c) != g:
            return False
    return True


def get_arrangements(conditions, groups):

    if '?' not in conditions:
        if is_valid(conditions, groups):
            return 1
        else:
            return 0

    # check if conditions and groups are possible
    conditions2 = [c for c in conditions.split('.') if c]
    for c, g in zip(conditions2, groups):
        if '?' in c:
            break
        if len(c) != g:
            return 0

    for c, g in zip(reversed(conditions2), reversed(groups)):
        if '?' in c:
            break
        if len(c) != g:
            return 0

    return (
        get_arrangements(conditions.replace('?', '.', 1), groups) +
        get_arrangements(conditions.replace('?', '#', 1), groups)
    )


def task1(fn):
    arrangements = 0
    with open(fn) as fh:
        for line in fh.read().splitlines():
            conditions, groups = line.split()
            groups = [int(x) for x in groups.split(',')]
            arrangements += get_arrangements(conditions, groups)

    return arrangements


def task2(fn):
    arrangements = 0
    with open(fn) as fh:
        for i, line in enumerate(fh.read().splitlines()):
            print(i)
            conditions, groups = line.split()
            conditions = '?'.join([conditions] * 5)
            groups = ','.join([groups] * 5)
            groups = [int(x) for x in groups.split(',')]
            arrangements += get_arrangements(conditions, groups)

    return arrangements


assert task1('test_input.txt') == 21
print(task1('input.txt'))

#assert task2('test_input.txt') == 525152
#print(task2('input.txt'))
