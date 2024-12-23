from collections import defaultdict
from itertools import combinations


def read_input(fn):
    graph = defaultdict(set)
    with open(fn) as fh:
        for line in fh:
            a, b = line.strip().split('-')
            graph[a].add(b)
            graph[b].add(a)
    return graph


def task1(fn):
    graph = read_input(fn)
    clusters = set()
    for node, neighbours in graph.items():
        for a, b in combinations(neighbours, 2):
            if (
                (a.startswith('t') or b.startswith('t') or node.startswith('t')) and
                b in graph[a] and node in graph[a] and
                a in graph[b] and node in graph[b]
            ):
                clusters.add(tuple(sorted([node, a, b])))
    return len(clusters)


def task2(fn):
    graph = read_input(fn)

    todo = {(node, ) for node in graph}
    result = set()
    while todo:
        cluster = todo.pop()
        candidates = set()
        for node in cluster:
            candidates.update(graph[node])
        candidates.difference_update(cluster)
        found = False
        for node in candidates:
            if all(node in graph[other] for other in cluster):
                todo.add(tuple(sorted(set(cluster) | {node})))
                found = True
        if not found:
            result.add(tuple(sorted(cluster)))
    result = sorted(result, key=lambda x: len(x))
    return ','.join(result[-1])


assert task1('test_input.txt') == 7
print(task1('input.txt'))

assert task2('test_input.txt') == 'co,de,ka,ta'
print(task2('input.txt'))
