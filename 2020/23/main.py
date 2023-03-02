from collections import deque


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
        print(n)

        circle.insert(circle.index(n)+1, a)
        circle.insert(circle.index(n)+2, b)
        circle.insert(circle.index(n)+3, c)
        print(circle)


assert task1("389125467", 10) == "92658374"
assert task1("389125467", 100) == "67384529"
print(task1("952316487", 100))
