test = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".splitlines()


with open('input.txt') as fh:
    input_ = fh.read().splitlines()


map = dict(
    list(zip('abcdefghijklmnopqrstuvwxyz', list(range(1, 27))))
    + list(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', list(range(27, 53))))
)
print(map)


def part1(input_):
    common = []
    for rucksack in input_:
        l = len(rucksack) // 2
        compartment1 = set(list(rucksack[:l]))
        compartment2 = set(list(rucksack[l:]))

        common.append(compartment1.intersection(compartment2).pop())

    prio = 0
    for c in common:
        prio += map[c]

    print(prio)


def part2(input_):
    sum = 0
    while input_:
        r1 = input_.pop(0)
        r2 = input_.pop(0)
        r3 = input_.pop(0)
        c = set(r1).intersection(set(r2)).intersection(set(r3))
        sum += map[c.pop()]
    print(sum)

#part1(test) # 157
part1(input_)

#part2(test) # 70
part2(input_)
