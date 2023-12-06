def task1(fn):
    with open(fn) as fh:
        table = []
        for line in fh.read().splitlines():
            label, numbers = line.split(': ')
            numbers = map(int, numbers.split())
            table.append(numbers)
        table = list(zip(*table))

    result = 1
    for time, distance in table:
        wins = 0
        for i in range(time):
            v = i
            d = v * (time - i)
            if d > distance:
                wins += 1
        result *= wins

    return result


def task2(fn):
    with open(fn) as fh:
        table = []
        for line in fh.read().splitlines():
            _, numbers = line.split(': ')
            numbers = numbers.replace(' ', '')
            numbers = map(int, numbers.split())
            table.append(numbers)
        table = list(zip(*table))

    result = 1
    for time, distance in table:
        wins = 0
        for i in range(time):
            v = i
            d = v * (time - i)
            if d > distance:
                wins += 1
        result *= wins

    return result


assert task1('test_input.txt') == 288
print(task1('input.txt'))

assert task2('test_input.txt') == 71503
print(task2('input.txt'))
