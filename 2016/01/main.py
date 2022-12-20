def task1(fn):
    with open(fn) as fh:
        data = [s.strip() for s in fh.read().split(',')]

    direction = "n"
    pos = [0, 0]
    for i in data:
        new_dir = i[0]
        steps = int(i[1:])
        if direction == 'n' and new_dir == 'L':
            direction = 'w'
            pos[1] -= steps
        elif direction == 'n' and new_dir == 'R':
            direction = 'e'
            pos[1] += steps
        elif direction == 'e' and new_dir == 'L':
            direction = 'n'
            pos[0] += steps
        elif direction == 'e' and new_dir == 'R':
            direction = 's'
            pos[0] -= steps
        elif direction == 's' and new_dir == 'L':
            direction = 'e'
            pos[1] += steps
        elif direction == 's' and new_dir == 'R':
            direction = 'w'
            pos[1] -= steps
        elif direction == 'w' and new_dir == 'L':
            direction = 's'
            pos[0] -= steps
        elif direction == 'w' and new_dir == 'R':
            direction = 'n'
            pos[0] += steps
        else:
            raise ValueError

    return abs(pos[0]) + abs(pos[1])


def task2(fn):
    with open(fn) as fh:
        data = [s.strip() for s in fh.read().split(',')]

    visited = set()
    bunny = None
    direction = "n"
    pos = [0, 0]
    visited.add(tuple(pos))
    for i in data:
        new_dir = i[0]
        steps = int(i[1:])
        if direction == 'n' and new_dir == 'L':
            direction = 'w'
        elif direction == 'n' and new_dir == 'R':
            direction = 'e'
        elif direction == 'e' and new_dir == 'L':
            direction = 'n'
        elif direction == 'e' and new_dir == 'R':
            direction = 's'
        elif direction == 's' and new_dir == 'L':
            direction = 'e'
        elif direction == 's' and new_dir == 'R':
            direction = 'w'
        elif direction == 'w' and new_dir == 'L':
            direction = 's'
        elif direction == 'w' and new_dir == 'R':
            direction = 'n'
        for j in range(steps):
            if direction == 'n':
                pos[0] += 1
            elif direction == 's':
                pos[0] -= 1
            elif direction == 'e':
                pos[1] += 1
            elif direction == 'w':
                pos[1] -= 1

            if tuple(pos) in visited:
                return abs(pos[0]) + abs(pos[1])
            else:
                visited.add(tuple(pos))



assert task1('test_input1.txt') == 5
assert task1('test_input2.txt') == 2
assert task1('test_input3.txt') == 12
print(task1('input.txt'))

assert task2('test_input4.txt') == 4
print(task2('input.txt'))
