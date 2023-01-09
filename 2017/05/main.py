def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    lines = [int(n) for n in lines]

    ptr = 0
    jumps = 0
    while 0 <= ptr <= len(lines)-1:
        ptr2 = ptr + lines[ptr]
        lines[ptr] += 1
        ptr = ptr2
        jumps += 1
    return jumps


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    lines = [int(n) for n in lines]

    ptr = 0
    jumps = 0
    while 0 <= ptr <= len(lines)-1:
        ptr2 = ptr + lines[ptr]
        if lines[ptr] >= 3:
            lines[ptr] -= 1
        else:
            lines[ptr] += 1
        ptr = ptr2
        jumps += 1
    return jumps


assert task1('test_input.txt') == 5
print(task1('input.txt'))


assert task2('test_input.txt') == 10
print(task2('input.txt'))
