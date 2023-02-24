def task1(numbers, rounds):
    numbers = list(numbers)
    for i in range(len(numbers), rounds):
        if i % 1000 == 0:
            print(f'{rounds-i:>10}', end='\r')
        n = numbers[:i].count(numbers[i-1])
        if n == 1:
            numbers.append(0)
        else:
            for j, m in enumerate(reversed(numbers)):
                if j == 0:
                    continue
                if m == numbers[i-1]:
                    numbers.append(j)
                    break
    print()
    return numbers[-1]


assert task1((0, 3, 6), 2020) == 436
assert task1((1, 3, 2), 2020) == 1
print(task1((9, 3, 1, 0, 8, 4), 2020))

print(task1((9, 3, 1, 0, 8, 4), 30000000))
