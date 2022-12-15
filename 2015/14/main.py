import re


def simulate(speed, duration, rest, seconds):
    d = 0
    state = 'flying'
    s_state = 0
    for s in range(seconds):
        if state == 'flying':
            d += speed
        s_state += 1
        if state == 'flying' and s_state >= duration:
            state = 'resting'
            s_state = 0
        elif state == 'resting' and s_state >= rest:
            state = 'flying'
            s_state = 0
    return d


def task1(fn, seconds):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    deer = dict()
    for line in lines:
        name, speed, duration, rest = re.match(
            r'^(\w*) .*? (\d*) .*? (\d*) .*? (\d*) .*?$',
            line
        ).groups()
        speed = int(speed)
        duration = int(duration)
        rest = int(rest)
        deer[name] = [speed, duration, rest]

    max_d = 0
    for name, (speed, duration, rest) in deer.items():
        d = simulate(speed, duration, rest, seconds)
        if d > max_d:
            max_d = d

    return max_d


def simulate2(speed, duration, rest, seconds):
    d = 0
    t = []
    state = 'flying'
    s_state = 0
    for s in range(seconds):
        if state == 'flying':
            d += speed
        s_state += 1
        if state == 'flying' and s_state >= duration:
            state = 'resting'
            s_state = 0
        elif state == 'resting' and s_state >= rest:
            state = 'flying'
            s_state = 0
        t.append(d)
    return t


def task2(fn, seconds):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    deer = dict()
    for line in lines:
        name, speed, duration, rest = re.match(
            r'^(\w*) .*? (\d*) .*? (\d*) .*? (\d*) .*?$',
            line
        ).groups()
        speed = int(speed)
        duration = int(duration)
        rest = int(rest)
        deer[name] = [speed, duration, rest]

    ts = []
    for name, (speed, duration, rest) in deer.items():
        t = simulate2(speed, duration, rest, seconds)
        ts.append(t)

    points = [0 for i in range(len(deer))]
    for s in range(seconds):
        dists = []
        for i in range(len(deer)):
            dists.append(ts[i][s])
        d = max(dists)
        for i in range(len(deer)):
            if ts[i][s] == d:
                points[i] += 1

    return max(points)


assert task1('test_input.txt', 1) == 16
assert task1('test_input.txt', 10) == 160
assert task1('test_input.txt', 11) == 176
assert task1('test_input.txt', 12) == 176
assert task1('test_input.txt', 1000) == 1120
print(task1('input.txt', 2503))


assert task2('test_input.txt', 1000) == 689
print(task2('input.txt', 2503))
