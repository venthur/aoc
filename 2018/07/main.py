def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    rules = [(line.split()[1], line.split()[-3]) for line in lines]

    order = []
    for first, second in rules:
        if not order:
            order = [first, second]
        elif first in order and second not in order:
            for i in range(order.index(first), len(order)):
                if order[i] > second:
                    order.insert(i, second)
                    break
            else:
                order.append(second)
        elif second in order and first not in order:
            for i in range(0, order.index(second)):
                if order[i] > second:
                    order.insert(i, first)
                    break
            else:
                order.insert(i+1, first)
        elif first in order and second in order:
            if order.index(first) < order.index(second):
                pass
            else:
                order.remove(first)
                order.insert(order.index(second), first)
        else:
            order.insert(0, first)
            order.insert(1, second)

    return ''.join(order)

assert task1('test_input.txt') == 'CABDFE'
print(task1('input.txt'))


