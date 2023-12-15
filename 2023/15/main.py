def hash_(data):
    current_value = 0
    for d in data:
        current_value += ord(d)
        current_value *= 17
        current_value %= 256
    return current_value


def task1(fn):
    with open(fn) as fh:
        data = fh.read().strip().split(',')

    return sum(hash_(d) for d in data)


def task2(fn):
    with open(fn) as fh:
        data = fh.read().strip().split(',')

    boxes = [[] for _ in range(256)]
    for d in data:
        if '-' in d:
            label, _ = d.split('-')
            box = hash_(label)
            for i, lens in enumerate(boxes[box]):
                if lens.startswith(label + ' '):
                    boxes[box].pop(i)
                    break
        elif '=' in d:
            label, focal_length = d.split('=')
            box = hash_(label)
            for i, lens in enumerate(boxes[box]):
                if lens.startswith(label + ' '):
                    boxes[box][i] = label + ' ' + focal_length
                    break
            else:
                boxes[box].append(label + ' ' + focal_length)

    result = 0
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            focal_length = int(lens.split(' ')[1])
            result += (i+1) * (j+1) * focal_length
    return result


assert task1('test_input.txt') == 1320
print(task1('input.txt'))

assert task2('test_input.txt') == 145
print(task2('input.txt'))
