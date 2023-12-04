def task1(fn):
    s = 0
    with open(fn) as fh:
        for line in fh.read().splitlines():
            _, cards = line.split(': ')
            winning, cards = cards.split(' | ')
            winning = set(winning.split())
            cards = set(cards.split())
            matches = len(winning.intersection(cards))
            if matches > 0:
                s += 2 ** (matches-1)
    return s


def task2(fn):
    card = []  # amount, matches
    with open(fn) as fh:
        for i, line in enumerate(fh.read().splitlines()):
            card_id, cards = line.split(': ')
            winning, cards = cards.split(' | ')
            winning = set(winning.split())
            cards = set(cards.split())
            matching = len(winning.intersection(cards))
            card.append([1, matching])

    for i, (amount, matching) in enumerate(card):
        if matching > 0:
            for j in range(matching):
                card[i+j+1][0] += amount

    return sum([amount for amount, _ in card])


assert task1('test_input.txt') == 13
print(task1('input.txt'))

assert task2('test_input.txt') == 30
print(task2('input.txt'))
