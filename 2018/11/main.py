def task1(serialnr):

    power = dict()
    for y in range(1, 300+1):
        for x in range(1, 300+1):
            rack_id = x + 10
            p = rack_id * y
            p += serialnr
            p *= rack_id
            p //= 100
            p %= 10
            p -= 5
            power[x, y] = p

    power3 = dict()
    for y in range(1, 300+1-3):
        for x in range(1, 300+1-3):
            power3[x, y] = (
                power[x, y] + power[x+1, y] + power[x+2, y] +
                power[x, y+1] + power[x+1, y+1] + power[x+2, y+1] +
                power[x, y+2] + power[x+1, y+2] + power[x+2, y+2]
            )

    power3 = list(power3.items())
    power3.sort(key=lambda x: x[-1])
    return power3[-1][0]


def task2(serialnr):

    power = dict()
    for y in range(1, 300+1):
        for x in range(1, 300+1):
            rack_id = x + 10
            p = rack_id * y
            p += serialnr
            p *= rack_id
            p //= 100
            p %= 10
            p -= 5
            power[x, y] = p

    # calculate the summed area table
    sat = dict()
    for y in range(1, 300+1):
        for x in range(1, 300+1):
            sat[x, y] = (
                power[x, y]
                + sat.get((x, y-1), 0)
                + sat.get((x-1, y), 0)
                - sat.get((x-1, y-1), 0)
            )

    value, vx, vy, vs = 0, 0, 0, 0
    for y in range(1, 300+1):
        for x in range(1, 300+1):
            for s in range(1, 300):
                try:
                    v = sat[x+s, y+s] + sat[x, y] - sat[x, y+s] - sat[x+s, y]
                    if v > value:
                        value = v
                        vx, vy, vs = x+1, y+1, s
                except KeyError:
                    pass

    return vx, vy, vs


assert task1(42) == (21, 61)
print(task1(6303))

assert task2(42) == (232, 251, 12)
print(task2(6303))
