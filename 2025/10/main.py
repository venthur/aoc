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

        min_presses = None
        for button in buttons:
            mx = min([joltages[i] for i in button])

            mn = 0
            for bi in button:
                # find remaining buttons with that wiring
                found = False
                for button2 in buttons[::-1]:
                    if button == button2:
                        break
                    if bi in button2:
                        found = True
                        break
                # minimal button presses for this one
                if not found:
                    mn = max(mn, joltages[bi])

            if buttonpresses + mn >= current_best:
                return current_best



            for i in range(mx, mn-1, -1):
                if i == 0:
                    break
                joltages2 = joltages[:]
                for bi in button:
                    joltages2[bi] -= i
                p = calculate_button_presses(buttonpresses+i, joltages2)

                if (
                    p and min_presses is None or
                    p and p < min_presses
                ):
                    min_presses = p

        return min_presses

    def reorder_buttons(buttons, joltages):
        todo = buttons[:]
        res = []
        while todo:
            cnt = [0] * len(joltages)
            for button in todo:
                for id in button:
                    cnt[id] += 1
            mn = min(x for x in cnt if x > 0)
            id = cnt.index(mn)
            next_button = None
            for button in todo:
                if id in button:
                    if next_button is None or len(button) > len(next_button):
                        next_button = button
            res.append(next_button)
            todo.remove(next_button)
        return res


    result = 0
    for lights, buttons, joltages in schematics:
        global current_best
        current_best = sum(joltages)
        # buttons = sorted(
        #     buttons,
        #     key=lambda idx: [joltages[i] for i in idx],
        #     reverse=True
        # )
        # buttons = sorted(buttons, key=len, reverse=True)
        buttons = reorder_buttons(buttons, joltages)
        result += calculate_button_presses(0, joltages)
        print('.')
    print()
    return result

assert task1('test_input.txt') == 7
print(task1('input.txt'))

assert task2('test_input.txt') == 33
print(task2('input.txt'))
