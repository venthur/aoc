import re


def task1(fn):
    with open(fn) as fh:
        blocks = fh.read().split('\n\n')

    rules = dict()
    p = re.compile(r'([a-zA-Z]+)\{(.+)\}')
    for line in blocks[0].splitlines():
        rule_id, rule = p.match(line).groups()
        rule = rule.split(',')
        rules[rule_id] = rule

    accepted = []
    for line in blocks[1].splitlines():
        line = line[1:-1]

        input_ = dict()
        for i in line.split(','):
            l, v = i.split('=')
            input_[l] = int(v)

        rule = 'in'
        while True:

            if rule == 'A':
                accepted.append(input_)
                break
            if rule == 'R':
                break

            for rule in rules[rule]:
                if rule == 'R':
                    break
                if rule == 'A':
                    break
                if ':' not in rule:
                    break
                if '<' in rule:
                    rule, target = rule.split(':')
                    l, n = rule.split('<')
                    n = int(n)
                    if input_[l] < n:
                        rule = target
                        break
                if '>' in rule:
                    rule, target = rule.split(':')
                    l, n = rule.split('>')
                    n = int(n)
                    if input_[l] > n:
                        rule = target
                        break

    result = 0
    for a in accepted:
        result += sum(a.values())
    return result


def task2(fn):

    MIN, MAX = 1, 4000

    with open(fn) as fh:
        blocks = fh.read().split('\n\n')

    rules = dict()
    p = re.compile(r'([a-zA-Z]+)\{(.+)\}')
    for line in blocks[0].splitlines():
        rule_id, rule = p.match(line).groups()
        rule = rule.split(',')
        rules[rule_id] = rule

    def acceptable(rule_id, intervals):
        intervals = intervals.copy()

        if rule_id == 'R':
            return 0
        if rule_id == 'A':
            combinations = 1
            for i in intervals.values():
                combinations *= len(i)
            return combinations
        combinations = 0
        for rule in rules[rule_id]:
            if rule in 'AR' or ':' not in rule:
                combinations += acceptable(rule, intervals)
                continue
            if '<' in rule:
                rule, target = rule.split(':')
                l, n = rule.split('<')
                n = int(n)
                interval1 = intervals.copy()
                interval1[l] = intervals[l].intersection(
                    {i for i in range(MIN, n)}
                )
                combinations += acceptable(target, interval1)

                intervals[l] = intervals[l].intersection(
                    {i for i in range(n, MAX+1)}
                )
            if '>' in rule:
                rule, target = rule.split(':')
                l, n = rule.split('>')
                n = int(n)
                interval1 = intervals.copy()
                interval1[l] = intervals[l].intersection(
                    {i for i in range(n+1, MAX+1)}
                )
                combinations += acceptable(target, interval1)

                intervals[l] = intervals[l].intersection(
                    {i for i in range(MIN, n+1)}
                )
        return combinations

    return acceptable(
        'in',
        {
            'x': {i for i in range(MIN, MAX+1)},
            'm': {i for i in range(MIN, MAX+1)},
            'a': {i for i in range(MIN, MAX+1)},
            's': {i for i in range(MIN, MAX+1)},
        },
    )


assert task1('test_input.txt') == 19114
print(task1('input.txt'))

assert task2('test_input.txt') == 167409079868000
print(task2('input.txt'))
