from itertools import combinations
from functools import cache

def task1(fn):
    schematics = []
    with open(fn) as fh:
        for line in fh:
            line = line.strip()

            data, rest = line.split(']')
            data = data[1:]
            lights = [True if i == '#' else False for i in data]

            data1, data2 = rest.split('{')
            data1 = data1.strip()
            buttons = []
            for d in data1.split():
                d = d[1:-1]
                button = [int(i) for i in d.split(',')]
                buttons.append(button)

            data = data2[:-1]
            joltages = [int(i) for i in data.split(',')]

            schematics.append([lights, buttons, joltages])

    result = 0
    for lights, buttons, joltages in schematics:
        seen = set()
        queue = []
        l = [False for i in range(len(lights))]
        queue.append([0, l])
        seen.add(tuple(l))

        while queue:
            presses, l = queue.pop(0)
            if l == lights:
                result += presses
                break
            for button in buttons:
                lnew = l[:]
                for bi in button:
                    lnew[bi] = not lnew[bi]
                if tuple(lnew) not in seen:
                    queue.append([presses+1, lnew])
                    seen.add(tuple(lnew))
        else:
            raise ValueError('Empty Queue')

    return result


def task2(fn):
    schematics = []
    with open(fn) as fh:
        for line in fh:
            line = line.strip()

            data, rest = line.split(']')
            data = data[1:]
            lights = [True if i == '#' else False for i in data]

            data1, data2 = rest.split('{')
            data1 = data1.strip()
            buttons = []
            for d in data1.split():
                d = d[1:-1]
                button = [int(i) for i in d.split(',')]
                buttons.append(button)

            data = data2[:-1]
            joltages = [int(i) for i in data.split(',')]

            buttons = [
                [1 if i in b else 0 for i in range(len(joltages))]
                for b
                in buttons
            ]
            schematics.append([buttons, joltages])

    def patterns(buttons):
        out = {}
        out[tuple(0 for _ in range(len(buttons[0])))] = 0
        for pattern_len in range(1, len(buttons)+1):
            for button_combo in combinations(buttons, pattern_len):
                pattern = tuple(map(sum, zip(*button_combo)))
                if pattern not in out:
                    out[pattern] = pattern_len

        return out

    def solve(buttons, joltage):

        pattern_costs = patterns(buttons)

        @cache
        def solve_r(joltage):
            if all(i == 0 for i in joltage):
                return 0
            res = 100000000
            for pattern, cost in pattern_costs.items():
                if all(i <= j and i % 2 == j % 2 for i, j in zip(pattern, joltage)):
                    joltage2 = tuple((j - i)//2 for i, j in zip(pattern, joltage))
                    res = min(res, cost + 2 * solve_r(joltage2))
            return res

        return solve_r(joltage)

    result = 0
    for buttons, joltages in schematics:
        res = solve(buttons, tuple(joltages))
        result += res

    return result

assert task1('test_input.txt') == 7
print(task1('input.txt'))

assert task2('test_input.txt') == 33
print(task2('input.txt'))
