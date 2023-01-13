def hash_(s):

    lengths = [ord(b) for b in s]
    lengths += [17, 31, 73, 47, 23]
    numbers = [i for i in range(256)]

    pos = 0
    skip_size = 0
    for i in range(64):
        for l in lengths:
            # shift pos numbers to the left to avoid wraparound logic
            numbers = numbers[pos:] + numbers[:pos]

            numbers = numbers[:l][::-1] + numbers[l:]

            # shift back
            numbers = numbers[-pos:] + numbers[:-pos]

            pos += l + skip_size
            pos %= len(numbers)
            skip_size += 1

    dense = []
    for i in range(16):
        b = numbers[:16]
        numbers = numbers[16:]
        v = (
            b[0] ^ b[1] ^ b[2] ^ b[3] ^ b[4] ^ b[5] ^ b[6] ^ b[7] ^
            b[8] ^ b[9] ^ b[10] ^ b[11] ^ b[12] ^ b[13] ^ b[14] ^ b[15]
        )
        dense.append(v)

    densehex = ''.join([f'{i:0>8b}' for i in dense])
    return densehex


def task1(s):
    sum_ = 0
    for i in range(128):
        sum_ += hash_(f'{s}-{i}').count('1')
    return sum_


def task2(s):
    used = set()
    for i in range(128):
        row = hash_(f'{s}-{i}')
        for j, c in enumerate(row):
            if c == '1':
                used.add((j, i))

    groups = 0
    while used:
        groups += 1
        stack = []
        x, y = used.pop()
        stack.append((x, y))
        while stack:
            x, y = stack.pop()
            for pos in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                if pos in used:
                    used.discard(pos)
                    stack.append(pos)

    return groups


print(task1('stpzcrnm'))
print(task2('stpzcrnm'))
