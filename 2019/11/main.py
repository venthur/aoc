from collections import defaultdict


def compute(code_in, in_):
    code = defaultdict(lambda: 0)
    for i, v in enumerate(code_in):
        code[i] = v

    ptr = 0
    relative_base = 0
    while True:
        instr = code[ptr]
        op = instr % 100
        # one parameter, none writing
        if op in (4, 9):
            ap = code[ptr+1]
            match instr // 100 % 10:
                case 0:
                    a = code[ap]
                case 1:
                    a = ap
                case 2:
                    a = code[relative_base + ap]
        # one parameter, writing
        elif op in (3, ):
            ap = code[ptr+1]
            if instr // 100 % 10 == 2:
                a = relative_base + ap
            else:
                a = ap
        # two parameters, no writing
        elif op in (5, 6):
            ap = code[ptr+1]
            match instr // 100 % 10:
                case 0:
                    a = code[ap]
                case 1:
                    a = ap
                case 2:
                    a = code[relative_base + ap]
            bp = code[ptr+2]
            match instr // 1000 % 10:
                case 0:
                    b = code[bp]
                case 1:
                    b = bp
                case 2:
                    b = code[relative_base + bp]
        # three parameters, last one writing
        elif op in (1, 2, 7, 8):
            ap = code[ptr+1]
            match instr // 100 % 10:
                case 0:
                    a = code[ap]
                case 1:
                    a = ap
                case 2:
                    a = code[relative_base + ap]
            bp = code[ptr+2]
            match instr // 1000 % 10:
                case 0:
                    b = code[bp]
                case 1:
                    b = bp
                case 2:
                    b = code[relative_base + bp]
            cp = code[ptr+3]
            if instr // 10000 % 10 == 2:
                c = relative_base + cp
            else:
                c = cp

        match op:
            case 1:
                code[c] = a + b
                ptr += 4
            case 2:
                code[c] = a * b
                ptr += 4
            case 3:
                code[a] = in_
                ptr += 2
            case 4:
                received = yield a
                in_ = in_ if received is None else received
                ptr += 2
            case 5:
                ptr = b-3 if a else ptr
                ptr += 3
            case 6:
                ptr = b-3 if not a else ptr
                ptr += 3
            case 7:
                code[c] = 1 if a < b else 0
                ptr += 4
            case 8:
                code[c] = 1 if a == b else 0
                ptr += 4
            case 9:
                relative_base += a
                ptr += 2
            case 99:
                break


def task1(fn):
    with open(fn) as fh:
        code = [int(n) for n in fh.read().strip().split(',')]

    hull = defaultdict(lambda: 0)
    x, y = 0, 0
    direction = 0
    cmp = compute(code, hull[x, y])
    painted = set()
    while True:
        try:
            c = next(cmp)
            d = next(cmp)
        except StopIteration:
            break
        print(c, d)
        # paint
        hull[x, y] = c
        painted.add((x, y))
        # change direction
        if d == 0:
            direction -= 1
        elif d == 1:
            direction += 1
        direction %= 4
        # move
        match direction:
            case 0:
                y -= 1
            case 1:
                x += 1
            case 2:
                y += 1
            case 3:
                x -= 1
        cmp.send(hull[x, y])

    return len(painted)


print(task1('input.txt'))




# On the way to Jupiter, you're pulled over by the Space Police.
# 
# "Attention, unmarked spacecraft! You are in violation of Space Law! All
# spacecraft must have a clearly visible registration identifier! You have 24
# hours to comply or be sent to Space Jail!"
# 
# Not wanting to be sent to Space Jail, you radio back to the Elves on Earth
# for help. Although it takes almost three hours for their reply signal to
# reach you, they send instructions for how to power up the emergency hull
# painting robot and even provide a small Intcode program (your puzzle input)
# that will cause it to paint your ship appropriately.
# 
# There's just one problem: you don't have an emergency hull painting robot.
# 
# You'll need to build a new emergency hull painting robot. The robot needs to
# be able to move around on the grid of square panels on the side of your ship,
# detect the color of its current panel, and paint its current panel black or
# white. (All of the panels are currently black.)
# 
# The Intcode program will serve as the brain of the robot. The program uses
# input instructions to access the robot's camera: provide 0 if the robot is
# over a black panel or 1 if the robot is over a white panel. Then, the program
# will output two values:
# 
#     First, it will output a value indicating the color to paint the panel the
#     robot is over: 0 means to paint the panel black, and 1 means to paint the
#     panel white.
#     Second, it will output a value indicating the direction the robot should
#     turn: 0 means it should turn left 90 degrees, and 1 means it should turn
#     right 90 degrees.
# 
# After the robot turns, it should always move forward exactly one panel. The
# robot starts facing up.
# 
# The robot will continue running for a while like this and halt when it is
# finished drawing. Do not restart the Intcode computer inside the robot during
# this process.
# 
# For example, suppose the robot is about to start running. Drawing black
# panels as ., white panels as #, and the robot pointing the direction it is
# facing (< ^ > v), the initial state and region near the robot looks like
# this:
# 
# .....
# .....
# ..^..
# .....
# .....
# 
# The panel under the robot (not visible here because a ^ is shown instead) is
# also black, and so any input instructions at this point should be provided 0.
# Suppose the robot eventually outputs 1 (paint white) and then 0 (turn left).
# After taking these actions and moving forward one panel, the region now looks
# like this:
# 
# .....
# .....
# .<#..
# .....
# .....
# 
# Input instructions should still be provided 0. Next, the robot might output 0
# (paint black) and then 0 (turn left):
# 
# .....
# .....
# ..#..
# .v...
# .....
# 
# After more outputs (1,0, 1,0):
# 
# .....
# .....
# ..^..
# .##..
# .....
# 
# The robot is now back where it started, but because it is now on a white
# panel, input instructions should be provided 1. After several more outputs
# (0,1, 1,0, 1,0), the area looks like this:
# 
# .....
# ..<#.
# ...#.
# .##..
# .....
# 
# Before you deploy the robot, you should probably have an estimate of the area
# it will cover: specifically, you need to know the number of panels it paints
# at least once, regardless of color. In the example above, the robot painted 6
# panels at least once. (It painted its starting panel twice, but that panel is
# still only counted once; it also never painted the panel it ended on.)
# 
# Build a new emergency hull painting robot and run the Intcode program on it.
# How many panels does it paint at least once?
