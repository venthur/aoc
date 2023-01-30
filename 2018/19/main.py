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


def gtir(r, a, b, c):
    r = r[:]
    r[c] = 1 if a > r[b] else 0
    return r


def gtri(r, a, b, c):
    r = r[:]
    r[c] = 1 if r[a] > b else 0
    return r


def gtrr(r, a, b, c):
    r = r[:]
    r[c] = 1 if r[a] > r[b] else 0
    return r


def eqir(r, a, b, c):
    r = r[:]
    r[c] = 1 if a == r[b] else 0
    return r


def eqri(r, a, b, c):
    r = r[:]
    r[c] = 1 if r[a] == b else 0
    return r


def eqrr(r, a, b, c):
    r = r[:]
    r[c] = 1 if r[a] == r[b] else 0
    return r


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    code = []
    for line in lines:
        if line.startswith('#'):
            ip = int(line.split()[-1])
        else:
            cmd, *tokens = line.split()
            tokens = [int(n) for n in tokens]
            code.append((cmd, *tokens))

    registers = [0 for i in range(6)]
    while 0 <= registers[ip] < len(code):
        cmd, *params = code[registers[ip]]
        registers = eval(
            f'{cmd}(registers, {params[0]}, {params[1]}, {params[2]})'
        )
        registers[ip] += 1
    return registers[0]


def task2(fn):
    D = 10551389
    s = 0
    for i in range(1, D+1):
        if D % i == 0:
            s += i
    return s


assert task1('test_input.txt') == 7
print(task1('input.txt'))

print(task2('input.txt'))
