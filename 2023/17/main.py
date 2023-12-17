from heapq import heappush, heappop, heapify


def task1(fn):
    maze = dict()
    with open(fn) as fh:
        for y, line in enumerate(fh.read().splitlines()):
            for x, char in enumerate(line):
                maze[(x, y)] = int(char)

    GOAL = x, y

    # heuristic, cost, x, y, d
    queue = []
    heappush(queue, (0, 0, 0, 0, 1))
    heappush(queue, (0, 0, 0, 0, 2))

    visited = set()

    while queue:
        _, cost, x, y, d = heappop(queue)
        visited.add((x, y, d))

        if (x, y) == GOAL:
            return cost

        for d2 in (d + 1) % 4, (d - 1) % 4:
            costs = 0
            for steps in range(1, 3+1):
                if d2 == 0:
                    x2, y2 = x, y - steps
                elif d2 == 2:
                    x2, y2 = x, y + steps
                elif d2 == 1:
                    x2, y2 = x + steps, y
                elif d2 == 3:
                    x2, y2 = x - steps, y

                value = maze.get((x2, y2))
                if value is None:
                    break
                costs += value

                if (x2, y2, d2) not in visited:
                    cost2 = cost + costs
                    h2 = cost2 + abs(GOAL[0] - x2) + abs(GOAL[1] - y2)
                    for i, (hq, costq, xq, yq, dq) in enumerate(queue):
                        if (x2, y2, d2) == (xq, yq, dq):
                            if h2 < hq:
                                queue[i] = (h2, cost2, x2, y2, d2)
                                heapify(queue)
                                break
                            else:
                                break
                    else:
                        heappush(queue, (h2, cost2, x2, y2, d2))


def task2(fn):
    maze = dict()
    with open(fn) as fh:
        for y, line in enumerate(fh.read().splitlines()):
            for x, char in enumerate(line):
                maze[(x, y)] = int(char)

    GOAL = x, y

    # heuristic, cost, x, y, d
    queue = []
    heappush(queue, (0, 0, 0, 0, 1))
    heappush(queue, (0, 0, 0, 0, 2))

    visited = set()

    while queue:
        _, cost, x, y, d = heappop(queue)
        visited.add((x, y, d))

        if (x, y) == GOAL:
            return cost

        for d2 in (d + 1) % 4, (d - 1) % 4:
            if d2 == 0:
                try:
                    costs = sum(maze[(x, y - i)] for i in range(1, 3+1))
                except KeyError:
                    continue
            elif d2 == 2:
                try:
                    costs = sum(maze[(x, y + i)] for i in range(1, 3+1))
                except KeyError:
                    continue
            elif d2 == 1:
                try:
                    costs = sum(maze[(x + i, y)] for i in range(1, 3+1))
                except KeyError:
                    continue
            elif d2 == 3:
                try:
                    costs = sum(maze[(x - i, y)] for i in range(1, 3+1))
                except KeyError:
                    continue

            for steps in range(4, 10+1):
                if d2 == 0:
                    x2, y2 = x, y - steps
                elif d2 == 2:
                    x2, y2 = x, y + steps
                elif d2 == 1:
                    x2, y2 = x + steps, y
                elif d2 == 3:
                    x2, y2 = x - steps, y

                value = maze.get((x2, y2))
                if value is None:
                    break
                costs += value

                if (x2, y2, d2) not in visited:
                    cost2 = cost + costs
                    h2 = cost2 + abs(GOAL[0] - x2) + abs(GOAL[1] - y2)
                    for i, (hq, costq, xq, yq, dq) in enumerate(queue):
                        if (x2, y2, d2) == (xq, yq, dq):
                            if h2 < hq:
                                queue[i] = (h2, cost2, x2, y2, d2)
                                heapify(queue)
                                break
                            else:
                                break
                    else:
                        heappush(queue, (h2, cost2, x2, y2, d2))


assert task1('test_input.txt') == 102
print(task1('input.txt'))

assert task2('test_input.txt') == 94
print(task2('input.txt'))
