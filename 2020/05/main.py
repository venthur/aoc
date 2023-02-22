def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    ids = []
    for line in lines:
        line = line.replace('B', '1')
        line = line.replace('F', '0')
        line = line.replace('R', '1')
        line = line.replace('L', '0')
        row = int(line[:7], base=2)
        col = int(line[7:], base=2)
        v = row * 8 + col
        ids.append(v)

    # pt 1
    print(max(ids))

    # pt 2
    ids.sort()
    for i in range(len(ids)-1):
        a, b = ids[i], ids[i+1]
        if a + 1 != b:
            print(a+1)
            return


task1('input.txt')
