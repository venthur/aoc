def flip(pattern):
    return pattern[::-1]


def rotate(pattern):
    if len(pattern) == 2:
        return ((pattern[0][1], pattern[1][1]), (pattern[0][0], pattern[1][0]))
    elif len(pattern) == 3:
        return (
            (pattern[0][2], pattern[1][2], pattern[2][2]),
            (pattern[0][1], pattern[1][1], pattern[2][1]),
            (pattern[0][0], pattern[1][0], pattern[2][0])
        )


def parse(s):
    in_, out = s.split(' => ')

    in_ = tuple(
        tuple(True if c == '#' else False for c in block)
        for block
        in in_.split('/')
    )

    out = tuple(
        tuple(True if c == '#' else False for c in block)
        for block
        in out.split('/')
    )

    return in_, out


def task1(fn, iterations):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    # .#.
    # ..#
    # ###
    image = (
        (False, True,  False),
        (False, False, True),
        (True,  True,  True)
    )

    patterns = dict()
    for line in lines:
        in_, out = parse(line)
        # prepare all patterns...
        for i in range(4):
            in_ = rotate(in_)
            patterns[in_] = out

        in_ = flip(in_)
        for i in range(4):
            in_ = rotate(in_)
            patterns[in_] = out

    for i in range(iterations):

        if len(image) % 2 == 0:
            target = 3 * len(image) // 2
            image2 = [[False for j in range(target)] for jj in range(target)]
            for row in range(len(image) // 2):
                for col in range(len(image) // 2):
                    # get the pattern
                    pattern = tuple(tuple(r[col*2:col*2+2]) for r in image[row*2:row*2+2])
                    p = patterns[pattern]
                    for j, prow in enumerate(p):
                        image2[row*3+j][col*3:col*3+3] = prow
            image = image2[:]

        elif len(image) % 3 == 0:
            target = 4 * len(image) // 3
            image2 = [[False for j in range(target)] for jj in range(target)]
            for row in range(len(image) // 3):
                for col in range(len(image) // 3):
                    # get the pattern
                    pattern = tuple(tuple(r[col*3:col*3+3]) for r in image[row*3:row*3+3])
                    p = patterns[pattern]
                    for j, prow in enumerate(p):
                        image2[row*4+j][col*4:col*4+4] = prow
            image = image2[:]

        #print()
        #for r in image:
        #    print(''.join(['#' if c else '.' for c in r]))

    return sum(sum(t) for t in image)


assert task1('test_input.txt', 2) == 12
print(task1('input.txt', 5))

print(task1('input.txt', 18))
