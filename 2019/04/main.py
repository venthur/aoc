from itertools import pairwise


def task1(r):
    start, end = [int(n) for n in r.split('-')]

    count = 0
    for i in range(start, end+1):
        consecutive = False
        for a, b in pairwise(str(i)):
            if a > b:
                break
            if a == b:
                consecutive = True
        else:
            if consecutive:
                count += 1

    return count


def task2(r):
    start, end = [int(n) for n in r.split('-')]

    count = 0
    for i in range(start, end+1):
        for a, b in pairwise(str(i)):
            if a > b:
                break
        else:
            si = str(i)
            if 2 in [si.count(c) for c in si]:
                count += 1

    return count


print(task1('124075-580769'))

print(task2('124075-580769'))
