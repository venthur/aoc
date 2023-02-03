def task1(fn):
    with open(fn) as fh:
        data = fh.read().strip()

    code = [int(n) for n in data.split(',')]
    code[1] = 12
    code[2] = 2

    ptr = 0
    while True:
        #print(code, ptr)
        match code[ptr]:
            case 1:
                a, b, c = code[ptr+1:ptr+1+3]
                code[c] = code[a] + code[b]
                ptr += 4
            case 2:
                a, b, c = code[ptr+1:ptr+1+3]
                code[c] = code[a] * code[b]
                ptr += 4
            case 99:
                break

    return code[0]


def task2(fn):
    for noun in range(100):
        for verb in range(100):

            with open(fn) as fh:
                data = fh.read().strip()

            code = [int(n) for n in data.split(',')]
            code[1] = noun
            code[2] = verb

            ptr = 0
            while True:
                #print(code, ptr)
                match code[ptr]:
                    case 1:
                        a, b, c = code[ptr+1:ptr+1+3]
                        code[c] = code[a] + code[b]
                        ptr += 4
                    case 2:
                        a, b, c = code[ptr+1:ptr+1+3]
                        code[c] = code[a] * code[b]
                        ptr += 4
                    case 99:
                        break

            if code[0] == 19690720:
                return 100 * noun + verb


print(task1('input.txt'))

print(task2('input.txt'))
