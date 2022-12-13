def cmp(l1, l2):
    print(f'{l1} {l2}')
    if isinstance(l1, int) and isinstance(l2, int):
        if l1 < l2:
            return -1
        if l1 > l2:
            return 1
        else:
            return 0
    for i in range(max(len(l1), len(l2))):
        try:
            i1 = l1[i]
        except IndexError:
            return -1
        try:
            i2 = l2[i]
        except IndexError:
            return 1
        # check the types
        if isinstance(i1, int) and isinstance(i2, int):
            pass
        elif isinstance(i1, int):
            i1 = [i1]
        elif isinstance(i2, int):
            i2 = [i2]
        res = cmp(i1, i2)
        if res == -1:
            return -1
        if res == 1:
            return 1
    return 0


def task1(input_):
    with open(input_) as fh:
        lines = fh.read().splitlines()

    indices = []
    i = 1
    candidates = []
    for line in lines:
        if not line:
            if cmp(candidates[0], candidates[1]) == -1:
                indices.append(i)
            i += 1
            candidates = []
            continue
        candidates.append(eval(line))
    if cmp(candidates[0], candidates[1]) == -1:
        indices.append(i)

    return sum(indices)


assert task1('test_input.txt') == 13
print(task1('input.txt'))
