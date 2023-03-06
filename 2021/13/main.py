def task1(fn):
    with open(fn) as fh:
        dots, folds = fh.read().split('\n\n')

    paper = dict()
    for line in dots.splitlines():
        x, y = [int(n) for n in line.split(',')]
        paper[x, y] = '#'

    for line in folds.splitlines():
        cmd = line.split()[-1]
        ax, v = cmd.split('=')
        for x, y in list(paper.keys()):
            v = int(v)
            if ax == 'x' and x > v:
                paper.pop((x, y))
                paper[v-abs(x-v), y] = '#'
            elif ax == 'y' and y > v:
                paper.pop((x, y))
                paper[x, v-abs(y-v)] = '#'
        return len(paper)


def task2(fn):
    with open(fn) as fh:
        dots, folds = fh.read().split('\n\n')

    paper = dict()
    for line in dots.splitlines():
        x, y = [int(n) for n in line.split(',')]
        paper[x, y] = '#'

    for line in folds.splitlines():
        cmd = line.split()[-1]
        ax, v = cmd.split('=')
        for x, y in list(paper.keys()):
            v = int(v)
            if ax == 'x' and x > v:
                paper.pop((x, y))
                paper[v-abs(x-v), y] = '#'
            elif ax == 'y' and y > v:
                paper.pop((x, y))
                paper[x, v-abs(y-v)] = '#'

    xs, ys = zip(*paper.keys())
    s = ''
    for y in range(min(ys), max(ys)+1):
        for x in range(min(xs), max(xs)+1):
            if (x, y) in paper:
                s += '#'
            else:
                s += ' '
        s += '\n'

    return s


print(task1('input.txt'))

print(task2('input.txt'))
