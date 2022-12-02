with open('input.txt') as fh:
    data = fh.readlines()

score = 0
for line in data:
    a, b = line.strip().split()
    print(f'{a=} {b=}')

    b = {
        "X": "A",
        "Y": "B",
        "Z": "C",
    }[b]

    if b == "A": score += 1
    elif b == "B": score += 2
    elif b == "C": score += 3

    if a == b: score += 3
    elif b == "A" and a == "C": score += 6
    elif b == "B" and a == "A": score += 6
    elif b == "C" and a == "B": score += 6

print(score)


score = 0
for line in data:
    a, b = line.strip().split()
    print(f'{a=} {b=}')

    # lose
    if b == "X": score += 0
    # draw
    elif b == "Y": score += 3
    # win
    elif b == "Z": score += 6

    # rock
    if a == "A":
        if b == "X": score += 3
        elif b == "Y": score += 1
        elif b == "Z": score += 2
    # paper
    if a == "B":
        if b == "X": score += 1
        elif b == "Y": score += 2
        elif b == "Z": score += 3
    # scissors
    if a == "C":
        if b == "X": score += 2
        elif b == "Y": score += 3
        elif b == "Z": score += 1

print(score)
