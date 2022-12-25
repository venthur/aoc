from itertools import combinations
import re
from copy import deepcopy


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    chip = re.compile(r'(\w+)-compatible microchip')
    generator = re.compile(r'(\w+) generator')
    floors = [[] for i in range(4)]
    for i, line in enumerate(lines):
        j = 0
        while m := chip.search(line[j:]):
            floors[i].append(m.group(1)[0] + 'C')
            j += m.end()
        j = 0
        while m := generator.search(line[j:]):
            floors[i].append(m.group(1)[0] + 'G')
            j += m.end()

    def is_valid(floors):
        for floor in floors:
            chips = []
            generators = []
            for item in floor:
                if item.endswith('C'):
                    chips.append(item[0])
                elif item.endswith('G'):
                    generators.append(item[0])
            for chip in chips:
                if chip not in generators and len(generators) > 0:
                    return False
        return True

    def encode_state(floors, elevator):
        s = str(elevator)
        for floor in floors:
            s += '|'
            floor.sort()
            s += '-'.join(floor)
        return s

    # state: valid config of floors, elevators, steps
    states = [[floors, 0, 0]]
    states_seen = set(encode_state(floors, 0))
    while True:
        floors, elevator, steps = states.pop(0)
        # if final state
        if floors[0] == floors[1] == floors[2] == []:
            return steps
        # generate new states: (1) for each item on the same floor, try to move
        # it up or do
        for item in floors[elevator]:
            # up
            if elevator < 3:
                floors2 = deepcopy(floors)
                floors2[elevator+1].append(item)
                floors2[elevator].remove(item)
                s = encode_state(floors2, elevator+1)
                if s not in states_seen and is_valid(floors2):
                    states.append([floors2, elevator+1, steps+1])
                    states_seen.add(s)
            # down
            if elevator > 0:
                floors2 = deepcopy(floors)
                floors2[elevator-1].append(item)
                floors2[elevator].remove(item)
                s = encode_state(floors2, elevator-1)
                if s not in states_seen and is_valid(floors2):
                    states.append([floors2, elevator-1, steps+1])
                    states_seen.add(s)
        # (2) try to move any two-combinations up or down:
        for item1, item2 in combinations(floors[elevator], 2):
            # up
            if elevator < 3:
                floors2 = deepcopy(floors)
                floors2[elevator+1].append(item1)
                floors2[elevator+1].append(item2)
                floors2[elevator].remove(item1)
                floors2[elevator].remove(item2)
                s = encode_state(floors2, elevator+1)
                if s not in states_seen and is_valid(floors2):
                    states.append([floors2, elevator+1, steps+1])
                    states_seen.add(s)
            # down
            if elevator > 0:
                floors2 = deepcopy(floors)
                floors2[elevator-1].append(item1)
                floors2[elevator-1].append(item2)
                floors2[elevator].remove(item1)
                floors2[elevator].remove(item2)
                s = encode_state(floors2, elevator-1)
                if s not in states_seen and is_valid(floors2):
                    states.append([floors2, elevator-1, steps+1])
                    states_seen.add(s)


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    chip = re.compile(r'(\w+)-compatible microchip')
    generator = re.compile(r'(\w+) generator')
    floors = [[] for i in range(4)]
    for i, line in enumerate(lines):
        j = 0
        while m := chip.search(line[j:]):
            floors[i].append(m.group(1)[0] + 'C')
            j += m.end()
        j = 0
        while m := generator.search(line[j:]):
            floors[i].append(m.group(1)[0] + 'G')
            j += m.end()
    # add the new items
    floors[0].extend(['eC', 'eG', 'dC', 'dG'])

    def is_valid(floors):
        for floor in floors:
            chips = []
            generators = []
            for item in floor:
                if item.endswith('C'):
                    chips.append(item[0])
                elif item.endswith('G'):
                    generators.append(item[0])
            for chip in chips:
                if chip not in generators and len(generators) > 0:
                    return False
        return True

    def encode_state(floors, elevator):
        s = str(elevator)
        for floor in floors:
            s += '|'
            floor.sort()
            s += '-'.join(floor)
        return s

    # state: valid config of floors, elevators, steps
    states = [[floors, 0, 0]]
    states_seen = set(encode_state(floors, 0))
    while True:
        if len(states) % 100 == 0:
        floors, elevator, steps = states.pop(0)
        # if final state
        if floors[0] == floors[1] == floors[2] == []:
            return steps
        # generate new states: (1) for each item on the same floor, try to move
        # it up or do
        for item in floors[elevator]:
            # up
            if elevator < 3:
                floors2 = deepcopy(floors)
                floors2[elevator+1].append(item)
                floors2[elevator].remove(item)
                s = encode_state(floors2, elevator+1)
                if s not in states_seen and is_valid(floors2):
                    states.append([floors2, elevator+1, steps+1])
                    states_seen.add(s)
            # down
            if elevator > 0:
                floors2 = deepcopy(floors)
                floors2[elevator-1].append(item)
                floors2[elevator].remove(item)
                s = encode_state(floors2, elevator-1)
                if s not in states_seen and is_valid(floors2):
                    states.append([floors2, elevator-1, steps+1])
                    states_seen.add(s)
        # (2) try to move any two-combinations up or down:
        for item1, item2 in combinations(floors[elevator], 2):
            # up
            if elevator < 3:
                floors2 = deepcopy(floors)
                floors2[elevator+1].append(item1)
                floors2[elevator+1].append(item2)
                floors2[elevator].remove(item1)
                floors2[elevator].remove(item2)
                s = encode_state(floors2, elevator+1)
                if s not in states_seen and is_valid(floors2):
                    states.append([floors2, elevator+1, steps+1])
                    states_seen.add(s)
            # down
            if elevator > 0:
                floors2 = deepcopy(floors)
                floors2[elevator-1].append(item1)
                floors2[elevator-1].append(item2)
                floors2[elevator].remove(item1)
                floors2[elevator].remove(item2)
                s = encode_state(floors2, elevator-1)
                if s not in states_seen and is_valid(floors2):
                    states.append([floors2, elevator-1, steps+1])
                    states_seen.add(s)


assert task1('test_input.txt') == 11
print(task1('input.txt'))

print(task2('input.txt'))
