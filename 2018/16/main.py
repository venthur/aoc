def addr(r, a, b, c):
    r = r[:]
    r[c] = r[a] + r[b]
    return r


def addi(r, a, b, c):
    r = r[:]
    r[c] = r[a] + b
    return r


def mulr(r, a, b, c):
    r = r[:]
    r[c] = r[a] * r[b]
    return r


def muli(r, a, b, c):
    r = r[:]
    r[c] = r[a] * b
    return r


def banr(r, a, b, c):
    r = r[:]
    r[c] = r[a] & r[b]
    return r


def bani(r, a, b, c):
    r = r[:]
    r[c] = r[a] & b
    return r


def borr(r, a, b, c):
    r = r[:]
    r[c] = r[a] | r[b]
    return r


def bori(r, a, b, c):
    r = r[:]
    r[c] = r[a] | b
    return r


def setr(r, a, _, c):
    r = r[:]
    r[c] = r[a]
    return r


def seti(r, a, _, c):
    r = r[:]
    r[c] = a
    return r


def getir(r, a, b, c):
    r = r[:]
    r[c] = 1 if a > r[b] else 0
    return r


def getri(r, a, b, c):
    r = r[:]
    r[c] = 1 if r[a] > b else 0
    return r


def getrr(r, a, b, c):
    r = r[:]
    r[c] = 1 if r[a] > r[b] else 0
    return r


def equir(r, a, b, c):
    r = r[:]
    r[c] = 1 if a == r[b] else 0
    return r


def equri(r, a, b, c):
    r = r[:]
    r[c] = 1 if r[a] == b else 0
    return r


def equrr(r, a, b, c):
    r = r[:]
    r[c] = 1 if r[a] == r[b] else 0
    return r


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    samples = []
    for line in lines:
        if line.startswith('Before'):
            before = eval(line.split(': ')[-1])
        elif line.startswith('After'):
            after = eval(line.split(': ')[-1])
            samples.append((before, after, cmd))
        else:
            cmd = [int(i) for i in line.split()]

    possible_opcodes = []
    for before, after, cmd in samples:
        possible = 0
        for op in (
            addr, addi, mulr, muli,
            banr, bani, borr, bori,
            setr, seti,
            getir, getri, getrr,
            equir, equri, equrr,
        ):
            if op(before, *cmd[1:]) == after:
                possible += 1
                print(f'{op} {before} {cmd[1:]} -> {after}')
        possible_opcodes.append(possible)

    return len(list(filter(lambda x: x >= 3, possible_opcodes)))


print(task1('input.txt'))
