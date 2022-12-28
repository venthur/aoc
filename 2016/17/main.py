from hashlib import md5


def possible_directions(path):
    h = md5(path.encode()).hexdigest()
    directions = ''
    for d, i in zip('UDLR', range(4)):
        if h[i] in 'bcdef':
            directions += d
    return directions


def task1(passcode):
    stack = [(0, 0, passcode)]
    while True:
        x, y, path = stack.pop(0)
        if (x, y) == (3, 3):
            path = path[len(passcode):]
            return path
        for d in possible_directions(path):
            if d == 'U' and y-1 >= 0:
                stack.append((x, y-1, path+'U'))
            elif d == 'D' and y+1 <= 3:
                stack.append((x, y+1, path+'D'))
            elif d == 'L' and x-1 >= 0:
                stack.append((x-1, y, path+'L'))
            elif d == 'R' and x+1 <= 3:
                stack.append((x+1, y, path+'R'))


def task2(passcode):
    stack = [(0, 0, passcode)]
    longest = 0
    while True:
        try:
            x, y, path = stack.pop(0)
        except IndexError:
            break
        if (x, y) == (3, 3):
            path = path[len(passcode):]
            if len(path) > longest:
                longest = len(path)
            continue
        for d in possible_directions(path):
            if d == 'U' and y-1 >= 0:
                stack.append((x, y-1, path+'U'))
            elif d == 'D' and y+1 <= 3:
                stack.append((x, y+1, path+'D'))
            elif d == 'L' and x-1 >= 0:
                stack.append((x-1, y, path+'L'))
            elif d == 'R' and x+1 <= 3:
                stack.append((x+1, y, path+'R'))
    return longest


assert task1('ihgpwlah') == 'DDRRRD'
assert task1('kglvqrro') == 'DDUDRLRRUDRD'
assert task1('ulqzkmiv') == 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'
print(task1('pslxynzg'))

assert task2('ihgpwlah') == 370
assert task2('kglvqrro') == 492 
assert task2('ulqzkmiv') == 830
print(task2('pslxynzg'))



