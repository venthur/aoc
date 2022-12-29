def task1(n_elves):
    elves = [i+1 for i in range(n_elves)]

    while True:
        if len(elves) == 1:
            return elves[0]
        odd = len(elves) % 2 != 0
        del elves[1::2]
        if odd:
            elves = [elves[-1]] + elves[:-1]


def task2(n_elves):
    elves = [i+1 for i in range(n_elves)]

    i = 0
    while True:
        i += 1
        if len(elves) == 1:
            return elves[0]
        del elves[len(elves)//2]
        elves.append(elves.pop(0))


assert task1(5) == 3
print(task1(3012210))

assert task2(5) == 2
assert task2(10) == 1
print(task2(3012210))
