def read(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    data = []
    for line in lines:
        data.append([int(i) for i in line.split()])

    return data


def task1(fn):
    data = read(fn)

    valid = 0
    for a, b, c in data:
        if a + b <= c or b + c <= a or c + a <= b:
            pass
        else:
            valid += 1

    return valid


def task2(fn):
    data = read(fn)

    valid = 0
    for i in range(len(data)//3):
        line1 = data[i*3+0]
        line2 = data[i*3+1]
        line3 = data[i*3+2]
        for j in range(3):
            a = line1[j]
            b = line2[j]
            c = line3[j]
            if a + b <= c or b + c <= a or c + a <= b:
                pass
            else:
                valid += 1

    return valid


print(task1('input.txt'))
print(task2('input.txt'))
