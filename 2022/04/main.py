example = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".splitlines()

with open('input.txt') as fh:
    input_ = fh.read().splitlines()


def get_ids(input_):
    start, stop = [int(i) for i in input_.split('-')]
    return set(list(range(start, stop+1)))


def task1(input_):
    count = 0
    for line in input_:
        e1, e2 = [get_ids(i) for i in line.split(',')]
        if e1 <= e2 or e2 <= e1:
            count += 1
    print(count)


def task2(input_):
    count = 0
    for line in input_:
        e1, e2 = [get_ids(i) for i in line.split(',')]
        if not e1.isdisjoint(e2):
            count += 1
    print(count)


task1(example) # 2
task1(input_)


task2(example) # 4
task2(input_)
