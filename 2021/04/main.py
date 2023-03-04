from copy import deepcopy


def task1(fn):
    with open(fn) as fh:
        numbers, boards = fh.read().split('\n\n', 1)

    numbers = [int(n) for n in numbers.split(',')]
    boards = [
        [
            [int(n) for n in line.split()]
            for line
            in board.splitlines()
        ]
        for board
        in boards.split('\n\n')
    ]

    boards_set = []
    for board in boards:
        board_set = []
        for line in board:
            row = set(tuple(line))
            board_set.append(row)
        for col in zip(*board):
            col = set(tuple(col))
            board_set.append(col)
        boards_set.append(board_set)

    n_seen = set()
    for n in numbers:
        n_seen.add(n)
        for board in boards_set:
            for row_or_col in board:
                if row_or_col <= n_seen:
                    # bingo!
                    n_board = set()
                    for row_or_col in board:
                        n_board.update(row_or_col)
                    unmarked = n_board - n_seen
                    return sum(unmarked) * n


def task2(fn):
    with open(fn) as fh:
        numbers, boards = fh.read().split('\n\n', 1)

    numbers = [int(n) for n in numbers.split(',')]
    boards = [
        [
            [int(n) for n in line.split()]
            for line
            in board.splitlines()
        ]
        for board
        in boards.split('\n\n')
    ]

    boards_set = []
    for board in boards:
        board_set = []
        for line in board:
            row = set(tuple(line))
            board_set.append(row)
        for col in zip(*board):
            col = set(tuple(col))
            board_set.append(col)
        boards_set.append(board_set)

    ret = None
    n_seen = set()
    for n in numbers:
        n_seen.add(n)
        boards_set_bak = deepcopy(boards_set)
        for board in boards_set_bak:
            for row_or_col in board:
                if row_or_col <= n_seen:
                    # bingo!
                    n_board = set()
                    for row_or_col in board:
                        n_board.update(row_or_col)
                    unmarked = n_board - n_seen
                    ret = sum(unmarked) * n
                    boards_set.remove(board)
                    break

    return ret


assert task1('test_input0.txt') == 4512
print(task1('input.txt'))

assert task2('test_input0.txt') == 1924
print(task2('input.txt'))
