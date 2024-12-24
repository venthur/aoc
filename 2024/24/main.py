from itertools import count


def get_input(fn):
    with open(fn) as fh:
        w, g = fh.read().split('\n\n')

    values = {}
    for line in w.splitlines():
        name, value = line.split(': ')
        value = int(value)
        values[name] = value

    gates = {}
    for line in g.splitlines():
        gate, out = line.split(' -> ')
        gates[out] = gate

    return gates, values


def compute(out, gates, values):

    if out in values:
        return values[out]

    gate = gates[out]
    o1, op, o2 = gate.split()

    if op == 'XOR':
        return compute(o1, gates, values) ^ compute(o2, gates, values)
    elif op == 'OR':
        return compute(o1, gates, values) | compute(o2, gates, values)
    elif op == 'AND':
        return compute(o1, gates, values) & compute(o2, gates, values)
    else:
        raise ValueError(f'Unknown operator {op}')


def task1(fn):
    gates, values = get_input(fn)
    v = 0
    for i in count():
        z = f'z{i:02}'
        if z not in gates and z not in values:
            break
        v2 = compute(z, gates, values)
        v2 <<= i
        v += v2
    return v


def task2(fn):
    gates, _ = get_input(fn)

    highest_z = "z00"
    for res in gates.keys():
        if res[0] == 'z' and int(res[1:]) > int(highest_z[1:]):
            highest_z = res

    wrong = set()
    for res, gate in gates.items():
        op1, op, op2 = gate.split()
        if res[0] == 'z' and op != 'XOR' and res != highest_z:
            wrong.add(res)
        if (
            op == 'XOR' and
            res[0] not in 'xyz' and
            op1[0] not in 'xyz' and
            op2[0] not in 'xyz'
        ):
            wrong.add(res)
        if op == 'AND' and 'x00' not in (op1, op2):
            for rubres, subgate in gates.items():
                subop1, subop, subop2 = subgate.split()
                if (res == subop1 or res == subop2) and subop != 'OR':
                    wrong.add(res)
        if op == 'XOR':
            for rubres, subgate in gates.items():
                subop1, subop, subop2 = subgate.split()
                if (res == subop1 or res == subop2) and subop == 'OR':
                    wrong.add(res)

    return ",".join(sorted(wrong))


assert task1('test_input.txt') == 2024
print(task1('input.txt'))

print(task2('input.txt'))
