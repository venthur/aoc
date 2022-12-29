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
        if i % 100 == 0:
            print(len(elves))
        if len(elves) == 1:
            return elves[0]
        to_remove = (i + len(elves)//2) % len(elves)
        del elves[to_remove]
        if i >= len(elves):
            i %= len(elves)
        else:
            i += 1

assert task1(5) == 3
print(task1(3012210))

assert task2(5) == 2
print(task2(3012210))


# 1 2 3 4 5 i=0
# *   *
# 
# 1 2 4 5   i=1
#   *   *
# 
# 
# 1 2 4     i=2
# ^   *
# 
# 2 4       i=0
# * ^
