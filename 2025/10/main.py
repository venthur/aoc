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


from time import time

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

    # biggest first
    # schematics.sort(key=lambda x: sum(x[1]), reverse=True)
    # smallest first
    schematics.sort(key=lambda x: sum(x[1]))

    result = 0
    for buttons, joltages in schematics:

        # reorder buttons by rarity wirings, and number of wirings
        todo = buttons[:]
        res = []
        while todo:
            cnt = [0] * len(joltages)
            for button in todo:
                for id, v in enumerate(button):
                    if v == 1:
                        cnt[id] += 1
            mn = min(x for x in cnt if x > 0)
            id = cnt.index(mn)
            next_button = None
            for button in todo:
                if button[id] == 1:
                    if next_button is None or sum(button) > sum(next_button):
                        next_button = button
            res.append(next_button)
            todo.remove(next_button)
        buttons = res[::-1]

        t0 = time()
        current_best = None
        todo = [(0, joltages[:], [])]
        while todo:
            # print(current_best, len(todo))
            # print(todo)
            presses, joltages, used = todo.pop()

            if all(j == 0 for j in joltages):
                if current_best is None or presses < current_best:
                    current_best = presses
                    todo = [
                        (pt, jt, ut) for pt, jt, ut in todo
                        if pt + max(jt) < current_best
                    ]
                    print(f' {presses}')
                    continue

            for bi, b in enumerate(buttons):
                if bi in used:
                    continue
                mx = min(joltages[bi] for bi, bv in enumerate(b) if bv == 1)
                joltages2 = joltages[:]
                used2 = used + [bi]
                buttons2 = [buttons[i] for i in range(len(buttons)) if i not in used2]
                still_pressable = [1 in x for x in zip(*buttons2)]

                for i in range(1, mx+1):
                    joltages2 = [x - y for x, y in zip(joltages2, b)]
                    if (
                        current_best and
                        i + presses + max(joltages2) >= current_best
                    ):
                        break
                    # impossible to solve?
                    if not all(c > 0 and p or c == 0 for p, c in zip(still_pressable, joltages2)):
                        continue
                    todo.append((presses+i, joltages2, used2))

        print(f'{current_best} {time()-t0:.1f}s')
        result += current_best

    return result

assert task1('test_input.txt') == 7
print(task1('input.txt'))

assert task2('test_input.txt') == 33
print()
print(task2('input.txt'))
