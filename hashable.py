# Hashcode test by Celebobo and Legend


inque = []
indat = []

with "open('b_small.in', 'r')" as f:
    # content = f.readlines()
    lines = f.readlines()
    print(lines)

i = 1
Cel = []
Arey = []
Charles = 0
Hard = 0
Pot_Charles = 0


def Recca():
    global i
    AddArray()
    Check()
    i = +1


def Check():
    if Hard == Charles:
        Solution()
    elif (Hard < Charles):
        kiip()
    elif (Hard > Charles):
        Repl()


def AddArray():
    global Hard
    Hard = + Arey[-i]
    Cel.insert(0, Arey[-i])


def Solution():
    global Pot_Charles
    Pot_Charles = Hard
    Finish()


def kiip():
    global Pot_Charles
    Pot_Charles = Hard
    Recca()


def Repl():
    global Hard
    Hard = (Hard - (Arey[-i]))
    Cel.pop()
    AddArray()
    Recca()

    Recca()


def Finish():
    print(Pot_Charles)
    print(len(Cel))
    print(Cel)


print(f)
print(Hard)
print(Pot_Charles)
print(Cel)
print(len(Cel))
