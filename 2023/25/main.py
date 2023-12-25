import random


def task1(fn):
    vertices = set()
    edges = set()
    with open(fn) as fh:
        for line in fh.read().splitlines():
            v, *ws = line.replace(':', ' ').split()
            vertices |= {v, *ws}
            edges |= {(v, w) for w in ws}

    ss = lambda v: next(s for s in subsets if v in s)

    while True:
        subsets = [{v} for v in vertices]

        while len(subsets) > 2:
            s1, s2 = map(ss, random.choice([*edges]))
            if s1 != s2:
                s1 |= s2
                subsets.remove(s2)
        if sum(ss(u) != ss(v) for u, v in edges) < 4:
            break

    return len(subsets[0]) * len(subsets[1])


assert task1('test_input.txt') == 54
print(task1('input.txt'))
