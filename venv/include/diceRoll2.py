import random

rInput = input('How many dice?  ')

def splitAndStrip():
    plusSplit = rInput.split('+')
    rolls = [x.strip(' ') for x in plusSplit]
    rollSet = [x.split('d') for x in rolls]
    return rollSet

def roll1():
    dice = int(rollSet[0][0])
    sides = int(rollSet[0][1])
    for i in range(0, dice):
        print(random.randint(1, sides))


def roll2():
    dice = int(rollSet[1][0])
    sides = int(rollSet[1][1])
    for i in range(0, dice):
        print(random.randint(1, sides))

rollSet = splitAndStrip()
roll1()
print('And your next roll.......')
roll2()

