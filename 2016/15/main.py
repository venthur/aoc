from itertools import count


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    disks = []
    for i, line in enumerate(lines):
        tokens = line.split()
        positions = int(tokens[3])
        start = int(tokens[-1][:-1])
        disks.append((positions, start))

    for i in count():
        for j, (positions, start) in enumerate(disks):
            if (start + i + j + 1) % positions != 0:
                break
        else:
            return i


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    disks = []
    for i, line in enumerate(lines):
        tokens = line.split()
        positions = int(tokens[3])
        start = int(tokens[-1][:-1])
        disks.append((positions, start))
    disks.append((11, 0))

    for i in count():
        for j, (positions, start) in enumerate(disks):
            if (start + i + j + 1) % positions != 0:
                break
        else:
            return i


assert task1('test_input.txt') == 5
print(task1('input.txt'))

print(task2('input.txt'))
