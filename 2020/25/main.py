def task1(fn):
    with open(fn) as fh:
        card_pk, door_pk = [int(n) for n in fh.read().splitlines()]

    print(card_pk, door_pk)

    value, loop_size = 1, 0
    while value != card_pk:
        value *= 7
        value %= 20201227
        loop_size += 1

    return pow(door_pk, loop_size, 20201227)


print(task1('input.txt'))
