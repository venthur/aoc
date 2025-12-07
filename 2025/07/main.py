from functools import cache


def task1(fn):
    splitter = set()
    maze = dict()
    start = None
    last_row = None
    with open(fn) as fh:
        for row, line in enumerate(fh):
            for col, char in enumerate(line.strip()):
                if char == 'S':
                    start = (col, row)
                    continue
                if char == '.':
                    continue
                if char == '^':
                    splitter.add((col, row))
                    continue
    last_row = row

    hits = set()
    beams = [start]
    while beams:
        col, row = beams.pop(0)
        while row <= last_row:
            if (col, row) in splitter:
                if (col, row) not in hits:
                    beams.append((col-1, row))
                    beams.append((col+1, row))
                hits.add((col, row))
                break
            row += 1

    return len(hits)


def task2(fn):
    splitter = set()
    maze = dict()
    start = None
    last_row = None
    with open(fn) as fh:
        for row, line in enumerate(fh):
            for col, char in enumerate(line.strip()):
                if char == 'S':
                    start = (col, row)
                    continue
                if char == '.':
                    continue
                if char == '^':
                    splitter.add((col, row))
                    continue
    last_row = row

    @cache
    def get_paths(col, row):
        paths = 0
        while row <= last_row:
            if (col, row) in splitter:
                paths += get_paths(col-1, row)
                paths += get_paths(col+1, row)
                break
            row += 1
        else:
            paths += 1
        return paths

    paths = get_paths(*start)

    return paths


assert task1('test_input.txt') == 21
print(task1('input.txt'))

assert task2('test_input.txt') == 40
print(task2('input.txt'))
