from math import sqrt


def read_data(fn):
    with open(fn) as fh:
        data = fh.read().strip().split('\n\n')

    tiles = dict()
    for d in data:
        header, *tile = d.splitlines()
        tile_nr = int(header.removesuffix(':').split()[-1])
        tiles[tile_nr] = [tuple(c for c in line) for line in tile]

    return tiles


def rotate_and_flip(tile):
    """Generate all valid rotations and flips for the tile.

    """
    res = []

    rotated = tile[:]
    res.append(rotated)
    for i in range(3):
        rotated = tuple(zip(*rotated[::-1]))
        res.append(rotated)

    rotated = rotated[::-1]
    res.append(rotated)
    for i in range(3):
        rotated = tuple(zip(*rotated[::-1]))
        res.append(rotated)

    return tuple(res)


def fits(test_tile, top, left, tiles):
    fits_top = False
    if top is None:
        fits_top = True
    else:
        tile = tiles[test_tile[0]][test_tile[1]]
        tilet = tiles[top[0]][top[1]]
        fits_top = tile[0] == tilet[-1]

    fits_left = False
    if left is None:
        fits_left = True
    else:
        tile = tiles[test_tile[0]][test_tile[1]]
        tilel = tiles[left[0]][left[1]]

        fits_left = list(zip(*tile))[0] == list(zip(*tilel))[-1]

    return fits_left and fits_top


def task1(fn):
    tiles = read_data(fn)
    tiles = {k: rotate_and_flip(v) for k, v in tiles.items()}

    # assume the image is square
    l = int(sqrt(len(tiles)))

    # state is image, remaining titles
    todo = [([None for i in range(l*l)], list(tiles.keys()))]
    while todo:
        img, remaining_tiles = todo.pop()
        if not remaining_tiles:
            break

        idx = img.index(None)
        x = idx % l
        y = idx // l
        top = img[idx - l] if y > 0 else None
        left = img[idx - 1] if x > 0 else None
        for tileid in remaining_tiles:
            for i in range(8):
                if fits((tileid, i), top=top, left=left, tiles=tiles):
                    # remove current tile from remaining tiles and queue it up
                    remaining_tiles2 = remaining_tiles[:]
                    remaining_tiles2.remove(tileid)
                    img2 = img[:]
                    img2[idx] = (tileid, i)
                    todo.append((img2, remaining_tiles2))

    # pt1
    pt1 = img[0][0] * img[l-1][0] * img[-l][0] * img[-1][0]

    # pt2
    img2 = [[None for i in range(l*8)] for j in range(l*8)]
    for idx, (tileid, r) in enumerate(img):
        # x, y offsets
        x = 8 * (idx % l)
        y = 8 * (idx // l)

        tile = tiles[tileid][i]
        for yi, row in enumerate(tile):
            for xi, v in enumerate(row):
                # cut off the borders
                if xi in (0, 9) or yi in (0, 9):
                    continue
                img2[y + yi - 1][x + xi - 1] = v

    candidates = rotate_and_flip(img2)
    for c in candidates:
        s = ''
        print()
        for row in c:
            print(''.join(row))
            s += ''.join(row)
        print(s)
    pt2 = None
    return (pt1, pt2)

assert task1('test_input0.txt') == (20899048083289, 273)
print(task1('input.txt'))
