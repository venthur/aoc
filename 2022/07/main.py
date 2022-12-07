test_input = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""".splitlines()


with open('input.txt') as fh:
    input_ = fh.read().splitlines()


def task1(input_):
    total = 0
    seen = set()
    cwd = []
    dirsizes = {}
    for line in input_:
        if line.startswith('dir'):
            continue
        if line.startswith('$ ls'):
            continue
        if line.startswith('$ cd'):
            _, _, path = line.split()
            if path == '/':
                cwd = []
            elif path == "..":
                cwd.pop()
            else:
                cwd.append(path)
        else:
            size, name = line.split()
            name = '/' + '/'.join(cwd+[name])
            if name not in seen:
                path = []
                for p in cwd:
                    path.append(p)

                    dir_ = '/'.join(path)
                    dirsizes[dir_] = dirsizes.get(dir_, 0) + int(size)
                seen.add(name)

    for dir_, size in dirsizes.items():
        if size <= 100000:
            total += size
    return total


def task2(input_):
    total = 0
    seen = set()
    cwd = []
    dirsizes = {}
    for line in input_:
        if line.startswith('dir'):
            continue
        if line.startswith('$ ls'):
            continue
        if line.startswith('$ cd'):
            _, _, path = line.split()
            if path == '/':
                cwd = []
            elif path == "..":
                cwd.pop()
            else:
                cwd.append(path)
        else:
            size, name = line.split()
            name = '/' + '/'.join(cwd+[name])
            if name not in seen:
                path = []
                dirsizes['/'] = dirsizes.get('/', 0) + int(size)
                for p in cwd:
                    path.append(p)

                    dir_ = '/'.join(path)
                    dirsizes[dir_] = dirsizes.get(dir_, 0) + int(size)
                seen.add(name)

    total = 70000000
    used = dirsizes['/']
    unused = total - used
    needed = 30000000 - unused
    current_best = None
    for dir_, size in dirsizes.items():
        if size < needed:
            continue
        if current_best is None:
            current_best = size
        if size < current_best:
            current_best = size
    return current_best


assert task1(test_input) == 95437
print(task1(input_))

assert task2(test_input) == 24933642
print(task2(input_))
