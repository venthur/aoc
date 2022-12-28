def task1(fn, rows):
    with open(fn) as fh:
        line = fh.read().strip()

    # 0: trap, 1: save
    map_ = dict()
    for i, char in enumerate(line):
        map_[i, 0] = 1 if char == '.' else 0

    for row in range(rows-1):
        for col in range(len(line)):
            a, b, c = map_.get((col-1, row), 1), map_.get((col, row), 1), map_.get((col+1, row), 1)
            if (a, b, c) in ((0, 0, 1), (1, 0, 0), (0, 1, 1), (1, 1, 0)):
                map_[col, row+1] = 0
            else:
                map_[col, row+1] = 1
    return sum(map_.values())


assert task1('test_input.txt', 10) == 38
print(task1('input.txt', 40))

print(task1('input.txt', 400000))
