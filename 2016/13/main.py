def task1(number, target_x, target_y):

    def is_wall(x, y):
        return (x**2 + 3*x + 2*x*y + y + y**2 + number).bit_count() % 2 != 0

    stack = [[1, 1, 0]]
    seen = set((1, 1))
    while True:
        x, y, steps = stack.pop(0)
        if (x, y) == (target_x, target_y):
            return steps
        for (xi, yi) in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if not is_wall(xi, yi) and (xi, yi) not in seen:
                stack.append([xi, yi, steps+1])
                seen.add((xi, yi))


def task2(number):

    def is_wall(x, y):
        return (x**2 + 3*x + 2*x*y + y + y**2 + number).bit_count() % 2 != 0

    stack = [[1, 1, 0]]
    seen = set()
    seen.add((1, 1))
    while True:
        x, y, steps = stack.pop(0)
        if steps >= 50:
            return len(seen)
        for (xi, yi) in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if xi < 0 or yi < 0:
                continue
            if not is_wall(xi, yi) and (xi, yi) not in seen:
                stack.append([xi, yi, steps+1])
                seen.add((xi, yi))


assert task1(10, 7, 4) == 11
print(task1(1350, 31, 39))

print(task2(1350))
