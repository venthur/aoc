test_input = """\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
""".splitlines()

test_input2 = """\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
""".splitlines()


with open('input.txt') as fh:
    input_ = fh.read().splitlines()


def task1(input_):
    visited = set()
    xt, yt = 0, 0
    xh, yh = 0, 0

    for line in input_:
        direction, steps = line.split()
        steps = int(steps)
        # calculate pos for head
        for i in range(steps):

            if direction == "R":
                xh += 1
            elif direction == "L":
                xh -= 1
            elif direction == "U":
                yh += 1
            elif direction == "D":
                yh -= 1


            # calculate pos for tail
            if xh == xt:
                if yh-1 > yt:
                    yt += 1
                elif yh+1 < yt:
                    yt -= 1
            elif yh == yt:
                if xh-1 > xt:
                    xt += 1
                elif xh+1 < xt:
                    xt -= 1
            else:
                if yh-1 > yt:
                    yt += 1
                    xt = xh
                elif yh+1 < yt:
                    yt -= 1
                    xt = xh
                if xh-1 > xt:
                    xt += 1
                    yt = yh
                elif xh+1 < xt:
                    xt -= 1
                    yt = yh

            #print(f"{direction}\n{xh, yt} -> {(xt, yt)}")
            visited.add((xt, yt))

    #print(sorted(visited))

    return len(visited)


def task2(input_):
    visited = set()
    # 0 is head, 9 is tail
    knots = [[0, 0] for i in range(10)]

    for line in input_:
        direction, steps = line.split()
        steps = int(steps)
        for i in range(steps):

            # calculate pos for head
            if direction == "R":
                knots[0][0] += 1
            elif direction == "L":
                knots[0][0] -= 1
            elif direction == "U":
                knots[0][1] += 1
            elif direction == "D":
                knots[0][1] -= 1

            # calculate pos for tail
            for t in range(1, 10):
                dx = knots[t-1][0] - knots[t][0]
                dy = knots[t-1][1] - knots[t][1]

                # same spot
                if dx == dy == 0:
                    pass

                # direct neighbors
                elif (
                    (dx == 0 and abs(dy) == 1) or
                    (abs(dx) == 1 and dy == 0) or
                    (abs(dx) == abs(dy) == 1)
                ):
                    pass

                # same col / 2 rows apart
                elif dx == 0 and dy == 2:
                    knots[t][1] += 1
                elif dx == 0 and dy == -2:
                    knots[t][1] -= 1

                # same row / 2 cols apart
                elif dx == 2 and dy == 0:
                    knots[t][0] += 1
                elif dx == -2 and dy == 0:
                    knots[t][0] -= 1

                # 1 col / 2 rows apart
                elif abs(dx) == 1 and dy == 2:
                    knots[t][0] = knots[t-1][0]
                    knots[t][1] += 1
                elif abs(dx) == 1 and dy == -2:
                    knots[t][0] = knots[t-1][0]
                    knots[t][1] -= 1

                # 1 row / 2 cols apart
                elif dx == 2 and abs(dy) == 1:
                    knots[t][0] += 1
                    knots[t][1] = knots[t-1][1]
                elif dx == -2 and abs(dy) == 1:
                    knots[t][0] -= 1
                    knots[t][1] = knots[t-1][1]

                # undefined
                elif dx == 2 and dy == 2:
                    knots[t][0] += 1
                    knots[t][1] += 1
                elif dx == 2 and dy == -2:
                    knots[t][0] += 1
                    knots[t][1] -= 1
                elif dx == -2 and dy == 2:
                    knots[t][0] -= 1
                    knots[t][1] += 1
                elif dx == -2 and dy == -2:
                    knots[t][0] -= 1
                    knots[t][1] -= 1

            visited.add(tuple(knots[-1]))

    return len(visited)


assert task1(test_input) == 13
print(task1(input_))

assert task2(test_input) == 1
assert task2(test_input2) == 36
print(task2(input_))
