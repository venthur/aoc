def task1(fn):
    numbers = []
    with open(fn) as fh:
        for line in fh:
            sign, number = line.strip()[0].lower(), int(line.strip()[1:])
            if sign == 'l':
                number *= -1
            numbers.append(number)

    n = 50
    counter = 0
    for nr in numbers:
        n += nr
        n %= 100
        if n == 0:
            counter += 1
    return counter


def task2(fn):
    numbers = []
    with open(fn) as fh:
        for line in fh:
            sign, number = line.strip()[0].lower(), int(line.strip()[1:])
            if sign == 'l':
                number *= -1
            numbers.append(number)

    n = 50
    counter = 0

    for nr in numbers:
        if nr >= 0:
            for _ in range(nr):
                n += 1
                n %= 100
                if n == 0:
                    counter += 1
        else:
            for _ in range(abs(nr)):
                n -= 1
                if n < 0:
                    n += 100
                if n == 0:
                    counter += 1
    return counter



assert task1('test_input.txt') == 3
print(task1('input.txt'))

assert task2('test_input.txt') == 6
print(task2('input.txt'))
