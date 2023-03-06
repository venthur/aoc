def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    height = dict()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            height[x, y] = int(char)

    sum_ = 0
    for (x, y), v in height.items():
        if all((
            v < height.get((x+1, y), 10), v < height.get((x-1, y), 10),
            v < height.get((x, y+1), 10), v < height.get((x, y-1), 10),
        )):
            sum_ += v+1

    return sum_


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    height = dict()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            height[x, y] = int(char)

    basins = []
    visited = set()
    for (x, y), v in height.items():
        if (x, y) in visited or v == 9:
            continue
        # bfs into a new basin
        todo = [(x, y)]
        visited.add((x, y))
        basin = 0
        while todo:
            x, y = todo.pop()
            basin += 1
            for xi, yi in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                if (xi, yi) not in visited and (xi, yi) in height and height[xi, yi] < 9:
                    todo.append((xi, yi))
                    visited.add((xi, yi))
        basins.append(basin)

    basins.sort()
    return basins[-1] * basins[-2] * basins[-3]


assert task1('test_input0.txt') == 15
print(task1('input.txt'))

assert task2('test_input0.txt') == 1134
print(task2('input.txt'))
