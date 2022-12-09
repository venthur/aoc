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


assert task1(test_input) == 13
print(task1(input_))
