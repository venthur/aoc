import logging

logging.basicConfig(level=logging.NOTSET)


def task1(input_):
    with open(input_, 'rb') as fh:
        data = fh.read()

    data = iter(data)
    string_literals = 0
    memory = 0
    while True:
        try:
            c = chr(next(data))
        except StopIteration:
            break
        if c == '\n':
            continue
        logging.debug(c)
        memory += 1
        if c == '\\':
            c2 = chr(next(data))
            memory += 1
            if c2 in ('\\', '"'):
                string_literals += 1
            elif c2 == 'x':
                next(data)
                next(data)
                memory += 2
                string_literals += 1
        elif c == '"':
            pass
        else:
            string_literals += 1
    print(f'{string_literals=} {memory=}')
    return memory - string_literals


assert task1('test_input.txt') == 12
print(task1('input.txt'))
