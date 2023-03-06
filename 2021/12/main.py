from collections import defaultdict


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    atob = defaultdict(set)
    for line in lines:
        a, b = line.split('-')
        atob[a].add(b)
        atob[b].add(a)

    paths = []
    todo = [('start', {'start'})]
    while todo:
        path, visited_small = todo.pop(0)
        last = path.rsplit(',', maxsplit=1)[-1]
        if last == 'end':
            paths.append(path)
            continue
        for neighbor in atob[last]:
            visited_small2 = visited_small.copy()
            path2 = path[:]
            if neighbor not in visited_small:
                if neighbor.islower():
                    visited_small2.add(neighbor)
                path2 += ',' + neighbor
                todo.append((path2, visited_small2))

    return len(paths)


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    atob = defaultdict(set)
    small_caves = set()
    for line in lines:
        a, b = line.split('-')
        atob[a].add(b)
        atob[b].add(a)
        for x in (a, b):
            if x not in ('start', 'end') and x.islower():
                small_caves.add(x)

    paths = []
    todo = []
    for x in small_caves:
        todo.append(('start', {'start'}, x, 0))
    while todo:
        path, visited_small, special, count = todo.pop(0)
        last = path.rsplit(',', maxsplit=1)[-1]
        if last == 'end':
            paths.append(path)
            continue
        for neighbor in atob[last]:
            visited_small2 = visited_small.copy()
            path2 = path[:]
            count2 = count
            if (
                neighbor != special and neighbor not in visited_small or
                neighbor == special and count < 2
            ):
                if neighbor != special and neighbor.islower():
                    visited_small2.add(neighbor)
                elif neighbor == special:
                    count2 += 1
                path2 += ',' + neighbor
                todo.append((path2, visited_small2, special, count2))

    return len(set(paths))


assert task1('test_input0.txt') == 10
print(task1('input.txt'))

assert task2('test_input0.txt') == 36
print(task2('input.txt'))
