from collections import deque


def task1(steps):
    list_ = [0]
    pos = 0
    for i in range(2017):
        pos += steps
        pos %= len(list_)
        list_.insert(pos+1, i+1)
        pos += 1

    return list_[pos+1]


def task2(steps):
    dq = deque([0])
    for i in range(50000000):
        dq.rotate(-steps)
        dq.append(i+1)

    return dq[dq.index(0)+1]


assert task1(3) == 638
print(task1(377))

print(task2(377))
