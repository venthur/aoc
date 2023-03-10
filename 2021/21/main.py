from itertools import product
from functools import cache


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    pos = [int(n) for n in [line.split()[-1] for line in lines]]

    scores = [0, 0]
    rolls = 0
    dice = 0
    while True:
        dice = dice % 100 + 1
        if not rolls % 2:
            pos[0] += sum([dice, dice+1, dice+2])
            scores[0] += pos[0] % 10 if pos[0] % 10 else 10
        else:
            pos[1] += sum([dice, dice+1, dice+2])
            scores[1] += pos[1] % 10 if pos[1] % 10 else 10
        dice += 2
        rolls += 3
        if any(filter(lambda x: x >= 1000, scores)):
            break

    return min(scores) * rolls


@cache
def play(p1, s1, p2, s2):
    w1, w2 = 0, 0
    for m1, m2, m3 in product((1, 2, 3), (1, 2, 3), (1, 2, 3)):
        p1_new = (p1 + m1 + m2 + m3) % 10 if (p1 + m1 + m2 + m3) % 10 else 10
        s1_new = s1 + p1_new
        if s1_new >= 21:
            w1 += 1
        else:
            w2_new, w1_new = play(p2, s2, p1_new, s1_new)
            w1 += w1_new
            w2 += w2_new

    return w1, w2


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    p1, p2 = [int(n) for n in [line.split()[-1] for line in lines]]

    return max(play(p1, 0, p2, 0))


assert task1('test_input0.txt') == 739785
print(task1('input.txt'))

assert task2('test_input0.txt') == 444356092776315
print(task2('input.txt'))
