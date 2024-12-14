import functools


def read_input(fn):
    with open(fn) as fh:
        return [int(i) for i in fh.read().strip().split()]


def task1(fn):
    stones = read_input(fn)
    for i in range(25):
        stones2 = []
        for stone in stones:
            if stone == 0:
                stones2.append(1)
            elif len(str(stone)) % 2 == 0:
                l = len(str(stone)) // 2
                stones2.append(int(str(stone)[:l]))
                stones2.append(int(str(stone)[l:]))
            else:
                stones2.append(stone*2024)
        stones = stones2
    return len(stones)


@functools.cache
def calc_stones(stone, blinks):
    if blinks == 0:
        return 1
    if stone == 0:
        val = calc_stones(1, blinks-1)
    elif len(str(stone)) % 2 == 0:
        l = len(str(stone)) // 2
        val = calc_stones(int(str(stone)[:l]), blinks-1) + calc_stones(int(str(stone)[l:]), blinks-1)
    else:
        val = calc_stones(stone*2024, blinks-1)
    return val


def task2(fn):
    stones = read_input(fn)
    s = 0
    for stone in stones:
        s += calc_stones(stone, 75)
    return s


assert task1('test_input.txt') == 55312
print(task1('input.txt'))

print(task2('input.txt'))
