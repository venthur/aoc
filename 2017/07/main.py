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

    print(candidates)

    # find the leaf if we have more than one candidate
    for a, b in permutations(list(candidates), 2):
        for name, _, aboves in items:
            if name == a and b in aboves:
                candidates.discard(b)

    # get the neighbors of the target
    target = candidates.pop()
    for _, _, aboves in items:
        if target in aboves:
            for a in aboves:
                if a == target:
                    continue
                weight = get_weight(a, items)
    current_weight = get_weight(target, items)
    delta = current_weight - weight
    for name, weight, _ in items:
        if name == target:
            print(name, weight, delta)
            return weight - delta


assert task1("test_input.txt") == "tknk"
print(task1("input.txt"))

assert task2("test_input.txt") == 60
print(task2("input.txt"))


# --- Part Two ---
# 
# The programs explain the situation: they can't get down. Rather, they could
# get down, if they weren't expending all of their energy trying to keep the
# tower balanced. Apparently, one program has the wrong weight, and until it's
# fixed, they're stuck here.
# 
# For any program holding a disc, each program standing on that disc forms a
# sub-tower. Each of those sub-towers are supposed to be the same weight, or
# the disc itself isn't balanced. The weight of a tower is the sum of the
# weights of the programs in that tower.
# 
# In the example above, this means that for ugml's disc to be balanced, gyxo,
# ebii, and jptl must all have the same weight, and they do: 61.
# 
# However, for tknk to be balanced, each of the programs standing on its disc
# and all programs above it must each match. This means that the following sums
# must all be the same:
# 
#     ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
#     padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
#     fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243
# 
# As you can see, tknk's disc is unbalanced: ugml's stack is heavier than the
# other two. Even though the nodes above ugml are balanced, ugml itself is too
# heavy: it needs to be 8 units lighter for its stack to weigh 243 and keep the
# towers balanced. If this change were made, its weight would be 60.
# 
# Given that exactly one program is the wrong weight, what would its weight
# need to be to balance the entire tower?
