# Hashcode test by Celebobo and Legend

test = input("please input name of test file")
with open('test', 'r') as f:
    #  content = f.readlines()
    lines = f.read().splitlines()
    # lines = lines
    # lines = lines.strip()
# lines = lines.split(" ")
# print(lines)
# lines.split(" ")


inque = lines[0]
# inque = str (inque)
inque = inque.split(" ")
indat = lines[1]
indat = indat.split(" ")

i = 1
Cel = []
arey = indat.copy()

charles = int(inque[0])
pizzas = int(inque[1])
hard = 0
pot_charles = 0


def recca():
    global i
    addarray()
    chiek()
    i = i + 1


def chiek():
    if hard == charles:
        solution()
    elif hard < charles:
        kiip()
    elif hard > charles:
        repl()


def addarray():
    global hard
    hard = hard + int(arey[-i])
    Cel.insert(0, arey[-i])


def solution():
    global pot_charles
    pot_charles = hard
    feenish()


def kiip():
    global pot_charles
    pot_charles = hard
    recca()


def repl():
    global hard
    hard = (hard - (arey[-i]))
    Cel.pop()
    addarray()
    recca()

    recca()


def feenish():
    print(pot_charles)
    print(len(Cel))
    print(Cel)


print(f)
print(i)
print(lines)
print(inque)
print(arey)
# print(indat)
print(charles)
print(pizzas)
print(hard)
print(arey[-i])
print(pot_charles)
print(Cel)
print(len(Cel))
