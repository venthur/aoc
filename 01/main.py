with open('input.txt') as fh:
    data = fh.readlines()

food = []
elf = 1
calories = 0
for line in data:
    line = line.strip()
    if not line:
        food.append([elf, calories])
        calories = 0
        elf += 1
        continue
    calories += int(line)

food.sort(key=lambda x: x[1], reverse=True)
print(food[0][1])

print(food[0][1] + food[1][1] + food[2][1])
