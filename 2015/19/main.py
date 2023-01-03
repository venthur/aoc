from heapq import heappush, heappop


def task1(fn):

    with open(fn) as fh:
        data = fh.read().splitlines()
    rules_raw = data[:-2]
    molecule = data[-1]

    rules = []
    for rule in rules_raw:
        rules.append(rule.split(' => '))

    distinct = set()
    for in_, out in rules:
        i = 0
        while True:
            i = molecule.find(in_, i)
            if i == -1:
                break
            new = molecule[:i] + out + molecule[i+len(in_):]
            distinct.add(new)
            i += 1

    return len(distinct)


def task2(fn):

    with open(fn) as fh:
        data = fh.read().splitlines()
    rules_raw = data[:-2]
    molecule = data[-1]

    rules = []
    for rule in rules_raw:
        rules.append(rule.split(' => '))

    rules.sort(key=lambda x: len(x[1]), reverse=True)

    h = []
    heappush(h, (len(molecule), 0, molecule))
    seen = set()
    while True:
        _, steps, current = heappop(h)
        #print(f'{len(current)=} {len(h)=}, {len(seen)=}')
        if current == 'e':
            return steps
        for in_, out in rules:
            i = 0
            while True:
                i = current.find(out, i)
                if i == -1:
                    break
                # optimization to eliminate the Rn..Ar pairs first
                if 'Rn' in current:
                    if not (current.find('Rn') < i < current.find('Ar') or 'Rn' in out):
                        i += 1
                        continue
                new = current[:i] + in_ + current[i+len(out):]
                if new not in seen:
                    heappush(h, (len(new), steps+1, new))
                    seen.add(new)
                i += 1


assert task1('test_input.txt') == 4
assert task1('test_input2.txt') == 7
print(task1('input.txt'))

assert task2('test_input3.txt') == 3
assert task2('test_input4.txt') == 6
print(task2('input.txt'))
