from functools import cache


def task1(fn):
    paths = dict()
    with open(fn) as fh:
        for line in fh:
            start, ends = line.strip().split(':')
            paths[start] = [end for end in ends.split()]

    def count_paths(node):

        if node == 'out':
            return 1

        npaths = 0
        for next_ in paths[node]:
            npaths += count_paths(next_)
        return npaths

    return count_paths('you')


def task2(fn):
    paths = dict()
    with open(fn) as fh:
        for line in fh:
            start, ends = line.strip().split(':')
            paths[start] = [end for end in ends.split()]

    @cache
    def count_paths(node, dac, fft):

        if node == 'out':
            if dac and fft:
                return 1
            else:
                return 0

        if node == 'dac':
            dac = True
        if node == 'fft':
            fft = True

        npaths = 0
        for next_ in paths[node]:
            npaths += count_paths(next_, dac, fft)
        return npaths

    return count_paths('svr', False, False)


assert task1('test_input.txt') == 5
print(task1('input.txt'))

assert task2('test_input2.txt') == 2
print(task2('input.txt'))
