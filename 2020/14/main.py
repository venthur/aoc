from copy import deepcopy


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    mem = dict()
    for line in lines:
        if line.startswith('mask'):
            mask_str = line.split()[-1]
            mask_or = int(mask_str.replace('X', '0'), 2)
            mask_and = int(mask_str.replace('X', '1'), 2)
        else:
            mem_str, n = line.split(' = ')
            mem_str = mem_str[4:-1]
            addr = int(mem_str)
            n = int(n)

            n |= mask_or
            n &= mask_and

            mem[addr] = n

    return sum(mem.values())


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    mem = dict()
    for line in lines:
        if line.startswith('mask'):
            mask_str = line.split()[-1]
            mask_or = int(mask_str.replace('X', '0'), 2)
            floating_pos = [len(mask_str)-i-1 for i, c in enumerate(mask_str) if c == 'X']
            todo = [[[i, 0] for i in floating_pos]]
            for i, _ in enumerate(floating_pos):
                for td in deepcopy(todo):
                    td2 = td[:]
                    td2[i][-1] = 1
                    todo.append(td2)

        else:
            mem_str, n = line.split(' = ')
            mem_str = mem_str[4:-1]
            addr = int(mem_str)
            n = int(n)

            addr |= mask_or
            for td in todo:
                addr2 = addr
                for pos, val in td:
                    if val == 0:
                        addr2 &= ~(1 << pos)
                    elif val == 1:
                        addr2 |= (1 << pos)
                mem[addr2] = n

    return sum(mem.values())


assert task1('test_input0.txt') == 165
print(task1('input.txt'))

assert task2('test_input1.txt') == 208
print(task2('input.txt'))
