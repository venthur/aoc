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

    result = 0
    for buttons, joltages in schematics:

        # reorder buttons
        buttons = sorted(buttons, key=sum)

        current_best = None
        todo = [(0, joltages[:])]
        while todo:
            # print(current_best, len(todo))
            # print(todo)
            presses, joltages = todo.pop()

            if all(j == 0 for j in joltages):
                if current_best is None or presses < current_best:
                    current_best = presses
                    todo = [
                        (pt, jt) for pt, jt in todo 
                        if pt + max(jt) < current_best
                    ]
                    print(f' {presses}')
                    continue

            for b in buttons:
                joltages2 = joltages[:]
                i = 0
                while True:
                    joltages2 = [x - y for x, y in zip(joltages2, b)]
                    i += 1
                    # too far?
                    if any(v < 0 for v in joltages2):
                        break
                    # too many presses required?
                    if (
                        current_best and
                        i + presses + max(joltages2) >= current_best
                    ):
                        break
                    todo.append((presses+i, joltages2))

        print(current_best)
        result += current_best

    return result

assert task1('test_input.txt') == 7
print(task1('input.txt'))

assert task2('test_input.txt') == 33
print(task2('input.txt'))
