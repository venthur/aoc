from collections import deque


def pattern(i):
    PATTERN = [0, 1, 0, -1]
    pattern = []
    for p in PATTERN:
        pattern.extend([p]*i)
    pattern = deque(pattern)
    pattern.rotate(-1)
    while True:
        yield pattern[0]
        pattern.rotate(-1)


def fft(nrs, phases):
    for phase in range(phases):
        print(phase, end='\r')
        nrs2 = []
        for i, nr in enumerate(nrs):
            p = pattern(i+1)
            nrs2.append(abs(sum([n * next(p) for n in nrs])) % 10)
        nrs = nrs2[:]
    return nrs


def task1(fn):
    with open(fn) as fh:
        data = [int(n) for n in fh.read().strip()]

    res = fft(data, 100)[:8]
    return ''.join([str(c) for c in res])


def task2(fn):
    with open(fn) as fh:
        data = [int(n) for n in fh.read().strip()]
    data *= 10000
    skip = int(''.join([str(c) for c in data[:7]]))
    data = data[skip:]
    for _ in range(100):
        for i in range(len(data)-1, 0, -1):
            data[i-1] = (data[i-1]+data[i]) % 10

    res = data[:8]
    return ''.join([str(c) for c in res])


print(task1('input.txt'))
print(task2('input.txt'))
