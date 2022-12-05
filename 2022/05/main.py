test = """\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""".splitlines()


with open('input.txt') as fh:
    input_ = fh.read().splitlines()


def parse_input(input_):
    # separate stacks from orders first
    i = input_.index('')
    stacks_input = input_[:i]
    orders_input = input_[i+1:]

    # get the stacks
    last = stacks_input.pop()
    n_stacks = int(last.split()[-1])
    stacks = [[] for i in range(n_stacks)]
    for i in range(n_stacks):
        for j in stacks_input[::-1]:
            pos = i*4 + 1
            item = j[pos].strip()
            if item:
                stacks[i].append(item)

    # get the orders (n, from, to)
    orders = []
    for order in orders_input:
        order = order.replace('move', '').replace('from', '').replace('to', '')
        orders.append([int(i) for i in order.split()])

    return stacks, orders


def task1(input_):
    stacks, orders = parse_input(input_)
    for n, from_, to in orders:
        for _ in range(n):
            stacks[to-1].append(stacks[from_-1].pop())
    tops = ''.join([i.pop() for i in stacks])
    print(tops)


def task2(input_):
    stacks, orders = parse_input(input_)
    for n, from_, to in orders:
        buffer = []
        for _ in range(n):
            buffer.append(stacks[from_-1].pop())
        buffer = buffer[::-1]
        stacks[to-1].extend(buffer)
    tops = ''.join([i.pop() for i in stacks])
    print(tops)


#task1(test)  # c m z
task1(input_)

#task2(test)  # m c d
task2(input_)
