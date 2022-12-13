def transform(input_):
    result = ""
    it = iter(input_)
    c = next(it)
    while True:
        count = 1
        while True:
            try:
                ci = next(it)
            except StopIteration:
                result += str(count) + c
                return result
            if ci == c:
                count += 1
            else:
                result += str(count) + c
                c = ci
                break


def task1(input_, iterations):
    for i in range(iterations):
        input_ = transform(input_)
    return input_


assert task1('1', 1) == '11'
assert task1('1', 5) == '312211'

print(len(task1('1113222113', 40)))
print(len(task1('1113222113', 50)))
