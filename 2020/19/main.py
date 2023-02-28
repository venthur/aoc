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

    max_l = max(len(m) for m in messages.splitlines())

    allowed = set()
    todo = [rules['0']]
    seen = {rules['0']}
    while todo:
        pattern = todo.pop(0)
        if pattern.replace(' ', '').isalpha():
            pattern = pattern.replace(' ', '')
            allowed.add(pattern)
            print(f'{len(todo)} {len(allowed)}')
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
                    #if pattern2 not in seen and len(pattern2.replace(' ', '')) <= max_l:
                    if len(pattern2.replace(' ', '')) <= max_l:
                        #seen.add(pattern2)
                        todo.append(pattern2)
                break

    messages = messages.splitlines()

    count = 0
    for m in messages:
        if m in allowed:
            count += 1

    return count



#assert task1('test_input0.txt') == 2
#print(task1('input.txt'))

print(task2('input.txt'))
