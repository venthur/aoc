def task1(fn):
    with open(fn) as fh:
        joltage = 0
        for line in fh:
            numbers = [int(i) for i in line.strip()]
            a = max(numbers[:-1])
            b = max(numbers[numbers.index(a)+1:])
            v = 10*a+b
            joltage += v

    return joltage


def task2(fn):
    with open(fn) as fh:
        joltage = 0
        for line in fh:
            line = line.strip()
            numbers = [int(i) for i in line]
            v = 0
            for i in range(11, -1, -1):
                to_test = numbers[:len(numbers)-i]
                a = max(to_test)
                v *= 10
                v += a
                numbers = numbers[numbers.index(a)+1:]
            joltage += v

    return joltage


assert task1('test_input.txt') == 357
print(task1('input.txt'))

assert task2('test_input.txt') == 3121910778619
print(task2('input.txt'))
