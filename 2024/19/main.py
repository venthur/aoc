from functools import cache


def read_input(fn):
    with open(fn) as fh:
        patterns_raw, designs_raw = fh.read().split('\n\n')
    patterns = tuple(patterns_raw.strip().split(', '))
    designs = designs_raw.strip().split('\n')

    return patterns, designs


@cache
def count_matches(string, prefixes):
    if string == '':
        return 1
    c = 0
    for i, prefix in enumerate(prefixes):
        if string.startswith(prefix):
           c += count_matches(string[len(prefix):], prefixes)
    return c


def task1(fn):
    patterns, designs = read_input(fn)

    c = 0
    for design in designs:
        prefixes = count_matches(design, patterns)
        c += 1 if prefixes > 0 else 0
    return c


def task2(fn):
    patterns, designs = read_input(fn)

    c = 0
    for design in designs:
        c += count_matches(design, patterns)
    return c


assert task1('test_input.txt') == 6
print(task1('input.txt'))

assert task2('test_input.txt') == 16
print(task2('input.txt'))
