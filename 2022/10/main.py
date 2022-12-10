test_input = '''\
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
'''.splitlines()


with open('input.txt') as fh:
    input_ = fh.read().splitlines()


def task1(input_):
    x = [1]
    for line in input_:
        if line == 'noop':
            x.append(x[-1])
        else:
            _, value = line.split()
            value = int(value)
            for i in range(1):
                x.append(x[-1])
            x.append(x[-1] + value)

    strength = 0
    for i in 20, 60, 100, 140, 180, 220:
        strength += i * x[i-1]
    return strength


def task2(input_):
    x = [1]
    for line in input_:
        if line == 'noop':
            x.append(x[-1])
        else:
            _, value = line.split()
            value = int(value)
            for i in range(1):
                x.append(x[-1])
            x.append(x[-1] + value)

    screen = ""
    for cycle in range(40*6):
        if cycle % 40 == 0:
            screen += '\n'
        pos = cycle % 40
        if x[cycle] in [pos, pos-1, pos+1]:
            screen += '#'
        else:
            screen += '.'
    print(screen)


assert (task1(test_input)) == 13140
print(task1(input_))

task2(test_input)
task2(input_)  # EGJBGCFK
