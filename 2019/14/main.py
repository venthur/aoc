from itertools import count
from collections import defaultdict
from math import ceil


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    rules = []
    for line in lines:
        inputs, output = line.split(' => ')
        output = int(output.split()[0]), output.split()[1]

        inputs = [(int(in_.split()[0]), in_.split()[1]) for in_ in inputs.split(', ')]
        inputs = tuple(inputs)

        rules.append(output + inputs)

    orders = [(1, "FUEL")]
    leftovers = defaultdict(int)
    ore = 0
    while orders:
        amount, what = orders.pop(0)
        if what == 'ORE':
            ore += amount
        elif amount <= leftovers[what]:
            leftovers[what] -= amount
        else:
            amount -= leftovers[what]
            leftovers[what] = 0
            for q, w, *inputs in rules:
                if w == what:
                    batches = ceil(amount / q)
                    for qi, wi in inputs:
                        orders.append((batches*qi, wi))
                    leftovers[what] += batches*q - amount
                    break
    return ore


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    rules = []
    for line in lines:
        inputs, output = line.split(' => ')
        output = int(output.split()[0]), output.split()[1]

        inputs = [(int(in_.split()[0]), in_.split()[1]) for in_ in inputs.split(', ')]
        inputs = tuple(inputs)

        rules.append(output + inputs)

    min = 0
    max = 100000000
    while max-min > 1:
        i = min + (max-min) // 2
        orders = [(i, "FUEL")]
        leftovers = defaultdict(int)
        ore = 0
        while orders:
            amount, what = orders.pop(0)
            if what == 'ORE':
                ore += amount
            elif amount <= leftovers[what]:
                leftovers[what] -= amount
            else:
                amount -= leftovers[what]
                leftovers[what] = 0
                for q, w, *inputs in rules:
                    if w == what:
                        batches = ceil(amount / q)
                        for qi, wi in inputs:
                            orders.append((batches*qi, wi))
                        leftovers[what] += batches*q - amount
                        break
        if ore > 1000000000000:
            max = i
        elif ore < 1000000000000:
            min = i
    return i


assert task1('test_input0.txt') == 31
print(task1('input.txt'))


print(task2('input.txt'))
