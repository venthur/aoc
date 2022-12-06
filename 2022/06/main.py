test_cases = [
    ['bvwbjplbgvbhsrlpgdmjqwftvncz', 5],
    ['nppdvjthqldpwncqszvftbrmjlhg', 6],
    ['nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10],
    ['zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11],
]

test_cases2 = [
    ['mjqjpqmgbljsphdztnvjfqwrcgsmlb', 19],
    ['bvwbjplbgvbhsrlpgdmjqwftvncz', 23],
    ['nppdvjthqldpwncqszvftbrmjlhg', 23],
    ['nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29],
    ['zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26],
]

with open('input.txt') as fh:
    input_ = fh.read()


def task1(input_):
    for i, _ in enumerate(input_[3:]):
        s = set()
        for j in range(4):
            s.add(input_[i+3-j])
            if len(s) == 4:
                return i+4


def task2(input_):
    for i, _ in enumerate(input_[13:]):
        s = set()
        for j in range(14):
            s.add(input_[i+13-j])
            if len(s) == 14:
                return i+14


for i, o in test_cases:
    assert o == task1(i)

print(task1(input_))


for i, o in test_cases2:
    assert o == task2(i)

print(task2(input_))
