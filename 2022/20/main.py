from collections import deque


def read_input(fn):
    with open(fn) as fh:
        numbers = [(i, int(n)) for i, n in enumerate(fh.read().splitlines())]

    return deque(numbers)


def mix(numbers):
    for i in range(len(numbers)):
        while numbers[0][0] != i:
            numbers.rotate(-1)

        current = numbers.popleft()
        shift = current[1] % len(numbers)
        numbers.rotate(-shift)
        numbers.append(current)

    return numbers


def task1(fn):
    numbers = read_input(fn)

    numbers = mix(numbers)
    numbers = [n for i, n in numbers]
    sum_ = 0
    for i in 1000, 2000, 3000:
        sum_ += numbers[(numbers.index(0) + i) % len(numbers)]

    return sum_


def task2(fn):
    numbers = read_input(fn)

    DECRYPTION_KEY = 811589153

    numbers = deque([(i, n*DECRYPTION_KEY) for i, n in numbers])

    for _ in range(10):
        numbers = mix(numbers)

    numbers = [n for i, n in numbers]
    sum_ = 0
    for i in 1000, 2000, 3000:
        sum_ += numbers[(numbers.index(0) + i) % len(numbers)]

    return sum_


assert task1('test_input0.txt') == 3
print(task1('input.txt'))

assert task2('test_input0.txt') == 1623178306
print(task2('input.txt'))
