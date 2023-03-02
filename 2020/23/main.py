from collections import deque
from itertools import pairwise


def task1(in_, rounds):
    circle = deque([int(n) for n in in_])
    minv, maxv = min(circle), max(circle)
    for i in range(rounds):
        n = circle.popleft()
        a, b, c = circle.popleft(), circle.popleft(), circle.popleft()
        circle.appendleft(n)

        n -= 1
        while n in (a, b, c) or n < minv:
            n -= 1
            if n < minv:
                n = maxv

        shift = circle.index(n)
        circle.rotate(-shift)
        n = circle.popleft()
        circle.appendleft(c)
        circle.appendleft(b)
        circle.appendleft(a)
        circle.appendleft(n)
        circle.rotate(shift-1)

    shift = circle.index(1)
    circle.rotate(-shift-1)
    return ''.join(str(n) for n in list(circle))[:-1]


def task2(in_):
    in_ = [int(n) for n in in_]
    for i in range(max(in_) + 1, 1_000_000+1):
        in_.append(i)
    minv, maxv = min(in_), max(in_)

    succ = [None for i in range(1_000_000+1)]
    for a, b in pairwise(in_):
        succ[a] = b
    succ[in_[-1]] = in_[0]

    n = in_[0]
    for i in range(10_000_000):
        a = succ[n]
        b = succ[a]
        c = succ[b]

        m = n-1
        while m in (a, b, c) or m < minv:
            m -= 1
            if m < minv:
                m = maxv

        # now: m x | n a b c d
        # target: m a b c x | n d
        succ[n] = succ[c]
        succ[c] = succ[m]
        succ[m] = a

    print(succ[:100])
    return succ[1] * succ[succ[1]]



assert task1("389125467", 10) == "92658374"
assert task1("389125467", 100) == "67384529"
print(task1("952316487", 100))

assert task2("389125467") == 149245887792
print(task2("952316487"))

