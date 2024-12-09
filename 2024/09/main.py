def read_data(fn):
    files = []
    free_blocks = []
    with open(fn) as fh:
        data = [int(i) for i in fh.read().strip()]
    pos = 0
    for i, block in enumerate(data):
        if i % 2 == 0:
            files.append([j for j in range(pos, pos + block)])
            pos += block
        else:
            free_blocks.extend([j for j in range(pos, pos + block)])
            pos += block
    return files, free_blocks


def task1(fn):
    files, free_blocks = read_data(fn)

    for file in reversed(files):
        for block in range(len(file)-1, 0-1, -1):
            try:
                if free_blocks[0] < file[block]:
                    fblock = free_blocks.pop(0)
                    file[block] = fblock
            except IndexError:
                break

    s = 0
    for fileid, file in enumerate(files):
        for block in file:
            s += fileid * block
    return s


def task2(fn):
    files, free_blocks = read_data(fn)
    for file in reversed(files):
        l = len(file)
        for i in range(len(free_blocks) - l):
            for j in range(l-1):
                if free_blocks[i+j] != free_blocks[i+j+1] - 1:
                    break
            else:
                if free_blocks[i] > file[0]:
                    break
                free = []
                for j in range(l):
                    free.append(file[j])
                    file[j] = free_blocks.pop(i)
                free_blocks.extend(free)
                free_blocks.sort()
                break

    s = 0
    for fileid, file in enumerate(files):
        for block in file:
            s += fileid * block
    return s


assert task1('test_input.txt') == 1928
print(task1('input.txt'))

assert task2('test_input.txt') == 2858
print(task2('input.txt'))
