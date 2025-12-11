from collections import deque


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

INF = 2**32
current_best = INF


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

            schematics.append([lights, buttons, joltages])


    def calculate_button_presses(buttonpresses, joltages):

        global current_best

        if buttonpresses >= current_best:
            return None

        if max(joltages) + buttonpresses >= current_best:
            return None

        if all([i == 0 for i in joltages]):
            if buttonpresses < current_best:
                current_best = buttonpresses
            return buttonpresses

        if any([i < 0 for i in joltages]):
            return None

        min_presses = INF
        for button in buttons:
            minp = min([joltages[i] for i in button])
            for i in range(minp, 0, -1):
                joltages2 = joltages[:]
                for bi in button:
                    joltages2[bi] -= i
                p = calculate_button_presses(buttonpresses+i, joltages2)

                if p and p < min_presses:
                    min_presses = p

        return min_presses


    result = 0
    for lights, buttons, joltages in schematics:
        global current_best
        current_best = INF
        buttons = sorted(
            buttons,
            key=lambda idx: [joltages[i] for i in idx],
            reverse=True
        )
        buttons = sorted(buttons, key=len, reverse=True)
        result += calculate_button_presses(0, joltages)
        print('.', end='')
    print()
    return result

assert task1('test_input.txt') == 7
print(task1('input.txt'))

assert task2('test_input.txt') == 33
print(task2('input.txt'))
