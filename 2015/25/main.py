def generate():
    row, col = 1, 1
    last = 20151125
    while True:
        yield last, row, col

        last *= 252533
        last %= 33554393

        if row == 1:
            row = col + 1
            col = 1
        else:
            row -= 1
            col += 1


def task1(fn):
    with open(fn) as fh:
        line = fh.read()

    target_row = int(line.split()[-3][:-1])
    target_col = int(line.split()[-1][:-1])

    for last, row, col in generate():
        if (row, col) == (target_row, target_col):
            return last


print(task1('input.txt'))
