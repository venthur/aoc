from collections import deque


def parse_input(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    blueprints = []
    for line in lines:
        bp, line = line.split(': ', maxsplit=1)
        bp = int(bp.split()[-1])
        costs = line.split('.')
        # ore
        ore = int(costs[0].split()[-2])
        ore = (ore, 0, 0)
        # ore
        clay = int(costs[1].split()[-2])
        clay = (clay, 0, 0)
        # ore, clay
        obsidian = [int(c.split()[-2]) for c in costs[2].split('and')]
        obsidian = (obsidian[0], obsidian[1], 0)
        # ore, obsidian
        geode = [int(c.split()[-2]) for c in costs[3].split('and')]
        geode = (geode[0], 0, geode[1])
        blueprints.append((bp, ore, clay, obsidian, geode))

    return blueprints


def max_geodes(blueprint, minutes):
    # state:
    # minute, ore, clay, obsidian, geode (pm, amount)
    start = (0, 1, 0, 0, 0, 0, 0, 0, 0)

    # compute max resources to produce any robot
    max_resources = [0, 0, 0]
    for robot in blueprint:
        for i, cost in enumerate(robot):
            max_resources[i] = max(max_resources[i], cost)

    queue = deque([])
    queue.append(start)
    seen = set()
    seen.add(start)
    best = 0
    while queue:
        state = queue.popleft()

        geodes = state[-1] + state[-2] * (minutes - state[0])
        best = max(best, geodes)

        for ri, robot in enumerate(blueprint):
            # time per resource for next robot
            time_needed = [0, 0, 0]
            for i in range(3):
                if robot[i] <= state[2+i*2]:
                    # have enough
                    continue
                else:
                    if state[1+i*2] == 0:
                        # don't produce resource yet
                        time_needed[i] = minutes+1
                    else:
                        q, r = divmod((robot[i] - state[2+i*2]), state[1+i*2])
                        q += 1 if r > 0 else 0
                        time_needed[i] = q
            dt = max(time_needed)

            if state[0] + dt + 1 + 1 <= minutes:
                # enough time to build and harvest
                state2 = list(state)
                # harvest all until dt + 1
                for i in range(4):
                    state2[2+i*2] += (dt+1) * state[1+i*2]
                # cost for the robot
                for i in range(3):
                    state2[2+i*2] -= robot[i]
                # new robot
                state2[1+ri*2] += 1

                # update time
                state2[0] += dt + 1

                # optimization - if it costs N to produce a robot, don't have
                # M > N robots collecting that resource
                if not all(state2[1+i*2] <= max_resources[i] for i in range(3)):
                    continue

                # optimization - skip states that can't be better than current
                # best
                time_left = minutes - state[2]
                geodes_ideal = (time_left-1) * (time_left) // 2  # triangular number, don't ask...
                geodes_max = state[2+3*2] + state[1+3*2] * time_left + geodes_ideal
                if geodes_max <= best:
                    continue

                state2 = tuple(state2)
                if state2 not in seen:
                    seen.add(state2)
                    queue.append(state2)

    return best


def task1(fn):
    blueprints = parse_input(fn)

    sum_ = 0
    for i, *bp in blueprints:
        sum_ += i * max_geodes(bp, 24)

    return sum_


def task2(fn):
    blueprints = parse_input(fn)

    prod = 1
    for i, *bp in blueprints[:3]:
        prod *= max_geodes(bp, 32)
    return prod


assert task1('test_input.txt') == 33
print(task1('input.txt'))

print(task2('input.txt'))
