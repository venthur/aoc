import re
from collections import defaultdict

def task1(fn, values):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    rules = dict()
    agents = defaultdict(list)

    init = re.compile(r'^value (\d+) goes to (.*?)$')
    process = re.compile(r'^(.*?) gives low to (.*?) and high to (.*?)$')
    for line in lines:
        if m := init.match(line):
            v, agent = m.groups()
            agents[agent].append(int(v))
        elif m := process.match(line):
            agent, low, high = m.groups()
            rules[agent] = (low, high)
        else:
            raise ValueError()

    while True:
        for agent, (low, high) in rules.items():
            if not agent.startswith('bot'):
                continue
            for v in values:
                if v not in agents[agent]:
                    break
            else:
                return int(agent.split()[-1])
            if len(agents[agent]) >= 2:
                lv, hv = sorted(agents[agent][:2])
                agents[agent] = agents[agent][2:]
                agents[low].append(lv)
                agents[high].append(hv)


assert task1('test_input.txt', (5, 2)) == 2
print(task1('input.txt', (17, 61)))
