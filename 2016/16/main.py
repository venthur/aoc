def task1(seed, size):
    a = seed[:]
    while len(a) < size:
        b = a[::-1]
        b = ''.join(['0' if i == '1' else '1' for i in b])
        a += '0' + b

    checksum = ''
    buffer = a[:size]
    while True:
        for i in range(len(buffer) // 2):
            x, y = buffer[2*i], buffer[2*i+1]
            if x == y:
                checksum += '1'
            else:
                checksum += '0'
        if len(checksum) % 2 != 0:
            return checksum
        else:
            buffer = checksum[:]
            checksum = ''


assert task1('10000', 20) == '01100'
print(task1('01110110101001000', 272))

print(task1('01110110101001000', 35651584))
