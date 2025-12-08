from itertools import combinations
from math import dist


def task1(fn, max_connections):
    positions = []
    with open(fn) as fh:
        for line in fh:
            pos = tuple(int(i) for i in line.strip().split(','))
            positions.append(pos)

    distances = []
    for p1, p2 in combinations(positions, 2):
        d = dist(p1, p2)
        distances.append((d, p1, p2))
    distances.sort()

    clusters = []
    connections = 0
    for d, p1, p2 in distances:
        if connections >= max_connections:
            break

        conn_cluster_1 = None
        conn_cluster_2 = None
        for c in clusters:
            if p1 in c:
                conn_cluster_1 = c
            if p2 in c:
                conn_cluster_2 = c

        # both are not connected
        if conn_cluster_1 is None and conn_cluster_2 is None:
            clusters.append({p1, p2})
            connections += 1
            continue

        # both are already in same cluster
        if conn_cluster_1 == conn_cluster_2:
            connections += 1
            continue

        # one is connected the other is not
        if conn_cluster_1 and conn_cluster_2 is None:
            conn_cluster_1.add(p2)
            connections += 1
            continue
        if conn_cluster_2 and conn_cluster_1 is None:
            conn_cluster_2.add(p1)
            connections += 1
            continue

        # both are in different clusters
        if conn_cluster_1 is not None and conn_cluster_2 is not None:
            clusters.remove(conn_cluster_2)
            clusters.remove(conn_cluster_1)
            clusters.append(conn_cluster_1.union(conn_cluster_2))
            connections += 1
            continue

    lengths = [len(c) for c in clusters]
    lengths.sort(reverse=True)
    return lengths[0] * lengths[1] * lengths[2]


def task2(fn):
    positions = []
    with open(fn) as fh:
        for line in fh:
            pos = tuple(int(i) for i in line.strip().split(','))
            positions.append(pos)

    distances = []
    for p1, p2 in combinations(positions, 2):
        d = dist(p1, p2)
        distances.append((d, p1, p2))
    distances.sort()

    clusters = []
    connections = 0
    last_connection = None
    for d, p1, p2 in distances:

        conn_cluster_1 = None
        conn_cluster_2 = None
        for c in clusters:
            if p1 in c:
                conn_cluster_1 = c
            if p2 in c:
                conn_cluster_2 = c

        # both are not connected
        if conn_cluster_1 is None and conn_cluster_2 is None:
            clusters.append({p1, p2})
            connections += 1
            last_connection = (p1, p2)
            continue

        # both are already in same cluster
        if conn_cluster_1 == conn_cluster_2:
            connections += 1
            continue

        # one is connected the other is not
        if conn_cluster_1 and conn_cluster_2 is None:
            conn_cluster_1.add(p2)
            connections += 1
            last_connection = (p1, p2)
            continue
        if conn_cluster_2 and conn_cluster_1 is None:
            conn_cluster_2.add(p1)
            connections += 1
            last_connection = (p1, p2)
            continue

        # both are in different clusters
        if conn_cluster_1 is not None and conn_cluster_2 is not None:
            clusters.remove(conn_cluster_2)
            clusters.remove(conn_cluster_1)
            clusters.append(conn_cluster_1.union(conn_cluster_2))
            connections += 1
            last_connection = (p1, p2)
            continue

    return last_connection[0][0] * last_connection[1][0]


assert task1('test_input.txt', 10) == 40
print(task1('input.txt', 1000))

assert task2('test_input.txt') == 25272
print(task2('input.txt'))
