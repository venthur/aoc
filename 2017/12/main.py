def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    data = dict()
    for line in lines:
        parent, childs = line.split(' <-> ')
        parent = int(parent)
        childs = [int(n.strip()) for n in childs.split(',')]
        data[parent] = childs

    contains = set()
    contains.add(0)
    next_ = [0]
    while next_:
        n = next_.pop()
        for child in data[n]:
            if child not in contains:
                next_.append(child)
                contains.add(child)

    return len(contains)


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    data = dict()
    for line in lines:
        parent, childs = line.split(' <-> ')
        parent = int(parent)
        childs = [int(n.strip()) for n in childs.split(',')]
        data[parent] = childs

    groups = 0

    while data:

        contains = set()

        parent, childs = data.popitem()
        for child in childs:
            contains.add(child)
        next_ = list(contains)
        while next_:
            n = next_.pop()
            if n in data.keys():
                for child in data[n]:
                    if child not in contains:
                        next_.append(child)
                        contains.add(child)
                data.pop(n)
        groups += 1

    return groups


print(task1('input.txt'))
print(task2('input.txt'))
