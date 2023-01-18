import re
from collections import defaultdict


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    state = lines.pop(0)[-2]
    nsteps = int(lines.pop(0).split()[-2])
    lines = '\n'.join(lines)
    g = re.findall(
        r'In state (\w):\n.*0:\n.*(\d).\n.*(left|right).\n.*(\w).\n.*1:\n.*(\d).\n.*(left|right).\n.*(\w).',
        lines,
        re.MULTILINE,
        )
    states = dict()
    for s, w0, m0, s0, w1, m1, s1 in g:
        states[s] = (w0, m0, s0, w1, m1, s1)

    tape = defaultdict(lambda: '0')
    cursor = 0
    for i in range(nsteps):
        w0, m0, s0, w1, m1, s1 = states[state]
        if tape[cursor] == '0':
            w, m, s = w0, m0, s0
        else:
            w, m, s = w1, m1, s1
        tape[cursor] = w
        cursor = cursor + 1 if m == 'right' else cursor - 1
        state = s

    return list(tape.values()).count('1')


assert task1('test_input.txt') == 3
print(task1('input.txt'))
