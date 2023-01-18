from itertools import combinations


with open('input.txt') as fh:
    lines = fh.read().splitlines()


def task1():
    twos = 0
    threes = 0
    for line in lines:

        for c in set(list(line)):
            if line.count(c) == 2:
                twos += 1
                break

        for c in set(list(line)):
            if line.count(c) == 3:
                threes += 1
                break

    return twos * threes


def task2():
    for a, b in combinations(lines, 2):
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
        if diff == 1:
            letters = []
            for i in range(len(a)):
                if a[i] == b[i]:
                    letters.append(a[i])
            return ''.join(letters)


print(task1())

print(task2())
