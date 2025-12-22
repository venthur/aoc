def get_all_orientations(shape):
    orientations = set()
    current_shape = shape


    def to_hashable(s):
        return tuple(tuple(row) for row in s)


    def rotate_90_clockwise(shape):
        rotated = [[0] * 3 for _ in range(3)]
        for r in range(3):
            for c in range(3):
                # new_row = c, new_col = 3 - 1 - r
                rotated[c][2 - r] = shape[r][c]
        return rotated


    for _ in range(4):
        hashable_shape = to_hashable(current_shape)
        if hashable_shape not in orientations:
            orientations.add(hashable_shape)

        current_shape = rotate_90_clockwise(current_shape)

    flipped_shape = [row[::-1] for row in shape]
    current_shape = flipped_shape

    for _ in range(4):
        hashable_shape = to_hashable(current_shape)
        if hashable_shape not in orientations:
            orientations.add(hashable_shape)

        current_shape = rotate_90_clockwise(current_shape)

    return [list(list(row) for row in o) for o in orientations]


def flatten_shape(shape):
    coordinates = []
    for r in range(3):
        for c in range(3):
            if shape[r][c] == 1:
                coordinates.append((r, c))
    return coordinates


def task1(fn):
    with open(fn) as fh:
        *shapesd, regionsd = fh.read().split('\n\n')

    shapes = []
    for shaped in shapesd:
        shape = []
        shaped = shaped.split(':')[-1].strip()
        for line in shaped.split():
            r = [1 if c == '#' else 0 for c in line.strip()]
            shape.append(r)

        # 1. rotate to all possible positions and merge equal ones
        # 2. flatten representation to positions relative to (0, 0) with 1
        shapes.append(
            [flatten_shape(s) for s in get_all_orientations(shape)]
        )

    tasks = []
    for line in regionsd.strip().split('\n'):
        area, idx = line.split(':')
        y, x = [int(i) for i in area.split('x')]
        idx = [int(i) for i in idx.strip().split()]
        tasks.append((y, x, idx))


    def does_fit(area, todo):

        if not todo:
            return True

        area_list = sorted(list(area))
        for shape in todo:
            for orientation in shape:
                for row, col in area_list:
                    testshape = {(row+y, col+x) for x, y in orientation}
                    if testshape.issubset(area):
                        area2 = area - testshape
                        todo2 = todo[:]
                        todo2.remove(shape)
                        if does_fit(area2, todo2):
                            return True
        return False

    counter = 0
    for y, x, idx in tasks:
        print(idx)

        area = set()
        for row in range(y):
            for col in range(x):
                area.add((row, col))

        todo = []
        for i, cnt in enumerate(idx):
            if cnt == 0:
                continue
            for j in range(cnt):
                todo.append(shapes[i])

        # don't run if the pieces won't fit anyways
        if len(area) < sum(len(shapes[0]) for shapes in todo):
            continue

        if does_fit(area, todo):
            counter += 1
            print(f'fits ({counter})')

    return counter


assert task1('test_input.txt') == 2
# apparently this can be simply solved by checking if the pieces fit roughly
# into the area (but it won't work for the test input
print(task1('input.txt'))
