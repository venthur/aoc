import re


def read(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    data = []
    for line in lines:
        name, id_, checksum = re.match(
            r'^([a-z\-]+)-(\d+)\[([a-z]+)\]$',
            line
        ).groups()
        data.append([name, int(id_), checksum])

    return data


def task1(fn):
    rooms = read(fn)

    sum_ = 0
    for n, i, cs in rooms:
        counter = dict()
        for char in n:
            if char == '-':
                continue
            counter[char] = counter.get(char, 0) + 1
        counter = list(counter.items())
        # python's sort is stable, so we wort first for alphabetical order then
        # we sort for counts, preserving the alphabetical order for same counts
        counter.sort()
        counter.sort(key=lambda x: x[1], reverse=True)
        counter = counter[:5]
        if ''.join([i for i, _ in counter]) == cs:
            sum_ += i

    return sum_


def task2(fn):
    rooms = read(fn)

    real_rooms = []
    for n, i, cs in rooms:
        counter = dict()
        for char in n:
            if char == '-':
                continue
            counter[char] = counter.get(char, 0) + 1
        counter = list(counter.items())
        # python's sort is stable, so we wort first for alphabetical order then
        # we sort for counts, preserving the alphabetical order for same counts
        counter.sort()
        counter.sort(key=lambda x: x[1], reverse=True)
        counter = counter[:5]
        if ''.join([i for i, _ in counter]) == cs:
            real_rooms.append([n, i, cs])

    def rotate(x, n):
        if x == '-':
            return ' '
        n %= 26
        x2 = ord(x) + n
        if x2 > ord('z'):
            x2 -= 26
        return chr(x2)

    for n, i, cs in real_rooms:
        n2 = ''.join(map(lambda x: rotate(x, i), n))
        if n2 == 'northpole object storage':
            return i


assert task1('test_input.txt') == 123 + 987 + 404
print(task1('input.txt'))

print(task2('input.txt'))
