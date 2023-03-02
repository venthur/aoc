def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    foods = []
    for line in lines:
        line = line.replace('(', '')
        line = line.replace(')', '')
        line = line.replace(',', '')
        ingrediens, allergens = line.split('contains')
        foods.append([set(ingrediens.split()), set(allergens.split())])

    allergens = dict()
    for ing, algs in foods:
        for a in algs:
            if a not in allergens:
                allergens[a] = ing.copy()
            else:
                allergens[a].intersection_update(ing)

    while not all(len(f) == 1 for f in allergens.values()):
        for k, v in allergens.items():
            if len(v) == 1:
                for ki, vi in allergens.items():
                    if ki == k:
                        continue
                    vi.difference_update(v)

    count = 0
    afoods = set()
    for k in allergens.values():
        afoods.update(k)
    for ing, _ in foods:
        for i in ing:
            if i not in afoods:
                count += 1

    pt1 = count

    l = [(k, v.pop())for k, v in allergens.items()]
    l.sort()
    pt2 = ','.join([l[1] for l in l])

    return pt1, pt2


assert task1('test_input0.txt') == (5, 'mxmxvkd,sqjhc,fvjkl')
print(task1('input.txt'))
