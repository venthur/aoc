def task1(fn):
    with open(fn) as fh:
        data = fh.read().strip()

    trash = False
    score = 0
    group = 0
    i = 0
    while i < len(data):
        c = data[i]
        if trash:
            if c == '>':
                trash = False
            elif c == '!':
                i += 1
        else:
            if c == '{':
                group += 1
            elif c == '}':
                score += group
                group -= 1
            elif c == '<':
                trash = True
        i += 1
    return score


def task2(fn):
    with open(fn) as fh:
        data = fh.read().strip()

    trash = False
    count = 0
    i = 0
    while i < len(data):
        c = data[i]
        if trash:
            if c == '>':
                trash = False
            elif c == '!':
                i += 1
            else:
                count += 1
        else:
            if c == '<':
                trash = True
        i += 1
    return count


print(task1('input.txt'))
print(task2('input.txt'))
