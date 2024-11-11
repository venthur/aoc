import re


def gen_spoons(n):
    for i in range(101):
        for j in range(101-i):
            for k in range(101-i-j):
                h = 100-i-j-k
                yield (i, j, k, h)


def task1(fn, check_calories=False):

    with open(fn) as fh:
        lines = fh.read().splitlines()

    params = [[] for i in range(5)]
    for line in lines:
        p = [int(p) for p in re.match(
            r'^.*?(-?\d+).*?(-?\d+),.*?(-?\d+).*?(-?\d+).*?(-?\d+)$',
            line
        ).groups()]
        for i, pi in enumerate(p):
            params[i].append(pi)

    max_score = 0
    for spoons in gen_spoons(len(params[0])):
        score = 1
        if check_calories:
            # check the 500 calories
            if sum(map(lambda a, b: a*b, spoons, params[-1])) != 500:
                continue
        for p in params[:-1]:
            s = sum(map(lambda a, b: a*b, spoons, p))
            if s < 0:
                s = 0
            score *= s

        max_score = max(max_score, score)

    return max_score


assert task1('test_input.txt') == 62842880
print(task1('input.txt'))


assert task1('test_input.txt', check_calories=True) == 57600000
print(task1('input.txt', check_calories=True))
