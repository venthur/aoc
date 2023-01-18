def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    parts = [[int(n) for n in line.split('/')] for line in lines]

    def xx(bridge, parts):
        p = bridge[-1]
        potentials = []
        for part in parts:
            if p in part:
                if p == part[0]:
                    potentials.append(part)
                else:
                    potentials.append(part[::-1])

        if not potentials:
            return sum(bridge)

        bridges = []
        for p in potentials:
            parts2 = parts[:]
            if p in parts2:
                parts2.remove(p)
            else:
                parts2.remove(p[::-1])
            bridges.append(xx(bridge + p, parts2))
        return max(bridges)

    return xx([0], parts)


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    parts = [[int(n) for n in line.split('/')] for line in lines]

    def xx(bridge, parts):
        p = bridge[-1]
        potentials = []
        for part in parts:
            if p in part:
                if p == part[0]:
                    potentials.append(part)
                else:
                    potentials.append(part[::-1])

        if not potentials:
            return len(bridge), sum(bridge)

        bridges = []
        for p in potentials:
            parts2 = parts[:]
            if p in parts2:
                parts2.remove(p)
            else:
                parts2.remove(p[::-1])
            bridges.append(xx(bridge + p, parts2))
        return sorted(bridges)[-1]

    return xx([0], parts)[-1]


assert task1('test_input.txt') == 31
print(task1('input.txt'))

assert task2('test_input.txt') == 19
print(task2('input.txt'))
