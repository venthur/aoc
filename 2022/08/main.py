test_case = """\
30373
25512
65332
33549
35390
""".splitlines()


with open('input.txt') as fh:
    input_ = fh.read().splitlines()


def task1(input_):
    height = len(input_)
    width = len(input_[0])
    count = 0

    for y in range(height):
        for x in range(width):

            visible = False
            h = input_[y][x]

            # left
            visible2 = True
            for x2 in range(0, x):
                if input_[y][x2] >= h:
                    visible2 = False
                    break
            if visible2:
                visible = True

            # right
            visible2 = True
            for x2 in range(x+1, width):
                if input_[y][x2] >= h:
                    visible2 = False
                    break
            if visible2:
                visible = True

            # top
            visible2 = True
            for y2 in range(0, y):
                if input_[y2][x] >= h:
                    visible2 = False
                    break
            if visible2:
                visible = True

            # bottom
            visible2 = True
            for y2 in range(y+1, height):
                if input_[y2][x] >= h:
                    visible2 = False
                    break
            if visible2:
                visible = True

            if visible:
                count += 1

    return count


def task2(input_):
    height = len(input_)
    width = len(input_[0])
    best_score = 0

    for y in range(height):
        for x in range(width):

            h = input_[y][x]

            # left
            l = x
            for x2 in range(x-1, -1, -1):
                if input_[y][x2] >= h:
                    l = abs(x2 - x)
                    break

            # right
            r = width-x-1
            for x2 in range(x+1, width):
                if input_[y][x2] >= h:
                    r = abs(x2 - x)
                    break

            # top
            t = y
            for y2 in range(y-1, -1, -1):
                if input_[y2][x] >= h:
                    t = abs(y2 - y)
                    break

            # bottom
            b = height-y-1
            for y2 in range(y+1, height):
                if input_[y2][x] >= h:
                    b = abs(y2 - y)
                    break


            score = l * r * t * b
            if score > best_score:
                best_score = score

    return best_score


assert task1(test_case) == 21
print(task1(input_))

assert task2(test_case) == 8
print(task2(input_))
