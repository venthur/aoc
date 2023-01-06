def run(registers, code):
    ptr = 0
    while ptr < len(code):
        token = code[ptr]
        # print(f'{ptr} {token} {registers}')
        if token[0] == 'hlf':
            registers[token[1]] //= 2
            ptr += 1
        elif token[0] == 'tpl':
            registers[token[1]] *= 3
            ptr += 1
        elif token[0] == 'inc':
            registers[token[1]] += 1
            ptr += 1
        elif token[0] == 'jmp':
            ptr += token[-1]
        elif token[0] == 'jie':
            if registers[token[1]] % 2 == 0:
                ptr += token[-1]
            else:
                ptr += 1
        elif token[0] == 'jio':
            if registers[token[1]] == 1:
                ptr += token[-1]
            else:
                ptr += 1
        else:
            raise ValueError
    return registers


def task1(fn, a=0, b=0):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    code = []
    for line in lines:
        tokens = line.split()
        tokens = [t.rstrip(',') for t in tokens]
        if tokens[0] in ['jio', 'jie', 'jmp']:
            tokens[-1] = int(tokens[-1])
        code.append(tokens)

    registers = run(dict(a=a, b=b), code)
    return registers


assert task1('test_input.txt')['a'] == 2

print(task1('input.txt')['b'])
print(task1('input.txt', a=1)['b'])
