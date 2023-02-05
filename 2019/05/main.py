def task1(fn, in_):
    with open(fn) as fh:
        code = fh.read().strip().split(',')

    print(code)

    io = [str(in_), None]
    ptr = 0
    while True:
        # print(code, ptr)
        cmd = code[ptr]
        cmd = '0' * (5 - len(cmd)) + cmd
        match int(code[ptr][-2:]):
            case 1:
                a, b, c = [int(n) for n in code[ptr+1:ptr+1+3]]
                if cmd[0] == '0':
                    a = int(code[a])
                if cmd[1] == '0':
                    b = int(code[b])
                code[c] = str(a + b)
                ptr += 4
            case 2:
                a, b, c = [int(n) for n in code[ptr+1:ptr+1+3]]
                if cmd[0] == '0':
                    a = int(code[a])
                if cmd[1] == '0':
                    b = int(code[b])
                code[c] = str(a * b)
                ptr += 4
            case 3:
                c = code[ptr+1]
                code[int(c)] = str(io[0])
                ptr += 2
            case 4:
                c = int(code[ptr+1])
                if cmd[2] == '0':
                    c = int(code[c])
                io[1] = str(c)
                print(io)
                ptr += 2
            case 99:
                break

    return io[1]


print(task1('input.txt', 1))
