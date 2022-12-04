from hashlib import md5


def task1(input_):
    i = 0
    while True:
        i += 1
        if md5((input_ + str(i)).encode()).hexdigest().startswith('00000'):
            print(i)
            return


def task2(input_):
    i = 0
    while True:
        i += 1
        if md5((input_ + str(i)).encode()).hexdigest().startswith('000000'):
            print(i)
            return



#task1('abcdef')  # 609043
#task1('pqrstuv')  # 1048970
task1('ckczppom')
task2('ckczppom')
