def task1(fn):
    with open(fn) as fh:
        rules, messages = fh.read().split('\n\n')

    rules = rules.replace('"', '')
    rules = rules.splitlines()
    rules = [rule.split(': ') for rule in rules]
    rules = dict(rules)

    allowed = set()
    todo = [rules['0']]
    seen = {rules['0']}
    while todo:
        pattern = todo.pop()
        if pattern.replace(' ', '').isalpha():
            pattern = pattern.replace(' ', '')
            allowed.add(pattern)
        else:
            pattern = pattern.split()
            for i, token in enumerate(pattern):
                if token.isalpha():
                    continue
                new_rule = rules[token]
                for r in new_rule.split('|'):
                    r = r.strip()
                    pattern2 = pattern[:]
                    pattern2[i] = r
                    pattern2 = ' '.join(pattern2)
                    if pattern2 not in seen:
                        seen.add(pattern2)
                        todo.append(pattern2)
                break

    messages = messages.splitlines()

    count = 0
    for m in messages:
        if m in allowed:
            count += 1

    return count


def task2(fn):
    with open(fn) as fh:
        rules, messages = fh.read().split('\n\n')

    rules = rules.replace('"', '')
    rules = rules.splitlines()
    rules = [rule.split(': ') for rule in rules]
    rules = dict(rules)
    rules["8"] = "42 | 42 8"
    rules["11"] = "42 31 | 42 11 31"

    def match(string, ptr, rule):

        if rule.isalpha():
            if ptr < len(string) and string[ptr] == rule:
                yield ptr+1
            return
        for alt in rule.split(' | '):
            tokens = alt.split(' ', 1)
            if len(tokens) == 1:
                yield from match(string, ptr, rules[tokens[0]])
            else:
                for m in match(string, ptr, rules[tokens[0]]):
                    yield from match(string, m, tokens[1])

    counter = sum(
        1 if any(m == len(line) for m in match(line, 0, '0')) else 0
        for line in messages.splitlines()
    )
    return counter


assert task1('test_input0.txt') == 2
print(task1('input.txt'))

print(task2('input.txt'))
