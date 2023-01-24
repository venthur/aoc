from itertools import count


def task1(iterations):

    recipes = [3, 7]
    pos = [0, 1]

    for i in range(iterations+10):
        #print(recipes, pos)
        v = recipes[pos[0]] + recipes[pos[1]]
        recipes += [int(d) for d in str(v)]

        pos[0] = (pos[0] + recipes[pos[0]] + 1) % len(recipes)
        pos[1] = (pos[1] + recipes[pos[1]] + 1) % len(recipes)

    return ''.join([str(n) for n in recipes[iterations:iterations+10]])


def task2(pattern):

    pattern = [int(n) for n in str(pattern)]
    l = len(pattern)

    recipes = [3, 7]
    pos = [0, 1]

    for i in count():
        v = recipes[pos[0]] + recipes[pos[1]]
        recipes += [int(d) for d in str(v)]

        pos[0] = (pos[0] + recipes[pos[0]] + 1) % len(recipes)
        pos[1] = (pos[1] + recipes[pos[1]] + 1) % len(recipes)

        if recipes[-l:] == pattern:
            return len(recipes) - l
        if recipes[-l-1:-1] == pattern:
            return len(recipes) - l - 1


assert task1(9) == '5158916779'
print(task1(894501))

assert task2(51589) == 9
assert task2(92510) == 18
assert task2(59414) == 2018
print(task2(894501))
