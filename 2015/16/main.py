def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    sues = []
    for line in lines:
        name, rest = line.split(': ', 1)
        name = int(name.split()[-1])

        sue = dict(sue=name)
        rest = rest.split(', ')
        for item in rest:
            thing, nr = item.split(': ')
            sue[thing] = int(nr)
        sues.append(sue)

    ticker = dict(
        children=3,
        cats=7,
        samoyeds=2,
        pomeranians=3,
        akitas=0,
        vizslas=0,
        goldfish=5,
        trees=3,
        cars=2,
        perfumes=1,
    )

    for item, nr in ticker.items():
        sues = list(filter(lambda x: x.get(item, None) in (None, nr), sues))

    return sues[0]['sue']


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    sues = []
    for line in lines:
        name, rest = line.split(': ', 1)
        name = int(name.split()[-1])

        sue = dict(sue=name)
        rest = rest.split(', ')
        for item in rest:
            thing, nr = item.split(': ')
            sue[thing] = int(nr)
        sues.append(sue)

    ticker = dict(
        children=3,
        cats=7,
        samoyeds=2,
        pomeranians=3,
        akitas=0,
        vizslas=0,
        goldfish=5,
        trees=3,
        cars=2,
        perfumes=1,
    )

    for item, nr in ticker.items():
        if item in ('cats', 'trees'):
            sues = list(filter(lambda x: x.get(item, None) is None or x[item] > nr, sues))
        elif item in ('pomeranians', 'goldfish'):
            sues = list(filter(lambda x: x.get(item, None) is None or x[item] < nr, sues))
        else:
            sues = list(filter(lambda x: x.get(item, None) in (None, nr), sues))

    return sues[0]['sue']


print(task1('input.txt'))
print(task2('input.txt'))
