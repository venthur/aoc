from collections import defaultdict


def task1(numbers, rounds):

    counter = defaultdict(int)
    last = dict()
    for i, n in enumerate(numbers):
        counter[n] += 1
        if i < len(numbers)-1:
            last[n] = i
    lastn = n

    for i in range(len(numbers), rounds):
        n = counter[lastn]
        if n == 1:
            last[lastn] = i-1
            lastn = 0
            counter[lastn] += 1
        else:
            j = i - last[lastn] - 1
            last[lastn] = i-1
            lastn = j
            counter[lastn] += 1

    return lastn


assert task1((0, 3, 6), 2020) == 436
assert task1((1, 3, 2), 2020) == 1
print(task1((9, 3, 1, 0, 8, 4), 2020))

print(task1((9, 3, 1, 0, 8, 4), 30000000))
