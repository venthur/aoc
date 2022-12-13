import re
import itertools


def task1(input_):
    with open(input_) as fh:
        lines = fh.read().splitlines()

    distance = dict()
    destinations = set()
    for line in lines:
        origin, dest, dist = re.match(
            r'^(\w*) to (\w*) = (\d*)$',
            line
        ).groups()
        dist = int(dist)

        distance[origin, dest] = dist
        distance[dest, origin] = dist
        destinations.add(origin)
        destinations.add(dest)

    best_dist = None
    candidates = itertools.permutations(destinations)
    for c in candidates:
        dist = 0
        route = []
        for origin, dest in itertools.pairwise(c):
            if (origin, dest) in distance:
                dist += distance[origin, dest]
                route.append((origin, dest))
            else:
                break
        else:
            if (best_dist is None) or (dist < best_dist):
                best_dist = dist

    return best_dist


def task2(input_):
    with open(input_) as fh:
        lines = fh.read().splitlines()

    distance = dict()
    destinations = set()
    for line in lines:
        origin, dest, dist = re.match(
            r'^(\w*) to (\w*) = (\d*)$',
            line
        ).groups()
        dist = int(dist)

        distance[origin, dest] = dist
        distance[dest, origin] = dist
        destinations.add(origin)
        destinations.add(dest)

    best_dist = None
    candidates = itertools.permutations(destinations)
    for c in candidates:
        dist = 0
        route = []
        for origin, dest in itertools.pairwise(c):
            if (origin, dest) in distance:
                dist += distance[origin, dest]
                route.append((origin, dest))
            else:
                break
        else:
            if (best_dist is None) or (dist > best_dist):
                best_dist = dist

    return best_dist


assert task1('test_input.txt') == 605
print(task1('input.txt'))


assert task2('test_input.txt') == 982
print(task2('input.txt'))
