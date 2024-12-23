from itertools import permutations


NUMPAD = """
789
456
123
 0A
"""

numpad = {}
for row, line in enumerate(NUMPAD.split('\n')):
    for col, char in enumerate(line.strip()):
        if char != ' ':
            numpad[col, row] = char

DIRPAD = """
 ^A
<v>
"""

dirpad = {}
for row, line in enumerate(DIRPAD.split('\n')):
    for col, char in enumerate(line.strip()):
        if char != ' ':
            dirpad[col, row] = char


def read_input(fn):
    data = []
    with open(fn) as fh:
        data = fh.read().split()
    return data


for ((xs, ys), vs), ((xe, ye), ve) in permutations(numpad.items(), 2):
    print(vs, ve)

def task1(fn):
    data = read_input(fn)
    print(data)


assert task1('test_input.txt') == 126384
print(task1('input.txt'))
