from itertools import combinations, permutations
from functools import cmp_to_key


def read_input(fn):
    with open(fn) as fh:
        data = fh.read()

    rules, updates = data.split('\n\n')

    rules = [tuple(map(int, s.split('|'))) for s in rules.split()]
    updates = [tuple(map(int, s.split(','))) for s in updates.split()]

    return rules, updates


def is_correct(update, rules):
    for a, b in combinations(update, 2):
        if (a, b) not in rules:
            return False
    return True


def task1(fn):
    rules, updates = read_input(fn)

    s = 0
    for update in updates:
        if is_correct(update, rules):
            s += update[(len(update) - 1) // 2]
    return s


def task2(fn):
    rules, updates = read_input(fn)

    incorrect_updates = [u for u in updates if not is_correct(u, rules)]

    s = 0
    for update in incorrect_updates:

        matching_rules = []
        for a, b in permutations(update, 2):
            for r in rules:
                if r == (a, b):
                    matching_rules.append(r)
                    break

        def cmp(a, b):
            for x, y in matching_rules:
                if a == x and b == y:
                    return -1
                if a == y and b == x:
                    return 1
            raise ValueError(f'No match for {a=} {b=}')

        update = list(update)
        update.sort(key=cmp_to_key(cmp))

        s += update[(len(update) - 1) // 2]

    return s


assert task1('test_input.txt') == 143
print(task1('input.txt'))

assert task2('test_input.txt') == 123
print(task2('input.txt'))
