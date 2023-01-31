def task1():
    d = 0
    while True:
        e = d | 65536
        d = 1765573
        while True:
            a = e & 255
            d += a
            d &= 16777215
            d *= 65899
            d &= 16777215
            if (256 > e):
                return d
            e //= 256


def task2():
    seen = set()
    last = -1
    d = 0
    while True:
        e = d | 65536
        d = 1765573
        while True:
            a = e & 255
            d += a
            d &= 16777215
            d *= 65899
            d &= 16777215
            if (256 > e):
                if d not in seen:
                    seen.add(d)
                    last = d
                    break
                else:
                    return last
            e //= 256


print(task1())
print(task2())
