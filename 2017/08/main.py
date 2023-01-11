from collections import defaultdict


def task1(fn):

    with open(fn) as fh:
        lines = fh.read().splitlines()

    lines2 = []
    for line in lines:
        tokens = line.split()
        tokens2 = []
        for token in tokens:
            if token.startswith('-') or token.isnumeric():
                token = int(token)
            tokens2.append(token)
        lines2.append(tokens2)
    lines = lines2[:]

    registers = defaultdict(lambda: 0)
    for tokens in lines:
        register = tokens[0]
        incdec = tokens[1]
        value = tokens[2]
        a = tokens[-3]
        if not isinstance(a, int):
            a = registers[a]
        cmp = tokens[-2]
        b = tokens[-1]
        if not isinstance(b, int):
            b = registers[b]

        if eval(" ".join([str(a), cmp, str(b)])):
            if incdec == 'inc':
                registers[register] += value
            elif incdec == 'dec':
                registers[register] -= value

    return max(registers.values())


def task2(fn):

    with open(fn) as fh:
        lines = fh.read().splitlines()

    lines2 = []
    for line in lines:
        tokens = line.split()
        tokens2 = []
        for token in tokens:
            if token.startswith('-') or token.isnumeric():
                token = int(token)
            tokens2.append(token)
        lines2.append(tokens2)
    lines = lines2[:]

    maxv = None
    registers = defaultdict(lambda: 0)
    for tokens in lines:
        register = tokens[0]
        incdec = tokens[1]
        value = tokens[2]
        a = tokens[-3]
        if not isinstance(a, int):
            a = registers[a]
        cmp = tokens[-2]
        b = tokens[-1]
        if not isinstance(b, int):
            b = registers[b]

        if eval(" ".join([str(a), cmp, str(b)])):
            if incdec == 'inc':
                registers[register] += value
            elif incdec == 'dec':
                registers[register] -= value

        if maxv is None or max(registers.values()) > maxv:
            maxv = max(registers.values())

    return maxv


assert task1('test_input.txt') == 1
print(task1('input.txt'))

assert task2('test_input.txt') == 10
print(task2('input.txt'))
