def task1(fn, l):

    with open(fn) as fh:
        containers = [int(i) for i in fh.read().splitlines()]

    def measure(containers, candidates, l):
        if sum(containers) == l:
            return 1
        if sum(containers) > l:
            return 0
        if sum(containers) + sum(candidates) < l:
            return 0
        if not candidates:
            return 0
        return (
            measure(containers + [candidates[0]], candidates[1:], l)
            + measure(containers, candidates[1:], l)
        )

    combinations = measure([], containers, l)
    return combinations


def task2(fn, l):

    with open(fn) as fh:
        containers = [int(i) for i in fh.read().splitlines()]

    def measure(containers, candidates, l, target_c):
        if len(containers) == target_c and sum(containers) == l:
            return 1
        if (
            sum(containers) > l or
            sum(containers) + sum(candidates) < l or
            not candidates or
            len(containers) == target_c
        ):
            return 0
        return (
            measure(containers + [candidates[0]], candidates[1:], l, target_c)
            + measure(containers, candidates[1:], l, target_c)
        )

    for i in range(len(containers)):
        combinations = measure([], containers, l, i)
        if combinations > 0:
            return combinations


assert task1('test_input.txt', 25) == 4
print(task1('input.txt', 150))

assert task2('test_input.txt', 25) == 3
print(task2('input.txt', 150))
