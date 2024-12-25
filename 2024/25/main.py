def task1(fn):
    with open(fn) as fh:
        data = fh.read().split('\n\n')
    keys = []
    locks = []
    for block in data:
        key = block[0] == '#'
        values = [None for i in range(5)]
        for r, line in enumerate(block.splitlines()):
            for c, char in enumerate(line):
                if char == '#' and key:
                    values[c] = r
                if char == '.' and not key:
                    values[c] = 5-r
        if key:
            keys.append(values)
        else:
            locks.append(values)

    matches = 0
    for k in keys:
        for l in locks:
            v = [a+b for a, b in zip(k, l)]
            if all([v2 <= 5 for v2 in v]):
                matches += 1
    return matches


assert task1('test_input.txt') == 3
print(task1('input.txt'))
