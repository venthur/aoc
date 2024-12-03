import re

mul_exp = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
do_exp = re.compile(r'do\(\)')
dont_exp = re.compile(r"don't\(\)")


def task1(fn):
    with open(fn) as fh:
        data = fh.read()
        s = 0
        for match in mul_exp.finditer(data):
            s += int(match.group(1)) * int(match.group(2))
    return s


def task2(fn):
    with open(fn) as fh:
        data = fh.read()

        # toogle for multiplications, initially True
        do = True
        s = 0
        for i in range(len(data)):
            for exp in mul_exp, do_exp, dont_exp:
                if match := exp.match(data[i:]):
                    if exp == do_exp:
                        do = True
                    elif exp == dont_exp:
                        do = False
                    elif exp == mul_exp and do:
                        s += int(match.group(1)) * int(match.group(2))
                    elif exp == mul_exp and not do:
                        pass
    return s


assert task1('test_input.txt') == 161
print(task1('input.txt'))

assert task2('test_input2.txt') == 48
print(task2('input.txt'))
