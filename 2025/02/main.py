def task1(fn):
    ranges = []
    with open(fn) as fh:
        data = fh.read()
        for r in data.split(','):
            start, end = r.split('-')
            ranges.append((int(start), int(end)))

    invalids = []
    for start, end in ranges:
        for i in range(start, end+1):
            i_str = str(i)
            if len(i_str) % 2 != 0:
                continue
            half = len(i_str) // 2
            if i_str[:half] == i_str[half:]:
                invalids.append(i)

    return sum(invalids)


def task2(fn):
    ranges = []
    with open(fn) as fh:
        data = fh.read()
        for r in data.split(','):
            start, end = r.split('-')
            ranges.append((int(start), int(end)))

    invalids = []
    for start, end in ranges:
        for i in range(start, end+1):
            i_str = str(i)

            for t in range(2, len(i_str)+1):
                if len(i_str) % t != 0:
                    continue

                chunkl = len(i_str) // t

                chunks = []
                for j in range(t):
                    chunks.append(i_str[j*chunkl:(j+1)*chunkl])
                if len(set(chunks)) == 1:
                    invalids.append(i)
                    break

    return sum(invalids)


assert task1('test_input.txt') == 1227775554
print(task1('input.txt'))

assert task2('test_input.txt') == 4174379265
print(task2('input.txt'))
