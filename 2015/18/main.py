def task1(fn, dim, steps):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    state = dict()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                state[x, y] = 1
            else:
                state[x, y] = 0

    def run(state, dim):
        state2 = dict()
        for y in range(dim):
            for x in range(dim):
                n = (
                    state.get((x-1, y-1), 0)
                    + state.get((x, y-1), 0)
                    + state.get((x+1, y-1), 0)

                    + state.get((x-1, y), 0)
                    + state.get((x+1, y), 0)

                    + state.get((x-1, y+1), 0)
                    + state.get((x, y+1), 0)
                    + state.get((x+1, y+1), 0)
                )
                if state[x, y] == 1:
                    if n in (2, 3):
                        state2[x, y] = 1
                    else:
                        state2[x, y] = 0
                elif state[x, y] == 0:
                    if n == 3:
                        state2[x, y] = 1
                    else:
                        state2[x, y] = 0
        return state2

    for i in range(steps):
        state = run(state, dim)

    count = 0
    for i in state.values():
        if i:
            count += 1

    return count


def task2(fn, dim, steps):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    state = dict()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                state[x, y] = 1
            else:
                state[x, y] = 0
    state[0, dim-1] = state[0, 0] = state[dim-1, 0] = state[dim-1, dim-1] = 1

    def run(state, dim):
        state2 = dict()
        for y in range(dim):
            for x in range(dim):
                n = (
                    state.get((x-1, y-1), 0)
                    + state.get((x, y-1), 0)
                    + state.get((x+1, y-1), 0)

                    + state.get((x-1, y), 0)
                    + state.get((x+1, y), 0)

                    + state.get((x-1, y+1), 0)
                    + state.get((x, y+1), 0)
                    + state.get((x+1, y+1), 0)
                )
                if state[x, y] == 1:
                    if n in (2, 3):
                        state2[x, y] = 1
                    else:
                        state2[x, y] = 0
                elif state[x, y] == 0:
                    if n == 3:
                        state2[x, y] = 1
                    else:
                        state2[x, y] = 0
        state2[0, dim-1] = state2[0, 0] = state2[dim-1, 0] = state2[dim-1, dim-1] = 1
        return state2

    for i in range(steps):
        state = run(state, dim)

    count = 0
    for i in state.values():
        if i:
            count += 1

    return count


assert task1('test_input.txt', 6, 4) == 4
print(task1('input.txt', 100, 100))

assert task2('test_input.txt', 6, 5) == 17
print(task2('input.txt', 100, 100))

