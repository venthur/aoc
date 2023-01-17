def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    def convert_int(s):
        if s.startswith('-') or s.isnumeric():
            return int(s)
        return s

    lines = [list(map(convert_int, line.split())) for line in lines]
    print(lines)

    ptr = 0
    register = dict(a=0, b=0, c=0, d=0, e=0, f=0, g=0, h=0)
    multiplications = 0
    while 0 <= ptr < len(lines):
        match lines[ptr]:
            case 'set', reg, val:
                if isinstance(val, str):
                    val = register[val]
                register[reg] = val
            case 'sub', reg, val:
                if isinstance(val, str):
                    val = register[val]
                register[reg] -= val
            case 'mul', reg, val:
                if isinstance(val, str):
                    val = register[val]
                register[reg] *= val
                multiplications += 1
            case 'jnz', val, offset:
                if isinstance(val, str):
                    val = register[val]
                if val != 0:
                    ptr += offset - 1
        ptr += 1

    return multiplications


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    def convert_int(s):
        if s.startswith('-') or s.isnumeric():
            return int(s)
        return s

    lines = [list(map(convert_int, line.split())) for line in lines]
    print(lines)

    ptr = 0
    register = dict(a=1, b=0, c=0, d=0, e=0, f=0, g=0, h=0)
    while 0 <= ptr < len(lines):
        #print(f'{register}\n {ptr}, {lines[ptr]}')
        match lines[ptr]:
            case 'set', reg, val:
                if isinstance(val, str):
                    val = register[val]
                register[reg] = val
            case 'sub', reg, val:
                if isinstance(val, str):
                    val = register[val]
                register[reg] -= val
            case 'mul', reg, val:
                if isinstance(val, str):
                    val = register[val]
                register[reg] *= val
            case 'jnz', val, offset:
                if isinstance(val, str):
                    val = register[val]
                if val != 0:
                    ptr += offset - 1
        ptr += 1

    return register['h']


print(task1('input.txt'))

print(task2('input.txt'))

#--- Day 23: Coprocessor Conflagration ---
#
# You decide to head directly to the CPU and fix the printer from there. As you
# get close, you find an experimental coprocessor doing so much work that the
# local programs are afraid it will halt and catch fire. This would cause
# serious issues for the rest of the computer, so you head in and see what you
# can do.
#
# The code it's running seems to be a variant of the kind you saw recently on
# that tablet. The general functionality seems very similar, but some of the
# instructions are different:
#
#    set X Y sets register X to the value of Y.
#    sub X Y decreases register X by the value of Y.
#    mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
#    jnz X Y jumps with an offset of the value of Y, but only if the value of X is not zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
#
#    Only the instructions listed above are used. The eight registers here,
#    named a through h, all start at 0.
#
# The coprocessor is currently set to some kind of debug mode, which allows for
# testing, but prevents it from doing any meaningful work.
#
# If you run the program (your puzzle input), how many times is the mul
# instruction invoked?
