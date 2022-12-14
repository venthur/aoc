from itertools import permutations, pairwise


def task1(input_):
    with open(input_) as fh:
        lines = fh.read().splitlines()

    happiness = dict()
    people = set()
    for line in lines:
        line = line.split()
        p1 = line[0]
        p2 = line[-1][:-1]
        h = int(line[3]) if line[2] == 'gain' else -int(line[3])
        happiness[p1, p2] = h
        people.add(p1)
        people.add(p2)

    best = 0
    for p in permutations(people):
        h = 0
        for p1, p2 in pairwise(p):
            h += happiness[p1, p2]
            h += happiness[p2, p1]
        h += happiness[p[0], p[-1]]
        h += happiness[p[-1], p[0]]
        if h > best:
            best = h

    return best


def task2(input_):
    with open(input_) as fh:
        lines = fh.read().splitlines()

    happiness = dict()
    people = set()
    for line in lines:
        line = line.split()
        p1 = line[0]
        p2 = line[-1][:-1]
        h = int(line[3]) if line[2] == 'gain' else -int(line[3])
        happiness[p1, p2] = h
        people.add(p1)
        people.add(p2)

    for p in people:
        happiness['basti', p] = 0
        happiness[p, 'basti'] = 0
    people.add('basti')

    best = 0
    for p in permutations(people):
        h = 0
        for p1, p2 in pairwise(p):
            h += happiness[p1, p2]
            h += happiness[p2, p1]
        h += happiness[p[0], p[-1]]
        h += happiness[p[-1], p[0]]
        if h > best:
            best = h

    return best


assert task1('test_input.txt') == 330
print(task1('input.txt'))

print(task2('input.txt'))
