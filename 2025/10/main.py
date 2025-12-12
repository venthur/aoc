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

    result = 0
    for buttons, joltages in schematics:

        # reorder buttons
        #buttons = sorted(buttons, key=sum)

        # reorder buttons by wirings
        x = [[] for _ in range(len(joltages))]
        for ji in range(len(joltages)):
            for bi, b in enumerate(buttons):
                if b[ji] == 1:
                    x[ji].append((bi, sum(b)))

        for xi, xx in enumerate(x):
            x[xi] = sorted(xx, key=lambda v: -v[-1])
        x.sort(key=len)
        buttons2 = []
        for l in x:
            for bi, _ in l:
                if buttons[bi] not in buttons2:
                    buttons2.append(buttons[bi])
        buttons = buttons2[::-1]

        # # last wirings per button
        # last = [[] for i in range(len(buttons))]
        # for bi, b in enumerate(buttons):
        #     for bvi, bb in enumerate(b):
        #         if bb == 0:
        #             continue
        #         for bii in range(bi+1, len(buttons)):
        #             if buttons[bii][bvi] == 1:
        #                 break
        #         else:
        #             last[bi].append(bvi)

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
                # mx = min(joltages[bi] for bi, bv in enumerate(b) if bv == 1)
                # lastj = [joltages[i] for i in last[bi]]
                # if lastj:
                #     mn = max(joltages[i] for i in last[bi])
                # else:
                #     mn = 1
                # if mn > mx:
                #     break
                joltages2 = joltages[:]
                i = 0
                while True:
                # if mn == 0:
                #     mn += 1
                # for i in range(1, mx+1):
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
                    todo.append((presses+i, joltages2, used + [bi]))

        print(f'{current_best} {time()-t0:.1f}s')
        result += current_best

    return result

assert task1('test_input.txt') == 7
print(task1('input.txt'))

assert task2('test_input.txt') == 33
print()
print(task2('input.txt'))
