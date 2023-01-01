from itertools import permutations


def task1(fn, code):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    code = [i for i in code]

    for line in lines:
        tokens = line.split()
        if line.startswith('swap position'):
            a = int(tokens[2])
            b = int(tokens[-1])
            ca = code[a]
            cb = code[b]
            code[a] = cb
            code[b] = ca
        if line.startswith("swap letter"):
            a = tokens[2]
            b = tokens[-1]
            ai = [i for i, _ in enumerate(code) if code[i] == a]
            bi = [i for i, _ in enumerate(code) if code[i] == b]
            for i in ai:
                code[i] = b
            for i in bi:
                code[i] = a
        if line.startswith("rotate right"):
            i = int(tokens[2])
            code = code[-i:] + code[:-i]
        if line.startswith("rotate left"):
            i = int(tokens[2])
            code = code[i:] + code[:i]
        if line.startswith("rotate based"):
            l = tokens[-1]
            i = code.index(l)
            if i >= 4:
                i += 1
            i += 1
            i %= len(code)
            code = code[-i:] + code[:-i]
        if line.startswith("reverse positions"):
            a = int(tokens[-3])
            b = int(tokens[-1])
            code = code[:a] + code[a:b+1][::-1] + code[b+1:]
        if line.startswith("move position"):
            i1 = int(tokens[2])
            i2 = int(tokens[-1])
            l = code.pop(i1)
            code.insert(i2, l)

    code =  "".join(code)
    return code


def task2(fn, code):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    def scramble(code):

        code = [i for i in code]

        for line in lines:
            tokens = line.split()
            if line.startswith('swap position'):
                a = int(tokens[2])
                b = int(tokens[-1])
                ca = code[a]
                cb = code[b]
                code[a] = cb
                code[b] = ca
            if line.startswith("swap letter"):
                a = tokens[2]
                b = tokens[-1]
                ai = [i for i, _ in enumerate(code) if code[i] == a]
                bi = [i for i, _ in enumerate(code) if code[i] == b]
                for i in ai:
                    code[i] = b
                for i in bi:
                    code[i] = a
            if line.startswith("rotate right"):
                i = int(tokens[2])
                code = code[-i:] + code[:-i]
            if line.startswith("rotate left"):
                i = int(tokens[2])
                code = code[i:] + code[:i]
            if line.startswith("rotate based"):
                l = tokens[-1]
                i = code.index(l)
                if i >= 4:
                    i += 1
                i += 1
                i %= len(code)
                code = code[-i:] + code[:-i]
            if line.startswith("reverse positions"):
                a = int(tokens[-3])
                b = int(tokens[-1])
                code = code[:a] + code[a:b+1][::-1] + code[b+1:]
            if line.startswith("move position"):
                i1 = int(tokens[2])
                i2 = int(tokens[-1])
                l = code.pop(i1)
                code.insert(i2, l)

        return "".join(code)

    for p in permutations(code):
        if scramble(p) == code:
            return "".join(p)




assert task1("test_input.txt", "abcde") == "decab"
print(task1("input.txt", "abcdefgh"))

print(task2("input.txt", "fbgdceah"))


