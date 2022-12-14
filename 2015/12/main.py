import json


def task1(input_):
    with open(input_) as fh:
        data = fh.read()
        data = json.loads(data)

    def sum_(d):
        if isinstance(d, int):
            return d
        elif isinstance(d, str):
            return 0
        elif isinstance(d, dict):
            s = 0
            for k, v in d.items():
                s += sum_(v)
            return s
        elif isinstance(d, list):
            s = 0
            for i in d:
                s += sum_(i)
            return s
        else:
            print(type(d))

    return sum_(data)


def task2(input_):
    with open(input_) as fh:
        data = fh.read()
        data = json.loads(data)

    def sum_(d):
        if isinstance(d, int):
            return d
        elif isinstance(d, str):
            return 0
        elif isinstance(d, dict):
            if 'red' in d.values():
                return 0
            s = 0
            for k, v in d.items():
                s += sum_(v)
            return s
        elif isinstance(d, list):
            s = 0
            for i in d:
                s += sum_(i)
            return s
        else:
            print(type(d))

    return sum_(data)


print(task1('input.txt'))

print(task2('input.txt'))
