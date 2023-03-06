def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    p = 0
    for line in lines:
        stack = []
        for char in line:
            if char in '[({<':
                stack.append(char)
            elif len(stack) > 0:
                char2 = stack.pop()
                if char2+char not in ('()', '[]', '{}', '<>'):
                    p += points[char]
                    break
            else:
                p += points[char]
                break
    return p


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    points = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }

    # filter out corrupt lines
    lines2 = lines[:]
    for line in lines2:
        stack = []
        for char in line:
            if char in '[({<':
                stack.append(char)
            elif len(stack) > 0:
                char2 = stack.pop()
                if char2+char not in ('()', '[]', '{}', '<>'):
                    lines.remove(line)
                    break
            else:
                lines.remove(line)
                break

    scores = []
    for line in lines:
        s = 0
        stack = []
        for char in line:
            if char in '[({<':
                stack.append(char)
            elif len(stack) > 0:
                char2 = stack.pop()
        # only open should be left
        while stack:
            char = stack.pop()
            s = s*5 + points[char]
        scores.append(s)

    scores.sort()
    return scores[len(scores)//2]


assert task1('test_input0.txt') == 26397
print(task1('input.txt'))

assert task2('test_input0.txt') == 288957
print(task2('input.txt'))
