def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    tmp = dict()
    foods = []
    for line in lines:
        line = line.replace('(', '')
        line = line.replace(')', '')
        line = line.replace(',', '')
        ingrediens, allergens = line.split('contains')
        foods.append([set(ingrediens.split()), set(allergens.split())])

    print(foods)
    allergens = dict()
    for ing, algs in foods:
        for a in algs:
            if a not in allergens:
                allergens[a] = ing.copy()
            else:
                allergens[a].intersection_update(ing)
    print(allergens)


assert task1('test_input0.txt') == 5
print(task1('input.txt'))
