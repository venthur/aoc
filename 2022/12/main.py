import logging

logging.basicConfig(level=logging.NOTSET)

test_input = '''\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
'''.splitlines()

with open('input.txt') as fh:
    input_ = fh.read().splitlines()


def task1(input_):
    map_ = dict()

    for row, line in enumerate(input_):
        for col, char in enumerate(line):
            if char == 'S':
                start = col, row
                map_[col, row] = ord('a')
            elif char == 'E':
                end = col, row
                map_[col, row] = ord('z')
            else:
                map_[col, row] = ord(char)

    # do a breadth first search
    visited = set()
    length = dict()
    todo = [(start, 0)]
    while todo:
        pos, steps = todo.pop(0)
        if pos not in visited:
            visited.add(pos)
            length[pos] = steps

            for new_pos in (
                (pos[0]+1, pos[1]), (pos[0]-1, pos[1]),
                (pos[0], pos[1]+1), (pos[0], pos[1]-1)
            ):

                if (
                    new_pos not in visited
                    and new_pos in map_
                    and map_[new_pos] - map_[pos] <= 1
                ):
                    todo.append((new_pos, steps+1))

    return length[end]


assert task1(test_input) == 31
print(task1(input_))
