#Hashcode test by Celebobo and Legend



inque=[]
indat=[]

with "open('test.in', 'r')" as f:
    #content = f.readlines()
    lines = f.readlines()
    print (lines)


i= 1
Cel = []
Arey = []
Charles= 0
Add= 0
Pot_Charles=0



def Recca( i ):
    AddArray()
    Check()
    i=+1

def Check():
    if ( Add==Charles ) :
        Solution()
    elif (Add < Charles) :
        kiip()
    elif ( Add>Charles ) :
        Repl()

def AddArray():
    Add=+ Arey[-i]
    Cel.insert(0, Arey[-i])

def Solution():
    Pot_Charles= Add
    Finish()

def kiip ():
    Pot_Charles= Add
    Recca(i)

def Repl():
    Add = (Add - (Arey[-i]))
    Cel.pop()
    AddArray()
    Recca()

    Recca(i)

def Finish():
    print (Pot_Charles)
    print (len(Cel)
    print (Cel)