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


def task1(input_):
    wires = {}

    for line in input_:
        left, out = line.split(' -> ')
        if len(left.split()) == 1:
            try:
                value = int(left)
                wires[out] = value
            except ValueError:
                wires[out] = wires.get(left, 0)
        elif 'NOT' in left:
            in_ = left.split()[-1]
            wires[out] = ~wires.get(in_, 0)
        else:
            in1, op, in2 = left.split()
            if op == 'AND':
                wires[out] = wires.get(in1, 0) & wires.get(in2, 0)
            elif op == 'OR':
                wires[out] = wires.get(in1, 0) | wires.get(in2, 0)
            elif op == 'LSHIFT':
                wires[out] = wires.get(in1, 0) << int(in2)
            elif op == 'RSHIFT':
                wires[out] = wires.get(in1, 0) >> int(in2)
            else:
                print(op)
        wires[out] &= 0xffff
    return wires


assert task1(test_input) == dict(
    d=72, e=507, f=492, g=114, h=65412, i=65079, x=123, y=456
)
print(task1(input_)['a'])
