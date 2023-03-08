from operator import add, mul, gt, lt, eq


def parse(line):
    bits = ''.join(bin(int(char, 16))[2:].zfill(4) for char in line)
    ops = add, mul, lambda *x: min(x), lambda *x: max(x), None, gt, lt, eq
    pos = 0
    version = 0

    def read(size):
        nonlocal pos

        if pos > len(bits):
            return 0

        v = int(bits[pos:pos+size], 2)
        pos += size
        return v

    def packet():
        nonlocal version

        version += read(3)

        typeid = read(3)
        if typeid == 4:
            go, total = read(1), read(4)
            while go:
                go, total = read(1), total << 4 | read(4)
        elif read(1) == 0:
            length = read(15) + pos
            total = packet()
            while pos < length:
                total = ops[typeid](total, packet())
        else:
            count = read(11)
            total = packet()
            for _ in range(count - 1):
                total = ops[typeid](total, packet())

        return total

    total = packet()

    return version, total


def task1(fn):
    with open(fn) as fh:
        data = fh.read().strip()

    return parse(data)


print(task1('input.txt'))
