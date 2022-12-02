with open('input.txt') as fh:
    input_ = fh.read().strip()


def part1(input_):
    seen = set()
    x, y = 0, 0
    seen.add((x, y))
    for direction in input_:
        if direction == "^":
            y += 1
        elif direction == "v":
            y -= 1
        elif direction == ">":
            x += 1
        elif direction == "<":
            x -= 1
        seen.add((x, y))
    print(len(seen))


def part2(input_):
    seen = set()

    x, y = 0, 0
    seen.add((x, y))
    for direction in input_[::2]:
        if direction == "^":
            y += 1
        elif direction == "v":
            y -= 1
        elif direction == ">":
            x += 1
        elif direction == "<":
            x -= 1
        seen.add((x, y))

    x, y = 0, 0
    seen.add((x, y))
    for direction in input_[1::2]:
        if direction == "^":
            y += 1
        elif direction == "v":
            y -= 1
        elif direction == ">":
            x += 1
        elif direction == "<":
            x -= 1
        seen.add((x, y))

    print(len(seen))


part1(input_)
part2(input_)
