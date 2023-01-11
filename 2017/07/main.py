import re
from itertools import permutations


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    items = []
    for line in lines:
        name, weight, above = re.match(
            r"^(\w+) \((\d+)\)(?: -> (.*))?$",
            line,
        ).groups()
        weight = int(weight)
        above = (
            [n.strip() for n in above.split(",")] if above is not None else []
        )
        items.append([name, weight, above])

    candidates = set(name for name, _, _ in items)
    for name, _, above in items:
        for x in above:
            candidates.discard(x)

    return candidates.pop()


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    items = []
    for line in lines:
        name, weight, above = re.match(
            r"^(\w+) \((\d+)\)(?: -> (.*))?$",
            line,
        ).groups()
        weight = int(weight)
        above = (
            [n.strip() for n in above.split(",")] if above is not None else []
        )
        items.append([name, weight, above])

    def get_weight(name, items):
        for n, w, a in items:
            if n != name:
                continue
            if not a:
                return w
            return w + sum([get_weight(i, items) for i in a])

    candidates = set()
    for name, weight, above in items:
        weights = [get_weight(a, items) for a in above]
        if len(set(weights)) != 1:
            if len(above) == 2:
                for a in above:
                    candidates.add(a)
            else:
                # find the common element
                count = 0
                item = None
                for w in weights:
                    c = weights.count(w)
                    if c > count:
                        count = c
                        item = w
                for i, w in enumerate(weights):
                    if w != item:
                        candidates.add(above[i])

    # find the leaf if we have more than one candidate
    for a, b in permutations(list(candidates), 2):
        for name, _, aboves in items:
            if name == a and b in aboves:
                candidates.discard(a)

    # get the neighbors of the target
    target = candidates.pop()
    for _, _, aboves in items:
        if target in aboves:
            for a in aboves:
                if a == target:
                    continue
                weight = get_weight(a, items)
    current_weight = get_weight(target, items)
    delta = weight - current_weight
    for name, weight, _ in items:
        if name == target:
            return weight + delta


assert task1("test_input.txt") == "tknk"
print(task1("input.txt"))

assert task2("test_input.txt") == 60
print(task2("input.txt"))
