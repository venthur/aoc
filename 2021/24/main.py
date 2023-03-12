def parse_input(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    return [line.split() for line in lines]


def get_adds(code):
    div1, div26 = [], []
    for i in range(0, len(code), 18):
        if code[i + 4][2] == '1':
            div1.append(int(code[i + 15][2]))
            div26.append(None)
        else:
            div1.append(None)
            div26.append(int(code[i + 5][2]))

    return div1, div26


def task1(fn):
    code = parse_input(fn)

    div1, div26 = get_adds(code)

    model = [0 for i in range(14)]
    stack = []
    for i, (a, b) in enumerate(zip(div1, div26)):
        if a:
            stack.append((i, a))
        else:
            ia, a = stack.pop()
            diff = a + b
            model[ia] = min(9, 9 - diff)
            model[i] = min(9, 9 + diff)

    return ''.join(str(i) for i in model)


def task2(fn):
    code = parse_input(fn)

    div1, div26 = get_adds(code)

    model = [0 for i in range(14)]
    stack = []
    for i, (a, b) in enumerate(zip(div1, div26)):
        if a:
            stack.append((i, a))
        else:
            ia, a = stack.pop()
            diff = a + b
            model[ia] = max(1, 1 - diff)
            model[i] = max(1, 1 + diff)

    return ''.join(str(i) for i in model)


print(task1('input.txt'))

print(task2('input.txt'))
