def read_input(fn):
    input_ = []
    with open(fn) as fh:
        for line in fh:
            result, rest = line.split(':')
            input_.append((int(result), tuple(int(i) for i in rest.split())))
    return input_


def is_valid(result, values):

    if len(values) == 1:
        return values[0] == result

    a, b, *rest = values
    return is_valid(result, (a+b, *rest)) or is_valid(result, (a*b, *rest))


def task1(fn):
    data = read_input(fn)
    s = 0
    for result, values in data:
        if is_valid(result, values):
            s += result
    return s


def is_valid2(result, values):

    if len(values) == 1:
        return values[0] == result

    if result < values[0]:
        return False

    a, b, *rest = values
    return (
        is_valid2(result, (a+b, *rest)) or
        is_valid2(result, (a*b, *rest)) or
        is_valid2(result, (int(str(a)+str(b)), *rest))
    )


def task2(fn):
    data = read_input(fn)
    s = 0
    for result, values in data:
        if is_valid2(result, values):
            s += result
    return s


assert task1('test_input.txt') == 3749
print(task1('input.txt'))

assert task2('test_input.txt') == 11387
print(task2('input.txt'))
