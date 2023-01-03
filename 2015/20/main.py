from itertools import count
from math import sqrt


def task1(nr):
    for i in count(1):
        presents = 0
        for j in range(1, int(sqrt(i)+1)):
            if i % j == 0:
                presents += j*10
                if int(i / j) != j:
                    presents += int(i/j) * 10
        if presents >= nr:
            return i


def get_divisors(n):
    p1 = [i for i in range(1, int(sqrt(n)+1)) if n % i == 0]
    p2 = [n // d for d in p1 if n != d**2][::-1]
    return p1 + p2


def task2(nr):
    for i in count(1):
        presents = sum(d for d in get_divisors(i) if i // d <= 50) * 11
        if presents >= nr:
            return i


task1(200)
print(task1(33100000))

print(task2(33100000))
