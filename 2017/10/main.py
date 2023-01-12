def task1(fn_or_input):

    if isinstance(fn_or_input, tuple):
        lengths = fn_or_input[-1]
        numbers = [i for i in range(fn_or_input[0])]
    else:
        with open(fn_or_input) as fh:
            data = fh.read().strip()
        lengths = [int(i) for i in data.split(',')]
        numbers = [i for i in range(256)]

    pos = 0
    skip_size = 0

    for l in lengths:
        # shift pos numbers to the left to avoid wraparound logic
        numbers = numbers[pos:] + numbers[:pos]

        numbers = numbers[:l][::-1] + numbers[l:]

        # shift back
        numbers = numbers[-pos:] + numbers[:-pos]

        pos += l + skip_size
        pos %= len(numbers)
        skip_size += 1

    return numbers[0] * numbers[1]


def task2(fn_or_input):

    if isinstance(fn_or_input, bytes):
        lengths = [ord(b) for b in fn_or_input.decode()]
    else:
        with open(fn_or_input, 'rb') as fh:
            data = fh.read().decode().strip()
        lengths = [ord(i) for i in data]

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

    densehex = ''.join([f'{i:0>2x}' for i in dense])
    return densehex


assert task1((5, [3, 4, 1, 5])) == 12
print(task1('input.txt'))

assert task2(b'') == 'a2582a3a0e66e6e86e3812dcb672a272'
assert task2(b'AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
print(task2('input.txt'))
