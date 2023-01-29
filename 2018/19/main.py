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


assert task1('test_input.txt') == 7
print(task1('input.txt'))


# #ip 3         A B C ip D E
# addi 3 16 3   
# seti 1 2 5
# seti 1 3 2
# mulr 5 2 1
# eqrr 1 4 1
# addr 1 3 3
# addi 3 1 3
# addr 5 0 0
# addi 2 1 2
# gtrr 2 4 1
# addr 3 1 3
# seti 2 5 3
# addi 5 1 5
# gtrr 5 4 1
# addr 1 3 3
# seti 1 2 3
# mulr 3 3 3
# addi 4 2 4
# mulr 4 4 4
# mulr 3 4 4
# muli 4 11 4
# addi 1 6 1
# mulr 1 3 1
# addi 1 21 1
# addr 4 1 4
# addr 3 0 3
# seti 0 3 3
# setr 3 4 1
# mulr 1 3 1
# addr 3 1 1
# mulr 3 1 1
# muli 1 14 1
# mulr 1 3 1
# addr 4 1 4
# seti 0 3 0
# seti 0 7 3
