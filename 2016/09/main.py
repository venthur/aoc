import re


def decompress(s):
    result = ''
    while m := re.search(r'\(\d+x\d+\)', s):
        result += s[:m.start()]
        s = s[m.start() + len(m.group()):]
        nchars, rep = [int(i) for i in m.group()[1:-1].split('x')]
        chars = s[:nchars]
        s = s[nchars:]
        result += chars*rep
    if s:
        result += s
    return result


def task1(fn):
    with open(fn) as fh:
        data = fh.read()

    data = decompress(data)
    data = data.strip()
    return len(data)


from functools import cache
@cache
def decompress2(s):
    pattern = re.compile(r'\(\d+x\d+\)')
    result = 0
    i = 0
    while m := pattern.search(s):
        i += 1
        if i >= 10000:
            print(len(s))
            i = 0
        result += len(s[:m.start()])
        s = s[m.start() + len(m.group()):]
        nchars, rep = [int(i) for i in m.group()[1:-1].split('x')]
        chars = s[:nchars]
        s = s[nchars:]
        s = chars*rep + s
    if s:
        result += len(s)
    return result


def task2(fn):
    with open(fn) as fh:
        data = fh.read()

    return decompress2(data) - 1


assert decompress('ADVENT') == 'ADVENT'
assert decompress('A(1x5)BC') == 'ABBBBBC'
assert decompress('(3x3)XYZ') == 'XYZXYZXYZ'
assert decompress('A(2x2)BCD(2x2)EFG') == 'ABCBCDEFEFG'
assert decompress('(6x1)(1x3)A') == '(1x3)A'
assert decompress('X(8x2)(3x3)ABCY') == 'X(3x3)ABC(3x3)ABCY'

print(task1('input.txt'))


assert decompress2('(3x3)XYZ') == len('XYZXYZXYZ')
assert decompress2('X(8x2)(3x3)ABCY') == len('XABCABCABCABCABCABCY')
assert decompress2('(27x12)(20x12)(13x14)(7x10)(1x12)A') == len('A' * 241920)
assert decompress2('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN') == 445

print(task2('input.txt'))
