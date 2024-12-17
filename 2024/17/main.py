from math import trunc
from itertools import count
from functools import cache


def read_input(fn):
    with open(fn) as fh:
        data = fh.read()
    registers_raw, program_raw = data.split('\n\n')
    registers = []
    for rr in registers_raw.split('\n'):
        registers.append(int(rr.split(':')[-1]))
    program_raw = program_raw.split(':')[-1]
    program = [int(i) for i in program_raw.split(',')]
    return registers, program


@cache
def compute(registers, program, ip, out):
    # TODO check ip < len(program)
    instr = program[ip]
    operand = program[ip+1]
    combo = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: registers[0],
        5: registers[1],
        6: registers[2],
    }[operand]
    match instr:
        case 0:
            # division
            registers[0] = trunc(registers[0] / 2**combo)
            ip += 2
        case 1:
            # bitwise XOR
            registers[1] = registers[1] ^ operand
            ip += 2
        case 2:
            # mod 8
            registers[1] = combo % 8
            ip += 2
        case 3:
            # jnz
            if registers[0] == 0:
                ip += 2
            else:
                ip = operand
        case 4:
            # bitwise XOR
            registers[1] = registers[1] ^ registers[2]
            ip += 2
        case 5:
            # out
            out.append(combo % 8)
            ip += 2
        case 6:
            registers[1] = trunc(registers[0] / 2**combo)
            ip += 2
        case 7:
            registers[2] = trunc(registers[0] / 2**combo)
            ip += 2
        case _:
            raise ValueError(f'Unknown instrunction {instr}')

    return registers, program, ip, out


def task1(fn):
    registers, program = read_input(fn)
    out = []
    ip = 0
    while ip < len(program):
        registers, program, ip, out = compute(registers, program, ip, out)

    return ','.join([str(i) for i in out])


def task2(fn):
    for i in count():
        registers, program = read_input(fn)
        registers[0] = i
        out = []
        ip = 0
        while ip < len(program):
            registers, program, ip, out = compute(registers, program, ip, out)
            #print(f'{ip=}, {registers=}, {out=}')
            if out == program:
                return i


assert task1('test_input.txt') == '4,6,3,5,6,3,5,2,1,0'
print(task1('input.txt'))

assert task2('test_input2.txt') == 117440
print(task2('input.txt'))
