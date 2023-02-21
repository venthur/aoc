def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    valid = 0
    for line in lines:
        rule, pw = line.split(': ')

        numbers, letter = rule.split()
        lower, upper = [int(n) for n in numbers.split('-')]
        if lower <= pw.count(letter) <= upper:
            valid += 1

    return valid


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    valid = 0
    for line in lines:
        rule, pw = line.split(': ')

        numbers, letter = rule.split()
        p1, p2 = [int(n) for n in numbers.split('-')]
        if (pw[p1-1] == letter or pw[p2-1] == letter) and pw[p1-1] != pw[p2-1]:
            valid += 1

    return valid


print(task1('input.txt'))
print(task2('input.txt'))
