def task1(fn):
    with open(fn) as fh:
        data = [int(n) for n in fh.read().strip()]

    width = 25
    height = 6
    size = width * height

    layers = len(data) // size
    minzeros = None
    l = None
    for layer in range(layers):
        zeros = data[layer*size:(layer+1)*size].count(0)
        if minzeros is None or zeros < minzeros:
            minzeros = zeros
            l = layer

    layer = data[l*size:(l+1)*size]
    return layer.count(1) * layer.count(2)


def task2(fn):
    with open(fn) as fh:
        data = [int(n) for n in fh.read().strip()]

    width = 25
    height = 6
    size = width * height
    layers = len(data) // size

    s = ''
    for y in range(height):
        for x in range(width):
            for l in range(layers):
                layer = data[l*size:(l+1)*size]
                pixel = layer[y*width+x]
                if pixel == 2:
                    continue
                elif pixel == 0:
                    s += ' '
                    break
                else:
                    s += '#'
                    break
        s += '\n'
    print(s)


print(task1('input.txt'))
print(task2('input.txt'))
