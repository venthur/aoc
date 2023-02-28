def task1(fn):
    with open(fn) as fh:
        data = fh.read()
        data = data.replace('(', '( ')
        data = data.replace(')', ' )')
        lines = data.splitlines()

    def compute(tokens):
        ans, op = None, None
        while tokens:
            t = tokens.pop(0)
            if t == ')':
                return ans
            if t == '(':
                if ans is None:
                    ans = compute(tokens)
                else:
                    if op == '*':
                        ans *= compute(tokens)
                    elif op == '+':
                        ans += compute(tokens)
            if t in '+*':
                op = t
            if t.isnumeric():
                t = int(t)
                if ans is None:
                    ans = t
                else:
                    if op == '*':
                        ans *= t
                    elif op == '+':
                        ans += t
        return ans

    s = 0
    for line in lines:
        tokens = line.split()
        s += compute(tokens)

    return s


print(task1('input.txt'))
