import re


def task1(fn):

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
    print(f'{params=}')

    def gen_spoons(n):
        spoons = [0 for i in range(n)]
        while True:
            spoons[0] += 1
            for i in range(n):
                if spoons[i] >= 100:
                    spoons[i] = 0
                    try:
                        spoons[i+1] += 1
                    except IndexError:
                        return
            if sum(spoons) == 100:
                yield spoons

    max_score = 0
    for spoons in gen_spoons(len(params[0])):
        score = 1
        for p in params[:-1]:
            s = sum(map(lambda a, b: a*b, spoons, p))
            if s < 0:
                s = 0
            score *= s

        if score > max_score:
            max_score = score
        print(f'{spoons=} {score=}')

    return max_score


def task2(fn):

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
    print(f'{params=}')

    def gen_spoons(n):
        spoons = [0 for i in range(n)]
        while True:
            spoons[0] += 1
            for i in range(n):
                if spoons[i] >= 100:
                    spoons[i] = 0
                    try:
                        spoons[i+1] += 1
                    except IndexError:
                        return
            if sum(spoons) == 100:
                yield spoons

    max_score = 0
    for spoons in gen_spoons(len(params[0])):
        score = 1
        # check the 500 calories
        if sum(map(lambda a, b: a*b, spoons, params[-1])) != 500:
            continue
        for p in params[:-1]:
            s = sum(map(lambda a, b: a*b, spoons, p))
            if s < 0:
                s = 0
            score *= s

        if score > max_score:
            max_score = score
        print(f'{spoons=} {score=}')

    return max_score


#assert task1('test_input.txt') == 62842880
#print(task1('input.txt'))


assert task2('test_input.txt') == 57600000
print(task2('input.txt'))
