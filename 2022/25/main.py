SNAFU = {
    '=': -2,
    '-': -1,
    '0': 0,
    '1': 1,
    '2': 2,
}

SNAFU_R = {
    5: '0',
    4: '-',
    3: '=',
    2: '2',
    1: '1',
    0: '0',
}


def snafu_to_decimal(s):
    return sum(SNAFU[i]*5**exp for exp, i in enumerate(s[::-1]))


def decimal_to_snafu(decimal):
    snafu = ''
    c = 0
    while decimal > 0:
        x = decimal % 5 + c
        snafu += SNAFU_R[x]
        c = 1 if x > 2 else 0
        decimal //= 5

    return snafu[::-1]


def task1(fn):
    with open(fn) as fh:
        snafu = fh.read().splitlines()

    numbers = [snafu_to_decimal(s) for s in snafu]
    return decimal_to_snafu(sum(numbers))


assert task1('test_input.txt') == '2=-1=0'
print(task1('input.txt'))
