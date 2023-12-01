def task1(fn):
    with open(fn) as fh:
        s = 0
        for line in fh.read().splitlines():
            for c in line:
                if c.isdigit():
                    a = int(c) * 10
                    break
            for c in reversed(line):
                if c.isdigit():
                    b = int(c)
                    break
            s += a + b
    return s


def task2(fn):
    NUMBERS = [
        'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
    ]

    with open(fn) as fh:
        s = 0
        for line in fh.read().splitlines():
            for i, c in enumerate(line):
                if c.isdigit():
                    a = int(c) * 10
                    break
                for n in NUMBERS:
                    if line[i:].startswith(n):
                        a = (NUMBERS.index(n) + 1) * 10
                        break
                # break outer loop if a is found
                else:
                    continue
                break

            for i, c in enumerate(reversed(line)):
                if c.isdigit():
                    b = int(c)
                    break
                for n in NUMBERS:
                    if line[-(i + 1):].startswith(n):
                        b = (NUMBERS.index(n) + 1)
                        break
                # break outer loop if b is found
                else:
                    continue
                break

            s += a + b
    return s


assert task1('test_input.txt') == 142
print(task1('input.txt'))

assert task2('test_input_2.txt') == 281
print(task2('input.txt'))
