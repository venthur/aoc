LETTERS = 'abcdefghijklmnopqrstuvwxyz'
VALID_LETTERS = 'abcdefghjkmnpqrstuvwxyz'

PAIRS = [''.join([c, c]) for c in VALID_LETTERS]
TRIPLES = [
    ''.join([LETTERS[i], LETTERS[i+1], LETTERS[i+2]])
    for i in range(len(LETTERS) - 2)
]

def task1(input_):
    while True:
        input_ = list(input_)
        if chr(ord(input_[-1]) + 1) in VALID_LETTERS:
            input_[-1] = chr(ord(input_[-1]) + 1)
        else:
            input_[-1] = chr(ord(input_[-1]) + 2)
        for i in range(7, 0, -1):
            if input_[i] > 'z':
                input_[i] = 'a'
                if chr(ord(input_[i-1]) + 1) in VALID_LETTERS:
                    input_[i-1] = chr(ord(input_[i-1]) + 1)
                else:
                    input_[i-1] = chr(ord(input_[i-1]) + 2)
        input_ = ''.join(input_)
        valid_l = True
        valid_p = 0
        valid_t = False
        for l in input_:
            if l not in VALID_LETTERS:
                valid_l = False
        for p in PAIRS:
            if p in input_:
                valid_p += 1
        for t in TRIPLES:
            if t in input_:
                valid_t = True
        if valid_l and valid_p >= 2 and valid_t:
            break
    return input_


assert task1('abcdefgh') == 'abcdffaa'
assert task1('ghijklmn') == 'ghjaabcc'
print(task1('vzbxkghb'))

print(task1('vzbxxyzz'))
