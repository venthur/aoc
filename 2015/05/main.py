with open('input.txt') as fh:
    input_ = fh.read().splitlines()


def is_nice(s):
    vovels = 0
    for vovel in 'aeiou':
        vovels += s.count(vovel)
    if vovels < 3:
        return False
    doubles = 0
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        doubles += s.count(letter + letter)
    if doubles < 1:
        return False
    for i in 'ab', 'cd', 'pq', 'xy':
        if i in s:
            return False
    return True


def task1(input_):
    count = 0
    for s in input_:
        if is_nice(s):
            count += 1
    print(count)


def is_nice2(s):
    for i, c in enumerate(s[:-1]):
        s2 = s[i] + s[i+1]
        test1 = False
        if s.find(s2, i+2) != -1:
            test1 = True
            break
    if not test1:
        return False

    for i, c in enumerate(s[:-2]):
        test2 = False
        if s[i] == s[i+2]:
            test2 = True
            break
    if not test2:
        return False

    return True


def task2(input_):
    count = 0
    for s in input_:
        if is_nice2(s):
            count += 1
    print(count)



#print(is_nice('ugknbfddgicrmopn'))  # true
#print(is_nice('aaa'))  # true
#print(is_nice('jchzalrnumimnmhp'))  # false
#print(is_nice('haegwjzuvuyypxyu'))  # false
#print(is_nice('dvszwmarrgswjxmb'))  # false
task1(input_)

print(is_nice2('qjhvhtzxzqqjkmpb'))  # True
print(is_nice2('xxyxx'))  # True
print(is_nice2('uurcxstgmygtbstg'))  # False
print(is_nice2('ieodomkazucvgmuy'))  # False
task2(input_)
