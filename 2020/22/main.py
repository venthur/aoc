from collections import deque


def task1(fn):
    with open(fn) as fh:
        decks = fh.read().split('\n\n')

    deck_a = deque([int(n) for n in decks[0].splitlines()[1:]])
    deck_b = deque([int(n) for n in decks[1].splitlines()[1:]])

    while deck_a and deck_b:
        a = deck_a.popleft()
        b = deck_b.popleft()

        if a > b:
            deck_a.append(a)
            deck_a.append(b)
        else:
            deck_b.append(b)
            deck_b.append(a)

    winner = deck_a if deck_a else deck_b
    score = 0
    i = 0
    while winner:
        i += 1
        score += i * winner.pop()

    return score


def task2(fn):
    with open(fn) as fh:
        decks = fh.read().split('\n\n')

    deck_a = deque([int(n) for n in decks[0].splitlines()[1:]])
    deck_b = deque([int(n) for n in decks[1].splitlines()[1:]])

    def recursive_combat(deck_a, deck_b):

        seen = set()
        while deck_a and deck_b:

            frozen = (tuple(deck_a), tuple(deck_b))
            if frozen in seen:
                # player 1 wins
                return 0, deck_a, deck_b
            seen.add(frozen)

            a = deck_a.popleft()
            b = deck_b.popleft()

            if a <= len(deck_a) and b <= len(deck_b):
                winner, _, _ = recursive_combat(
                    deque(list(deck_a)[:a]), deque(list(deck_b)[:b])
                )
            else:
                winner = 0 if a > b else 1

            if winner == 0:
                deck_a.append(a)
                deck_a.append(b)
            else:
                deck_b.append(b)
                deck_b.append(a)

        winner = 0 if deck_a else 1
        return winner, deck_a, deck_b

    winner, deck_a, deck_b = recursive_combat(deck_a, deck_b)

    winner = deck_a if winner == 0 else deck_b
    score = 0
    i = 0
    while winner:
        i += 1
        score += i * winner.pop()

    return score


assert task1('test_input0.txt') == 306
print(task1('input.txt'))

assert task2('test_input0.txt') == 291
print(task2('input.txt'))
