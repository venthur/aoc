def read_input(fn):
    with open(fn) as fh:
        return [int(line.strip()) for line in fh]


def compute_next(value):
    ans = value ^ (value * 64)
    ans %= 16777216

    ans = ans ^ (ans // 32)
    ans %= 16777216

    ans = ans ^ (ans * 2048)
    ans %= 16777216

    return ans


def task1(fn):
    numbers = read_input(fn)
    result = []
    for number in numbers:
        for i in range(2000):
            number = compute_next(number)
        result.append(number)
    return sum(result)


def task2(fn):
    numbers = read_input(fn)
    prices, diffs = [], []
    for number in numbers:
        p = [number % 10]
        d = []
        for i in range(2000):
            number = compute_next(number)
            p.append(number % 10)
            d.append(p[-1] - p[-2])
        p = p[1:]
        prices.append(p)
        diffs.append(d)

    pattern2value = [{} for i in range(len(prices))]
    for i in range(len(prices)):
        for j in range(len(diffs[i])-3):
            pattern = tuple(diffs[i][j:j+4])
            if pattern in pattern2value[i]:
                continue
            pattern2value[i][pattern] = prices[i][j+3]

    seen = set()
    best = 0
    for i in range(len(pattern2value)):
        for pattern, value in pattern2value[i].items():
            if pattern in seen:
                continue
            seen.add(pattern)
            current = value
            for j in range(len(pattern2value)):
                if i == j:
                    continue
                current += pattern2value[j].get(pattern, 0)
            if current > best:
                best = current
    return best


assert task1('test_input.txt') == 37327623
print(task1('input.txt'))

assert task2('test_input2.txt') == 23
print(task2('input.txt'))
