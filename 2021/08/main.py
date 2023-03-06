from itertools import permutations


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    counter = 0
    for line in lines:
        outputs = line.split('|')[-1]
        for o in outputs.split():
            if len(o) in (2, 4, 3, 7):
                counter += 1

    return counter


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    displays = {
        0: 'abc efg',
        1: '  c  f ',
        2: 'a cde g',
        3: 'a cd fg',
        4: ' bcd f ',
        5: 'ab d fg',
        6: 'ab defg',
        7: 'a c  f ',
        8: 'abcdefg',
        9: 'abcd fg',
    }

    sum_ = 0
    for line in lines:
        inputs, outputs = line.split('|')
        inputs = [sorted(i) for i in inputs.split()]
        outputs = [sorted(o) for o in outputs.split()]

        for letters in permutations('abcdefg'):
            d2 = dict()
            for n, wires in displays.items():
                s = []
                for i, w in enumerate(wires):
                    if w == ' ':
                        continue
                    s.append(letters[i])
                s.sort()
                if s not in inputs:
                    break
                d2[n] = s
            else:
                m = 0
                for o in outputs:
                    for n, wires in d2.items():
                        if wires == o:
                            m *= 10
                            m += n
                            break
                sum_ += m
                break

    return sum_


print(task1('input.txt'))
print(task2('input.txt'))
