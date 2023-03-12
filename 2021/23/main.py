def parse(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    state = dict()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char in '#.ABCD':
                state[x, y] = char

    return state


def pp(state):
    xs, ys = zip(*state)
    s = ''
    for y in range(min(ys), max(ys)+1):
        for x in range(min(xs), max(xs)+1):
            s += state.get((x, y), ' ')
        s += '\n'
    print(s)


def is_final(state):
    f = [(x, j) for ((x, y), j) in state.items() if j in 'ABCD']
    xs = []
    for i in 'ABCD':
        xi = [x for (x, j) in f if j == i]
        if len(set(xi)) > 1:
            return False
        xs.append(xi[0])

    if not sorted(xs) == xs:
        return False

    return True


def bfs(state, x, y):
    """Returns a list of all possible moves from x, y.

    """
    moves = []
    todo = [(x, y, 0)]
    visited = {x, y}
    while todo:
        x, y, steps = todo.pop(0)
        moves.append((x, y, steps))

        for xi, yi in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if state.get((xi, yi), '#') == '.' and (xi, yi) not in visited:
                todo.append((xi, yi, steps+1))
                visited.add((xi, yi))

    return moves


def generate_states(state):
    # hard coded target cols
    target = dict(A=3, B=5, C=7, D=9)

    # hard coded hallway row
    HALLWAY = 1

    costs = dict(A=1, B=10, C=100, D=1000)

    clear = dict()
    for i in 'ABCD':
        clear[i] = True
        for ((x, _), j) in state.items():
            if x == target[i] and j in 'ABCD' and j != i:
                clear[i] = False
                break

    # heuristics(state)
    def h(state):
        out = sum(
            [
                (1+abs(x-target[j])) * costs[j]
                for ((x, y), j) in state.items()
                if j in 'ABCD' and y == HALLWAY
            ]
        )
        wrong = sum(
            [
                (1+abs(x-target[j])) * costs[j] + (y - HALLWAY) * costs[j]
                for ((x, y), j) in state.items()
                if j in 'ABCD' and x != target[j] and y != HALLWAY
            ]
        )

        return out + wrong

    agents = [(x, y, j) for ((x, y), j) in state.items() if j in 'ABCD']
    for x, y, j in agents:
        if y == HALLWAY:
            if clear[j]:
                # go to target
                moves = bfs(state, x, y)
                moves = [m for m in moves if m[0] == target[j] and m[1] != HALLWAY]
                if len(moves) > 1:
                    moves.sort(key=lambda x: x[1])
                    moves = [moves[-1]]
                for xi, yi, steps in moves:
                    state2 = state.copy()
                    state2[x, y] = '.'
                    state2[xi, yi] = j
                    yield state2, steps * costs[j], h(state2)
            else:
                # can't go to target
                continue
        if y != HALLWAY:
            if clear[j] and x == target[j]:
                # home!
                continue
            else:
                # move out
                moves = bfs(state, x, y)
                moves = [m for m in moves if m[1] == HALLWAY and m[0] not in target.values()]
                for xi, yi, steps in moves:
                    state2 = state.copy()
                    state2[x, y] = '.'
                    state2[xi, yi] = j
                    yield state2, steps * costs[j], h(state2)


def task1(fn):
    state = parse(fn)

    todo = [(0, 0, state.copy())]
    visited = set()
    while todo:

        todo.sort(key=lambda x: x[0])
        _, cost, state = todo.pop(0)
        visited.add(tuple(state.items()))
        #print(_, cost)
        #pp(state)

        if is_final(state):
            #print(f'Found result for {cost}')
            #pp(state)
            return cost

        # explode
        for state2, cost2, h in generate_states(state):

            if tuple(state2.items()) in visited:
                continue

            for i, (h_old, cost_old, state_old) in enumerate(todo):
                if state_old == state2 and h_old <= h + cost + cost2:
                    break
                elif state_old == state2 and h_old > h + cost + cost2:
                    todo[i] = (cost + cost2 + h, cost + cost2, state_old)
                    break
            else:
                todo.append((cost + cost2 + h, cost + cost2, state2))


assert task1('test_input0.txt') == 12521
print(task1('input.txt'))

assert task1('test_input2.txt') == 44169
print(task1('input2.txt'))
