from itertools import count
from math import sqrt


def task1(nr):
    for i in count(1):
        presents = i*10
        for j in range(1, int(sqrt(i)+2)):
            if i % j == 0:
                presents += j*10
        print(f'{i} -> {presents}')
        if presents >= nr:
            return i

task1(200)
task1(33100000)

