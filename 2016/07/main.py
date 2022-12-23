def read(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    result = []
    for line in lines:
        ins, outs = [], []
        current = 'out'
        buffer = []
        for char in line:
            if char == '[':
                assert current == 'out'
                outs.append(''.join(buffer))
                buffer = []
                current = 'in'
            elif char == ']':
                assert current == 'in'
                ins.append(''.join(buffer))
                buffer = []
                current = 'out'
            else:
                buffer.append(char)
        if current == 'in':
            ins.append(''.join(buffer))
        elif current == 'out':
            outs.append(''.join(buffer))
        result.append([outs, ins])
    return result


def has_abba(s):
    for i, a in enumerate(s[:-3]):
        b, c, d = s[i+1:i+4]
        if a == b:
            continue
        if a == d and b == c:
            return True
    return False


def task1(fn):
    lines = read(fn)
    count = 0
    for outs, ins in lines:
        outs = list(filter(lambda x: has_abba(x), outs))
        ins = list(filter(lambda x: has_abba(x), ins))
        if len(outs) >= 1 and len(ins) == 0:
            count += 1
    return count


def get_aba(s):
    for i, a in enumerate(s[:-2]):
        b, c = s[i+1:i+3]
        if a == c and a != b:
            yield ''.join([a, b, c])


def task2(fn):
    lines = read(fn)
    count = 0
    for outs, ins in lines:
        abas = []
        babs = []
        for o in outs:
            aba = [aba for aba in get_aba(o)]
            abas.extend(aba)
        for i in ins:
            bab = [bab for bab in get_aba(i)]
            babs.extend(bab)
        for a in abas:
            a2 = ''.join([a[1], a[0], a[1]])
            if a2 in babs:
                count += 1
                break
    return count


assert task1('test_input.txt') == 2
print(task1('input.txt'))

assert task2('test_input2.txt') == 3
print(task2('input.txt'))
