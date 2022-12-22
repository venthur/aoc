from hashlib import md5


def task1(input_):
    password = []
    i = 0
    while True:
        if len(password) == 8:
            break
        i += 1
        hash_ = md5((input_ + str(i)).encode()).hexdigest()
        if hash_.startswith('00000'):
            password.append(hash_[5])

    return ''.join(password)


def task2(input_):
    password = [None for i in range(8)]
    i = 0
    while True:
        i += 1
        hash_ = md5((input_ + str(i)).encode()).hexdigest()
        if hash_.startswith('00000'):
            if hash_[5].isnumeric() and int(hash_[5]) <= 7 and password[int(hash_[5])] is None:
                password[int(hash_[5])] = hash_[6]
                if None not in password:
                    break

    return ''.join(password)


assert task1('abc') == '18f47a30'
print(task1('abbhdwsy'))

assert task2('abc') == '05ace8e3'
print(task2('abbhdwsy'))
