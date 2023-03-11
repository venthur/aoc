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
    todo = [x, y, 0]
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

    agents = [(x, y, j) for ((x, y), j) in state.items() if j in 'ABCD']
    for x, y, j in agents:
        if y == HALLWAY:
            if clear[j]:
                # go to target
                possible, state2, cost = go_home(state, x, y, target[j])
                if possible:
                    yield state2, cost
            else:
                # can't go to target
                continue
        if y != HALLWAY:
            if clear[j] and x == target[j]:
                # home!
                continue
            elif x != target[j]:
                # move out
                for state2, cost in generate_hallway_moves(state, x, y):
                    yield state2, cost
    


def task1(fn):
    state = parse(fn)
    pp(state)
    is_final(state)

    todo = [(0, state.copy())]
    visited = set()
    while todo:

        todo.sort()
        cost, state = todo.pop(0)
        visited.add(tuple(state.items()))

        if is_final(state):
            return cost

        # explode
        for cost2, state2 in generate_states(state):

            if tuple(state2.items()) in visited:
                continue

            for i, (cost_old, state_old) in enumerate(todo):
                if state_old == state2 and cost_old < cost + cost2:
                    break
                elif state_old == state2 and cost_old > cost + cost2:
                    todo[i] = (cost + cost2, state_old)
                    break
            else:
                todo.append((cost + cost2, state2))


assert task1('test_input0.txt') == 12521
print(task1('input.txt'))
