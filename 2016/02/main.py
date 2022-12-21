def task1(fn):

    with open(fn) as fh:
        lines = fh.read().splitlines()

    pos = 5
    password = []
    for line in lines:
        for char in line:
            if (
                (char == "U" and pos in (1, 2, 3))
                or (char == "D" and pos in (7, 8, 9))
                or (char == "L" and pos in (1, 4, 7))
                or (char == "R" and pos in (3, 6, 9))
            ):
                pass
            elif char == "U":
                pos -= 3
            elif char == "D":
                pos += 3
            elif char == "L":
                pos -= 1
            elif char == "R":
                pos += 1
        password.append(str(pos))

    return ''.join(password)


def task2(fn):

    with open(fn) as fh:
        lines = fh.read().splitlines()

    up = {
        '3': '1',
        '6': '2', '7': '3', '8': '4',
        'A': '6', 'B': '7', 'C': '8',
        'D': 'B',
    }
    down = {
        '1': '3',
        '2': '6', '3': '7', '4': '8',
        '6': 'A', '7': 'B', '8': 'C',
        'B': 'D',
    }
    left = {
        '3': '2', '4': '3',
        '6': '5', '7': '6', '8': '7', '9': '8',
        'B': 'A', 'C': 'B',
    }
    right = {
        '2': '3', '3': '4',
        '5': '6', '6': '7', '7': '8', '8': '9',
        'A': 'B', 'B': 'C',
    }

    pos = "5"
    password = []
    for line in lines:
        for char in line:
            if (
                (char == "U" and pos in ("5", "2", "1", "4", "9"))
                or (char == "D" and pos in ("5", "A", "D", "C", "9"))
                or (char == "L" and pos in ("1", "2", "5", "A", "D"))
                or (char == "R" and pos in ("1", "4", "9", "C", "D"))
            ):
                pass
            elif char == "U":
                pos = up[pos]
            elif char == "D":
                pos = down[pos]
            elif char == "L":
                pos = left[pos]
            elif char == "R":
                pos = right[pos]
        password.append(str(pos))

    return ''.join(password)

assert task1("test_input.txt") == "1985"
print(task1("input.txt"))

assert task2("test_input.txt") == "5DB3"
print(task2("input.txt"))
