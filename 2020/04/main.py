def task1(fn):
    with open(fn) as fh:
        data = [block.split() for block in fh.read().split('\n\n')]

    required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    valid = 0
    for d in data:
        keys = {item.split(':')[0] for item in d}
        if required.issubset(keys):
            valid += 1

    return valid


def task2(fn):
    with open(fn) as fh:
        data = [block.split() for block in fh.read().split('\n\n')]

    required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    valid = 0
    for d in data:
        keys = {item.split(':')[0] for item in d}
        if not required.issubset(keys):
            continue

        keys = {item.split(':')[0]: item.split(':')[1] for item in d}
        year = int(keys['byr'])
        if year < 1920 or year > 2002:
            continue
        year = int(keys['iyr'])
        if year < 2010 or year > 2020:
            continue
        year = int(keys['eyr'])
        if year < 2020 or year > 2030:
            continue
        height, unit = int(keys['hgt'][:-2]), keys['hgt'][-2:]
        if unit not in ('cm', 'in'):
            continue
        if unit == 'cm' and (height < 150 or height > 193):
            continue
        if unit == 'in' and (height < 59 or height > 76):
            continue
        hcl = keys['hcl']
        if not hcl.startswith('#') or len(hcl) != 7:
            continue
        if not {c for c in hcl[1:]} <= {c for c in '0123456789abcdef'}:
            continue
        ecl = keys['ecl']
        if ecl not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            continue
        pid = keys['pid']
        if len(pid) != 9 or not pid.isnumeric():
            continue

        valid += 1

    return valid


print(task1('input.txt'))
print(task2('input.txt'))
