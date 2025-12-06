def task1(fn):
    lines = []
    with open(fn) as fh:
        for line in fh:
            lines.append(line.strip())

    numbers = []
    operators = []
    for line in lines:
        try:
            n = [int(i) for i in line.split()]
            numbers.append(n)
        except ValueError:
            break
    operators = line.split()

    result = 0
    for i in range(len(operators)):
        ans = 1 if operators[i] == '*' else 0
        for row in numbers:
            if operators[i] == '*':
                ans *= row[i]
            else:
                ans += row[i]
        result += ans

    return result


def task2(fn):
    lines = []
    with open(fn) as fh:
        for line in fh:
            lines.append(line)

    numbers, operators = lines[:-1], lines[-1]
    transposed = [''.join(x).strip() for x in zip(*numbers)]
    numbers = transposed[:]
    operators = operators.split()

    result = 0
    op = operators.pop(0)
    ans = 1 if op == '*' else 0
    for n in numbers:
        if not n:
            result += ans
            try:
                op = operators.pop(0)
            except IndexError:
                break
            ans = 1 if op == '*' else 0
            continue
        if op == '*':
            ans *= int(n)
        else:
            ans += int(n)

    return result


assert task1('test_input.txt') == 4277556
print(task1('input.txt'))

assert task2('test_input.txt') == 3263827
print(task2('input.txt'))
