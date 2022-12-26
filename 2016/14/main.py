import re
from hashlib import md5
from functools import cache

THREE = re.compile(r'(\w)\1\1')


@cache
def hash(salt, i):
    return md5((salt + str(i)).encode()).hexdigest()


@cache
def hash2(salt, i):
    h = md5((salt + str(i)).encode()).hexdigest()
    for i in range(2016):
        h = md5(h.encode()).hexdigest()
    return h


def task1(salt):
    i = -1
    count = 0
    while True:
        if count == 64:
            return i
        i += 1
        h = hash(salt, i)
        if m := THREE.search(h):
            c = m.group(1)
            for ii in range(1000):
                h2 = hash(salt, i+ii+1)
                if re.search(rf'({c})\1\1\1\1', h2):
                    count += 1
                    break


def task2(salt):
    i = -1
    count = 0
    while True:
        if count == 64:
            return i
        i += 1
        h = hash2(salt, i)
        if m := THREE.search(h):
            c = m.group(1)
            for ii in range(1000):
                h2 = hash2(salt, i+ii+1)
                if re.search(rf'({c})\1\1\1\1', h2):
                    count += 1
                    break


assert task1('abc') == 22728
print(task1('zpqevtbw'))

assert task2('abc') == 22551
print(task2('zpqevtbw'))
