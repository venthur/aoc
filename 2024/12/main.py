def read_input(fn):
    area = dict()
    with open(fn) as fh:
        for row, line in enumerate(fh):
            for col, char in enumerate(line.strip()):
                area[(row, col)] = char
    return area


def task1(fn):
    area = read_input(fn)

    result = 0
    visited = set()
    for (row, col), char in area.items():
        if (row, col) in visited:
            continue

        region = set()
        queue = [(row, col)]
        while queue:
            row, col = queue.pop(0)
            visited.add((row, col))
            region.add((row, col))
            for (r, c) in (row-1, col), (row+1, col), (row, col-1), (row, col+1):
                if area.get((r, c)) == char and (r, c) not in visited and (r, c) not in queue:
                    queue.append((r, c))

        perimeter = 0
        for (row, col) in region:
            for (r, c) in (row-1, col), (row+1, col), (row, col-1), (row, col+1):
                if (r, c) not in region:
                    perimeter += 1

        result += len(region) * perimeter
    return result


def task2(fn):
    area = read_input(fn)

    result = 0
    visited = set()
    for (row, col), char in area.items():
        if (row, col) in visited:
            continue

        region = set()
        queue = [(row, col)]
        while queue:
            row, col = queue.pop(0)
            visited.add((row, col))
            region.add((row, col))
            for (r, c) in (row-1, col), (row+1, col), (row, col-1), (row, col+1):
                if area.get((r, c)) == char and (r, c) not in visited and (r, c) not in queue:
                    queue.append((r, c))

        # count corners
        left, right, up, down = set(), set(), set(), set()
        for (row, col) in region:
            if (row-1, col) not in region:
                up.add((row, col))
            if (row+1, col) not in region:
                down.add((row, col))
            if (row, col-1) not in region:
                left.add((row, col))
            if (row, col+1) not in region:
                right.add((row, col))

        corners = 0
        for (row, col) in up:
            if (row, col) in left:
                corners += 1
            if (row, col) in right:
                corners += 1
            if (row-1, col-1) in right and (row, col) not in left:
                corners += 1
            if (row-1, col+1) in left and (row, col) not in right:
                corners += 1

        for (row, col) in down:
            if (row, col) in left:
                corners += 1
            if (row, col) in right:
                corners += 1
            if (row+1, col-1) in right and (row, col) not in left:
                corners += 1
            if (row+1, col+1) in left and (row, col) not in right:
                corners += 1

        result += len(region) * corners
    return result


assert task1('test_input.txt') == 1930
print(task1('input.txt'))

assert task2('test_input.txt') == 1206
print(task2('input.txt'))
