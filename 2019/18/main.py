import heapq
from math import dist


def read_input(fn):

    with open(fn) as fh:
        lines = fh.read().splitlines()

    area = dict()
    keys, doors = dict(), dict()
    x, y = None, None
    for yi, line in enumerate(lines):
        for xi, char in enumerate(line):
            if char in '#.':
                area[xi, yi] = char
            elif char == '@':
                x, y = xi, yi
                area[xi, yi] = '.'
            elif char in 'abcdefghijklmnopqrstuvwxyz':
                area[xi, yi] = '.'
                keys[xi, yi] = char
            elif char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                area[xi, yi] = '.'
                doors[xi, yi] = char.lower()
            else:
                raise ValueError(char)
    return x, y, area, doors, keys


def reachable_keys(x, y, area, doors, keys):
    keys = keys.copy()

    queue = [(x, y)]
    visited = {(x, y)}
    reachable = []
    while queue:
        x, y = queue.pop(0)
        if (x, y) in keys:
            reachable.append((keys.pop((x, y)), x, y))
            # treat the key as a wall
            continue
        for xi, yi in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if (
                (xi, yi) not in visited and
                area[xi, yi] == '.' and
                (xi, yi) not in doors
            ):
                visited.add((xi, yi))
                queue.append((xi, yi))
    return reachable

from functools import cache

@cache
def shortest_path(x, y, tx, ty, area, doors):
    area = dict(area)
    doors = dict(doors)
    pq = []
    heapq.heappush(pq, (0, x, y, 0))
    visited = {x, y}
    while pq:
        _, x, y, d = heapq.heappop(pq)
        if (x, y) == (tx, ty):
            return d
        for xi, yi in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if (
                (xi, yi) not in visited and
                area[xi, yi] == '.' and
                (xi, yi) not in doors
            ):
                visited.add((xi, yi))
                heapq.heappush(pq, (d+1+dist((x, y), (xi, yi)), xi, yi, d+1))


def h(x, y, points):
    points = points + [(x, y)]
    xs, ys = zip(*points)
    return dist((min(xs), min(ys)), (max(xs), max(ys)))


def xx(fn):
    x, y, area, doors, keys = read_input(fn)

    pq = []
    heapq.heappush(pq, (0, 0, x, y, doors.items(), keys.items(), []))
    kh = ''.join(sorted(list(keys.values())))
    visited = {(x, y, 0, kh)}
    while pq:
        _, d, x, y, doors, keys, path = heapq.heappop(pq)
        doors = dict(doors)
        keys = dict(keys)

        print(f'{int(_):>5} -> {"->".join(path):<50} {len(pq):>5}', end='\r')
        if len(keys) == 0:
            print()
            print("->".join(path))
            print(d)
            return d

        for key, kx, ky in reachable_keys(x, y, area, doors, keys):
            l = shortest_path(x, y, kx, ky, tuple(area.items()), tuple(doors.items()))
            doors2 = dict(filter(lambda x: x[1] != key, doors.items()))
            keys2 = dict(filter(lambda x: x[1] != key, keys.items()))
            x2, y2 = kx, ky

            kh = ''.join(sorted(list(keys2.values())))
            if (x2, y2, d+l, kh) not in visited:
                #longest = [shortest_path(x2, y2, kx, ky, tuple(area.items()), tuple()) for kx, ky in keys2]
                #longest = max(longest + [0])

                #visited.add((x2, y2, d+l, kh))
                #heapq.heappush(pq, (d+l+longest, d+l, x2, y2, doors2.items(), keys2.items(), path + [key]))

                dist = h(x2, y2, list(keys2.keys()))
                visited.add((x2, y2, d+l, kh))
                heapq.heappush(pq, (d+l+dist, d+l, x2, y2, doors2.items(), keys2.items(), path + [key]))


            #longest = [shortest_path(x2, y2, kx, ky, tuple(area.items()), tuple()) for kx, ky in keys2]
            #longest = max(longest + [0])

            #heapq.heappush(pq, (d+l+longest+len(keys2)-1, d+l, x2, y2, doors2.items(), keys2.items(), path + [key]))


#print(xx('test_input.txt'))
assert xx('test_input0.txt') == 132
assert xx('test_input1.txt') == 136
assert xx('test_input2.txt') == 81
print(xx('input.txt'))


# --- Day 18: Many-Worlds Interpretation ---
# 
# As you approach Neptune, a planetary security system detects you and
# activates a giant tractor beam on Triton! You have no choice but to land.
# 
# A scan of the local area reveals only one interesting feature: a massive
# underground vault. You generate a map of the tunnels (your puzzle input). The
# tunnels are too narrow to move diagonally.
# 
# Only one entrance (marked @) is present among the open passages (marked .)
# and stone walls (#), but you also detect an assortment of keys (shown as
# lowercase letters) and doors (shown as uppercase letters). Keys of a given
# letter open the door of the same letter: a opens A, b opens B, and so on. You
# aren't sure which key you need to disable the tractor beam, so you'll need to
# collect all of them.
# 
# For example, suppose you have the following map:
# 
# #########
# #b.A.@.a#
# #########
# 
# Starting from the entrance (@), you can only access a large door (A) and a
# key (a). Moving toward the door doesn't help you, but you can move 2 steps to
# collect the key, unlocking A in the process:
# 
# #########
# #b.....@#
# #########
# 
# Then, you can move 6 steps to collect the only other key, b:
# 
# #########
# #@......#
# #########
# 
# So, collecting every key took a total of 8 steps.
# 
# Here is a larger example:
# 
# ########################
# #f.D.E.e.C.b.A.@.a.B.c.#
# ######################.#
# #d.....................#
# ########################
# 
# The only reasonable move is to take key a and unlock door A:
# 
# ########################
# #f.D.E.e.C.b.....@.B.c.#
# ######################.#
# #d.....................#
# ########################
# 
# Then, do the same with key b:
# 
# ########################
# #f.D.E.e.C.@.........c.#
# ######################.#
# #d.....................#
# ########################
# 
# ...and the same with key c:
# 
# ########################
# #f.D.E.e.............@.#
# ######################.#
# #d.....................#
# ########################
# 
# Now, you have a choice between keys d and e. While key e is closer,
# collecting it now would be slower in the long run than collecting key d
# first, so that's the best choice:
# 
# ########################
# #f...E.e...............#
# ######################.#
# #@.....................#
# ########################
# 
# Finally, collect key e to unlock door E, then collect key f, taking a grand
# total of 86 steps.
# 
# Here are a few more examples:
# 
#     ########################
#     #...............b.C.D.f#
#     #.######################
#     #.....@.a.B.c.d.A.e.F.g#
#     ########################
# 
#     Shortest path is 132 steps: b, a, c, d, f, e, g
# 
#     #################
#     #i.G..c...e..H.p#
#     ########.########
#     #j.A..b...f..D.o#
#     ########@########
#     #k.E..a...g..B.n#
#     ########.########
#     #l.F..d...h..C.m#
#     #################
# 
#     Shortest paths are 136 steps;
#     one is: a, f, b, j, g, n, h, d, l, o, e, p, c, i, k, m
# 
#     ########################
#     #@..............ac.GI.b#
#     ###d#e#f################
#     ###A#B#C################
#     ###g#h#i################
#     ########################
# 
#     Shortest paths are 81 steps; one is: a, c, f, i, d, g, b, e, h
# 
# How many steps is the shortest path that collects all of the keys?
# 
# To begin, get your puzzle input.
