from collections import deque, defaultdict


def task1(fn):
    with open(fn) as fh:
        data = fh.read().strip()

    players, points = int(data.split()[0]), int(data.split()[-2])

    circle = deque([0])
    score = defaultdict(lambda: 0)
    for i in range(1, points+1):
        if i % 23 == 0:
            score[i % players] += i
            circle.rotate(7)
            score[i % players] += circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(i)

    return max(score.values())


def task2(fn):
    with open(fn) as fh:
        data = fh.read().strip()

    players, points = int(data.split()[0]), int(data.split()[-2])

    circle = deque([0])
    score = defaultdict(lambda: 0)
    for i in range(1, 100*points+1):
        if i % 23 == 0:
            score[i % players] += i
            circle.rotate(7)
            score[i % players] += circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(i)

    return max(score.values())


print(task1('input.txt'))

print(task2('input.txt'))
