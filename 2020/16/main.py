def task1(fn):
    with open(fn) as fh:
        rules, ours, others = fh.read().split('\n\n')

    valid = set()
    for rule in rules.splitlines():
        r = ''.join([c if c.isnumeric() else ' ' for c in rule])
        r = [int(n) for n in r.split()]
        for i in range(r[0], r[1]+1):
            valid.add(i)
        for i in range(r[2], r[3]+1):
            valid.add(i)

    others = others.splitlines()[1:]
    error_rate = 0
    for line in others:
        for n in line.split(','):
            if int(n) not in valid:
                error_rate += int(n)

    return error_rate


print(task1('input.txt'))
