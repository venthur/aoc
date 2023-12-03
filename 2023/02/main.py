from math import prod


def task1(fn):
    ALLOWED = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    with open(fn) as fh:
        s = 0
        for line in fh.read().splitlines():
            valid = True
            game, rest = line.split(': ')
            game_id = int(game.split()[-1])
            reveals = rest.split('; ')
            for reveal in reveals:
                for cubes in reveal.split(', '):
                    n, color = cubes.split()
                    if int(n) > ALLOWED[color]:
                        valid = False
                        break
            if valid:
                s += game_id
    return s


def task2(fn):
    with open(fn) as fh:
        s = 0
        for line in fh.read().splitlines():
            _, rest = line.split(': ')
            reveals = rest.split('; ')
            colors = {}
            for reveal in reveals:
                for cubes in reveal.split(', '):
                    n, color = cubes.split()
                    colors[color] = max(colors.get(color, 0), int(n))
            s += prod(colors.values())
    return s


assert task1('test_input.txt') == 8
print(task1('input.txt'))

assert task2('test_input.txt') == 2286
print(task2('input.txt'))
