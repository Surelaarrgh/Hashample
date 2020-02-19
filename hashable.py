# Hashcode test by Celebobo and Legend




with open('b_small.in', 'r') as f:
  #  content = f.readlines()
    lines = f.read().splitlines()
    #lines = lines
    #lines = lines.strip()
   # lines = lines.split(" ")
    #print(lines)
#lines.split(" ")



inque = lines [0]
#inque = str (inque)
inque = inque.split(" ")
indat = lines[1]
indat = indat.split(" ")

i = 1
Cel = []
Arey = indat.copy()

Charles = int (inque[0])
Pizzas = int (inque[1])
Hard = 0
Pot_Charles = 0


def Recca():
    global i
    AddArray()
    Check()
    i = i + 1


def Check():
    if Hard == Charles:
        Solution()
    elif (Hard < Charles):
        kiip()
    elif (Hard > Charles):
        Repl()


def AddArray():
    global Hard
    Hard = Hard + int (Arey[-i])
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
print(i)
print(lines)
print(inque)
print(Arey)
#print(indat)
print(Charles)
print(Pizzas)
print(Hard)
print(Arey[-i])
print(Pot_Charles)
print(Cel)
print(len(Cel))
