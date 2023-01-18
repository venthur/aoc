with open('input.txt') as fh:
    lines = fh.read().splitlines()
lines = [int(n) for n in lines]


def task1():
    return sum(lines)


def task2():
    seen = set()
    seen.add(0)
    s = 0
    while True:
        for n in lines:
            s += n
            if s in seen:
                return s
            else:
                seen.add(s)

print(task1())
print(task2())
