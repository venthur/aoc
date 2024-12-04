def findall_horizontal(strings, sub):
    found = 0
    for string in strings:
        start = 0
        while True:
            start = string.find(sub, start)
            if start == -1:
                break
            found += 1
            start += 1
    return found


def findall_diagonal(strings, sub):
    found = 0
    for y in range(len(strings)):
        for x in range(len(strings[y])):
            for i, char in enumerate(sub):
                try:
                    if strings[y+i][x+i] != char:
                        break
                except IndexError:
                    break
            else:
                found += 1
    return found


def transpose(strings):
    zipd = zip(*strings)
    return [''.join(row) for row in zipd][::-1]


def task1(fn):
    with open(fn) as fh:
        data = fh.read().splitlines()

    found = 0
    for i in range(4):
        data = transpose(data)
        found += findall_horizontal(data, 'XMAS')
        found += findall_diagonal(data, 'XMAS')

    return found


def task2(fn):
    with open(fn) as fh:
        strings = fh.read().splitlines()

    found = 0
    for y in range(1, len(strings)-1):
        for x in range(1, len(strings[y])-1):
            if (
                strings[y][x] == 'A' and
                (strings[y-1][x-1] == 'M' and strings[y+1][x+1] == 'S' or
                    strings[y-1][x-1] == 'S' and strings[y+1][x+1] == 'M') and
                (strings[y-1][x+1] == 'M' and strings[y+1][x-1] == 'S' or
                    strings[y-1][x+1] == 'S' and strings[y+1][x-1] == 'M')
               ):
                found += 1
    return found


assert task1('test_input.txt') == 18
print(task1('input.txt'))

assert task2('test_input.txt') == 9
print(task2('input.txt'))
