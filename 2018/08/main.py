def task1(fn):
    with open(fn) as fh:
        data = [int(i) for i in fh.read().strip().split()]

    def parse(data):
        children, meta = data[:2]
        data = data[2:]

        totals = 0
        for i in range(children):
            total, data = parse(data)
            totals += total

        totals += sum(data[:meta])

        return totals, data[meta:]

    return parse(data)[0]


def task2(fn):
    with open(fn) as fh:
        data = [int(i) for i in fh.read().strip().split()]

    def parse(data):
        children, meta = data[:2]
        data = data[2:]
        scores = []

        totals = 0
        for i in range(children):
            total, score, data = parse(data)
            totals += total
            scores.append(score)

        if children == 0:
            return totals, sum(data[:meta]), data[meta:]
        else:
            return (
                totals,
                sum(
                    scores[k-1]
                    for k in data[:meta]
                    if k > 0 and k <= len(scores)
                ),
                data[meta:]
            )

    return parse(data)[1]


assert task1('test_input.txt') == 138
print(task1('input.txt'))

assert task2('test_input.txt') == 66
print(task2('input.txt'))
