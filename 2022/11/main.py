from math import floor

test_input = '''\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
'''.splitlines()


with open('input.txt') as fh:
    input_ = fh.read().splitlines()


class Monkey:

    def __init__(self, lines):
        for line in lines:
            line = line.strip()
            if line.startswith('Monkey'):
                self.id = int(line.split()[-1][:-1])
            if line.startswith('Starting items'):
                _, items = line.split(':')
                items = [int(i) for i in items.split(',')]
                self.worry_levels = items
            if line.startswith('Operation'):
                line = line.split(':')[-1].split('=')[-1].strip()
                self.op = line
            if line.startswith('Test'):
                self.test_value = int(line.split('by')[-1])
            if line.startswith('If true:'):
                self.monkey_true = int(line.split('monkey')[-1])
            if line.startswith('If false:'):
                self.monkey_false = int(line.split('monkey')[-1])
        self.inspections = 0

    def __str__(self):
        s = f'Monkey {self.id}: {self.worry_levels}'
        #s += f'\n  Operation: {self.op}'
        #s += f'\n  Test Value: {self.test_value}'
        #s += f'\n  if True: {self.monkey_true}'
        #s += f'\n  if False: {self.monkey_false}'
        return s

    def process_items(self, monkeys, worry_mod=None):
        while True:
            try:
                worry = self.worry_levels.pop(0)
            except IndexError:
                break
            old = worry
            worry = eval(self.op)
            if worry_mod is None:
                worry = floor(worry / 3)
            else:
                worry %= worry_mod
            if worry % self.test_value == 0:
                monkeys[self.monkey_true].catch_item(worry)
            else:
                monkeys[self.monkey_false].catch_item(worry)
            self.inspections += 1

    def catch_item(self, value):
        self.worry_levels.append(value)


def task1(input_):
    monkeys = []
    txt = []
    for line in input_:
        if line:
            txt.append(line)
        else:
            monkeys.append(Monkey(txt))
            txt = []
    # last monkey
    monkeys.append(Monkey(txt))

    for round_ in range(20):
        for m in monkeys:
            m.process_items(monkeys)

    most_active = sorted(monkeys, key=lambda x: x.inspections)[-2:]
    return most_active[0].inspections * most_active[1].inspections


def task2(input_):
    monkeys = []
    txt = []
    for line in input_:
        if line:
            txt.append(line)
        else:
            monkeys.append(Monkey(txt))
            txt = []
    # last monkey
    monkeys.append(Monkey(txt))

    mod = 1
    for m in monkeys:
        mod *= m.test_value

    for round_ in range(10000):
        for m in monkeys:
            m.process_items(monkeys, worry_mod=mod)

    most_active = sorted(monkeys, key=lambda x: x.inspections)[-2:]
    return most_active[0].inspections * most_active[1].inspections



assert task1(test_input) == 10605
print(task1(input_))

assert task2(test_input) == 2713310158
print(task2(input_))
