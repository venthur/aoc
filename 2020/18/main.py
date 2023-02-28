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


def task2(fn):
    with open(fn) as fh:
        data = fh.read()
        data = data.replace('(', '( ')
        data = data.replace(')', ' )')
        lines = data.splitlines()

    def compute(tokens):

        def prio(t):
            if t == '+':
                return 20
            if t == '*':
                return 10

        output_queue = []
        operator_stack = []
        while tokens:
            t = tokens.pop(0)
            if t.isnumeric():
                output_queue.insert(0, int(t))
            if t in "+*":
                while (
                    operator_stack and
                    operator_stack[-1] != '(' and
                    prio(operator_stack[-1]) >= prio(t)
                ):
                    output_queue.insert(0, operator_stack.pop())
                operator_stack.append(t)
            if t == '(':
                operator_stack.append(t)
            if t == ')':
                while (
                    operator_stack and
                    operator_stack[-1] != '('
                ):
                    output_queue.insert(0, operator_stack.pop())
                operator_stack.pop()

        while operator_stack:
            output_queue.insert(0, operator_stack.pop())

        # calculate
        op_stack = []
        while len(output_queue) > 0:
            t = output_queue.pop()
            if isinstance(t, int):
                op_stack.append(t)
            else:
                a = op_stack.pop()
                b = op_stack.pop()
                if t == '+':
                    r = a + b
                elif t == '*':
                    r = a * b
                op_stack.append(r)

        return op_stack.pop()

    s = 0
    for line in lines:
        tokens = line.split()
        s += compute(tokens)

    return s


print(task1('input.txt'))

print(task2('input.txt'))
