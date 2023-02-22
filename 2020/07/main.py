def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    c = dict()
    for line in lines:
        container, containees = line.split(' contain ')
        container, _ = container.rsplit(maxsplit=1)
        containees = containees[:-1]
        if containees == 'no other bags':
            c[container] = tuple()
            continue
        clist = []
        for cnt in containees.split(', '):
            nr, cnt = cnt.split(maxsplit=1)
            bags, _ = cnt.rsplit(maxsplit=1)
            clist.append((int(nr), bags))
        c[container] = tuple(clist)

    todo = ['shiny gold']
    containers = set()
    while todo:
        containee = todo.pop()

        for k, v in c.items():
            for _, bag in v:
                if bag == containee and k not in containers:
                    todo.append(k)
                    containers.add(k)

    return len(containers)


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    c = dict()
    for line in lines:
        container, containees = line.split(' contain ')
        container, _ = container.rsplit(maxsplit=1)
        containees = containees[:-1]
        if containees == 'no other bags':
            c[container] = tuple()
            continue
        clist = []
        for cnt in containees.split(', '):
            nr, cnt = cnt.split(maxsplit=1)
            bags, _ = cnt.rsplit(maxsplit=1)
            clist.append((int(nr), bags))
        c[container] = tuple(clist)

    todo = [(1, 'shiny gold')]
    bags = 0
    while todo:
        nr, bag = todo.pop()

        for n, bi in c[bag]:
            todo.append((n*nr, bi))
            bags += n*nr

    return bags


assert task1('test_input0.txt') == 4
print(task1('input.txt'))

assert task2('test_input0.txt') == 32
print(task2('input.txt'))
