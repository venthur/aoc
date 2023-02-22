from itertools import combinations


def task1(fn, preamble):
    with open(fn) as fh:
        numbers = [int(n) for n in fh.read().splitlines()]

    for i in range(preamble, len(numbers)-1):
        for a, b in combinations(numbers[i-preamble:i], 2):
            if a + b == numbers[i]:
                break
        else:
            return numbers[i]


def task2(fn, preamble):
    with open(fn) as fh:
        numbers = [int(n) for n in fh.read().splitlines()]

    number = task1(fn, preamble)

    for l in range(2, preamble+1):
        for i in range(len(numbers)-1):
            testrange = numbers[i:i+l]
            if sum(testrange) == number:
                return min(testrange) + max(testrange)


assert task1('test_input0.txt', 5) == 127
print(task1('input.txt', 25))

assert task2('test_input0.txt', 5) == 62
print(task2('input.txt', 25))
