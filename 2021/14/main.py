from itertools import pairwise
from collections import defaultdict


def count(pairs):
    counter = defaultdict(int)
    for (_, b), v in pairs.items():
        counter[b] += v

    return counter


def task1(fn, steps):
    with open(fn) as fh:
        template, pairs = fh.read().split('\n\n')

    rules = dict()
    for pair in pairs.splitlines():
        p, s = pair.split(' -> ')
        rules[p] = s

    pairs = defaultdict(int)
    for a, b in pairwise(template):
        pairs[a+b] += 1

    def count(pairs):
        counter = defaultdict(int)
        counter[template[0]] += 1
        for (_, b), v in pairs.items():
            counter[b] += v

        return counter

    for i in range(steps):
        pairs_bak = pairs.copy()
        for a, b in pairs_bak:
            insert = rules[a+b]
            n = pairs_bak[a+b]
            pairs[a+b] -= n

            pairs[a+insert] += n
            pairs[insert+b] += n

    res = count(pairs).values()
    return max(res) - min(res)


assert task1('test_input0.txt', 10) == 1588
print(task1('input.txt', 10))

print(task1('input.txt', 40))
