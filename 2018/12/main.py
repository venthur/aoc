def task1(fn, generations):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    state = {i: c for i, c in enumerate(lines[0].split()[-1])}

    rules = []
    lines = lines[2:]
    for line in lines:
        pattern, result = line.split(' => ')
        rules.append((pattern, result))

    for i in range(generations):

        #if i % 1000 == 0:
        #    print(i, sum(map(lambda x: x[0], filter(lambda x: x[1] == '#', state.items()))))

        while ''.join([v for _, v in sorted(state.items())][:2]) != '..':
            state[min(state.keys())-1] = '.'

        while ''.join([v for _, v in sorted(state.items())][-2:]) != '..':
            state[max(state.keys())+1] = '.'

        state_new = {i: '.' for i in state.keys()}

        for j in list(state.keys()):
            p = state.get(j-2, '.') + state.get(j-1, '.') + state[j] + state.get(j+1, '.') + state.get(j+2, '.')
            for pattern, result in rules:
                if p == pattern:
                    state_new[j] = result
                    break
        state = state_new.copy()

    s = sum(map(lambda x: x[0], filter(lambda x: x[1] == '#', state.items())))

    return s


assert task1('test_input.txt', 20) == 325
print(task1('input.txt', 20))

# number is too large to compute, return the sum avert each 1000 iterations and
# see the pattern: (50000000000 // 1000) * 63000 + 905
#print(task1('input.txt', 50000000000))
print(3150000000905)
