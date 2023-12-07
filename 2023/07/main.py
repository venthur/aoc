from collections import Counter


def value(hand):
    SHIFT = 4
    value = 0

    counts = Counter(hand)
    # five of a kind
    if len(counts) == 1:
        value += 7
        value <<= SHIFT
    # four of a kind
    elif sorted(counts.values()) == [1, 4]:
        value += 6
        value <<= SHIFT
    # full house
    elif sorted(counts.values()) == [2, 3]:
        value += 5
        value <<= SHIFT
    # three of a kind
    elif sorted(counts.values()) == [1, 1, 3]:
        value += 4
        value <<= SHIFT
    # two pairs
    elif sorted(counts.values()) == [1, 2, 2]:
        value += 3
        value <<= SHIFT
    # one pair
    elif sorted(counts.values()) == [1, 1, 1, 2]:
        value += 2
        value <<= SHIFT
    # high card
    elif sorted(counts.values()) == [1, 1, 1, 1, 1]:
        value += 1
        value <<= SHIFT

    for card in hand:
        if card == 'A':
            value += 14
        elif card == 'K':
            value += 13
        elif card == 'Q':
            value += 12
        elif card == 'J':
            value += 11
        elif card == 'T':
            value += 10
        else:
            value += int(card)
        value <<= SHIFT

    return value


def value2(hand):
    SHIFT = 4
    value = 0

    counts = Counter(hand)
    if 'J' in hand:
        if counts.most_common(1)[0][1] >= 1:
            # we have at least a pair
            if counts.most_common(1)[0][0] != 'J':
                # we at least a pair that is not JJ
                hand2 = hand.replace(
                    'J',
                    counts.most_common(1)[0][0],
                )
                counts = Counter(hand2)
            else:
                if len(counts) == 1:
                    # we have only JJ
                    hand2 = hand.replace(
                        'J',
                        'A',
                    )
                    counts = Counter(hand2)
                # we have at least a pair of JJ
                elif len(counts) >= 2 and counts.most_common(2)[1][1] >= 1:
                    # ... and at least another pair
                    hand2 = hand.replace(
                        'J',
                        counts.most_common(2)[1][0],
                    )
                    counts = Counter(hand2)
                else:
                    # ... and no other pair
                    for candidate in 'AKQT98765432':
                        if candidate in hand:
                            hand2 = hand.replace(
                                'J',
                                candidate,
                            )
                            counts = Counter(hand2)
                            break
        # all cards are unique, so upgrade the most valuable card
        else:
            for candidate in 'AKQT98765432':
                if candidate in hand:
                    hand2 = hand.replace(
                        'J',
                        candidate,
                    )
                    counts = Counter(hand2)
                    break

    # five of a kind
    if len(counts) == 1:
        value += 7
        value <<= SHIFT
    # four of a kind
    elif sorted(counts.values()) == [1, 4]:
        value += 6
        value <<= SHIFT
    # full house
    elif sorted(counts.values()) == [2, 3]:
        value += 5
        value <<= SHIFT
    # three of a kind
    elif sorted(counts.values()) == [1, 1, 3]:
        value += 4
        value <<= SHIFT
    # two pairs
    elif sorted(counts.values()) == [1, 2, 2]:
        value += 3
        value <<= SHIFT
    # one pair
    elif sorted(counts.values()) == [1, 1, 1, 2]:
        value += 2
        value <<= SHIFT
    # high card
    elif sorted(counts.values()) == [1, 1, 1, 1, 1]:
        value += 1
        value <<= SHIFT

    for card in hand:
        if card == 'A':
            value += 14
        elif card == 'K':
            value += 13
        elif card == 'Q':
            value += 12
        elif card == 'J':
            value += 1
        elif card == 'T':
            value += 10
        else:
            value += int(card)
        value <<= SHIFT

    return value


def task1(fn):
    hands = []
    with open(fn) as fh:
        for line in fh.read().splitlines():
            hand, bid = line.split()
            hands.append((hand, bid))

    hands.sort(key=lambda x: value(x[0]))
    result = 0
    for pos, (hand, bid) in enumerate(hands):
        result += (pos + 1) * int(bid)
    return result


def task2(fn):
    hands = []
    with open(fn) as fh:
        for line in fh.read().splitlines():
            hand, bid = line.split()
            hands.append((hand, bid))

    hands.sort(key=lambda x: value2(x[0]))
    result = 0
    for pos, (hand, bid) in enumerate(hands):
        result += (pos + 1) * int(bid)
    return result


assert task1('test_input.txt') == 6440
print(task1('input.txt'))

assert task2('test_input.txt') == 5905
print(task2('input.txt'))
