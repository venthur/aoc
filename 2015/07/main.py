import functools

test_input = '''\
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
'''.splitlines()

with open('input.txt') as fh:
    input_ = fh.read().splitlines()


def task1(input_, wire):
    wires = {}

    for line in input_:
        in_, out = line.split(' -> ')
        wires[out] = in_

    @functools.cache
    def simulate(rule):
        if len(rule.split()) == 1:
            if rule.isdigit():
                out = int(rule)
            else:
                out = simulate(wires[rule])
        elif 'NOT' in rule:
            in_ = rule.split()[-1]
            in_ = wires[in_]
            out = ~simulate(in_)
        else:
            in1, op, in2 = rule.split()
            if op == 'AND':
                out = simulate(in1) & simulate(in2)
            elif op == 'OR':
                out = simulate(in1) | simulate(in2)
            elif op == 'LSHIFT':
                out = simulate(in1) << simulate(in2)
            elif op == 'RSHIFT':
                out = simulate(in1) >> simulate(in2)
        return out & 0xffff

    return simulate(wire)


def task2(input_):
    wires = {}

    for line in input_:
        in_, out = line.split(' -> ')
        wires[out] = in_

    wires['b'] = '3176'

    @functools.cache
    def simulate(rule):
        if len(rule.split()) == 1:
            if rule.isdigit():
                out = int(rule)
            else:
                out = simulate(wires[rule])
        elif 'NOT' in rule:
            in_ = rule.split()[-1]
            in_ = wires[in_]
            out = ~simulate(in_)
        else:
            in1, op, in2 = rule.split()
            if op == 'AND':
                out = simulate(in1) & simulate(in2)
            elif op == 'OR':
                out = simulate(in1) | simulate(in2)
            elif op == 'LSHIFT':
                out = simulate(in1) << simulate(in2)
            elif op == 'RSHIFT':
                out = simulate(in1) >> simulate(in2)
        return out & 0xffff

    return simulate('a')


for k, v in dict(
    d=72, e=507, f=492, g=114, h=65412, i=65079, x=123, y=456
).items():
    assert task1(test_input, k) == v
print(task1(input_, 'a'))

print(task2(input_))
