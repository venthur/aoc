def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    n = 10007
    c = 2019
    a, b = 1, 0
    for line in lines:
        if line.startswith('deal with increment'):
            la = int(line.split()[-1])
            lb = 0
        elif line.startswith('deal into new stack'):
            la = -1
            lb = -1
        elif line.startswith('cut'):
            la = 1
            lb = -int(line.split()[-1])
        a = (la * a) % n
        b = (la * b + lb) % n
    c = (a * c + b) % n

    return c


def inv(a, n):
    return pow(a, n-2, n)


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    n = 119315717514047
    M = 101741582076661
    c = 2020
    a, b = 1, 0
    for line in lines:
        if line.startswith('deal with increment'):
            la = int(line.split()[-1])
            lb = 0
        elif line.startswith('deal into new stack'):
            la = -1
            lb = -1
        elif line.startswith('cut'):
            la = 1
            lb = -int(line.split()[-1])
        a = (la * a) % n
        b = (la * b + lb) % n

    Ma = pow(a, M, n)
    Mb = (b * (Ma - 1) * inv(a-1, n)) % n

    return ((c - Mb) * inv(Ma, n)) % n


print(task1('input.txt'))
print(task2('input.txt'))
