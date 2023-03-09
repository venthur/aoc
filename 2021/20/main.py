def task1(fn, steps):
    with open(fn) as fh:
        code, imagestr = fh.read().split('\n\n')

    code = code.strip()

    img = dict()
    for y, line in enumerate(imagestr.splitlines()):
        for x, char in enumerate(line):
            img[x, y] = char

    bg = '.'
    for i in range(steps):

        xs, ys = zip(*img)
        img_bak = img.copy()
        for yi in range(min(ys)-1, max(ys)+2):
            for xi in range(min(xs)-1, max(xs)+2):
                v = 0
                for yii in yi-1, yi, yi+1:
                    for xii in xi-1, xi, xi+1:
                        v <<= 1
                        v += 1 if img_bak.get((xii, yii), bg) == '#' else 0
                img[xi, yi] = code[v]

        bg = code[0] if bg == '.' else code[-1]

    return list(img.values()).count('#')


assert task1('test_input.txt', 2) == 35
print(task1('input.txt', 2))

assert task1('test_input.txt', 50) == 3351
print(task1('input.txt', 50))
