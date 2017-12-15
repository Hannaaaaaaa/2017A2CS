#Hanna Gao
#Recursion-1

def factorial(x):
    if x==1:
        return 1

    return x*factorial(x-1)

x=factorial(4)
print(x)
    

def bunnyEars(x):
    if x==0:
        return 0

    return 2+bunnyear(x-1)

def fibonacci(x):
    if x==0:
        return 0
    if x==1:
        return 1

    return fibonacci(x-2)+fibonacci(x-1)

def bunnyear2(x):
    if x==0:
        return 0

    if x%2==1:
        return bunnyear2(x-1)+2
    else:
        return bunnyear2(x-1)+3

def triangle(x):
    if x==0:
        return 0

    return x+triangle(x-1)

def sumdigit(x):
    if x==0:
        return 0
    
    return x%10+sumdigit(x//10)


def count7(x):
    if x==0:
        return 0

    if x%10==7:
        return 1+count7(x//10)
    else:
        return count7(x//10)

    
def count8(x):
    if x==0:
        return 0

    if x%10==8:
        if (x//10)%10==8:
            return 2+count8(x//10)
        else:
            return 1+count8(x//10)
    else:
        return count8(x//10)

def powerN(x,y):
    if y==0:
        return 1

    return x*powerN(x,y-1)
    

def countX(x):
    if x=='':
        return 0

    if x[0]=='x':
        return 1+countX(x[1:])
    else:
        return countX(x[1:])
    

def countHi(x):
    if x=='':
        return 0

    if x[0]=='h':
        if x[1]=='i':
            return 1+countHi(x[2:])
    else:
        return countHi(x[1:])

def changeXY(x):
    if x=='':
        return ''

    if x[len(x)-1]=='x':
        return changeXY(x[:(len(x)-1)])+'y'
    else:
        return changeXY(x[:(len(x)-1)])+x[len(x)-1]
           
def changePi(x):
    if x=='':
        return ''

    if x[-2:]=='Pi':
        return changePi(x[:-2])+'3.14'
    else:
        return changePi(x[:-1])+x[-1:]

def noX(x):
    if x=='':
        return ''

    if x[-1:]=='x':
        return noX(x[:-1])
    else:
        return noX(x[:-1])+x[-1:]

def array6(x,y):
    if y==len(x):
        return 'False'

    if x[y]==6:
            return 'True'
    
    return array6(x,y+1)


def array11(x,y):
    if y==len(x):
        return 0
    
    if x[y]==11:
        return array11(x,y+1)+1
    else:
        return array11(x,y+1)

    
def array220(x,y):
    if y==len(x)-1:
        return 'False'

    if x[y]*10==x[y+1]:
        return 'True'
    else:
        return array220(x,y+1)


def allStar(x):
    if x=='':
        return ''

    if x[1:]=='':
        return x[0]+allStar(x[1:])
    else:
        return x[0]+'*'+allStar(x[1:])

def pairStar(x):
    if x=='':
        return ''
    
    if x[1:]=='':
        return x
    if x[0]==x[1]:
        return x[0]+'*'+pairStar(x[1:])
    else:
        return x[0]+pairStar(x[1:])

def endX(x):
    if x=='':
        return ''

    if x[0]=='x':
        return endX(x[1:])+'x'
    else:
        return x[0]+endX(x[1:])

def countPairs(x):
    l=len(x)
    if l<3:
        return 0
    
    if l>2:
        if x[l-1]==x[l-3]:
            return 1+countPairs(x[:-1])
        else:
            return countPairs(x[:-1])

def countAbc(x):
    if x=='':
        return 0

    if x[:3]=='abc' or x[:3]=='aba':
        return 1+countAbc(x[1:])
    else:
        return countAbc(x[1:])

def count11(x):
    if x=='':
        return 0

    if x[:2]=='11':
        return 1+count11(x[2:])
    else:
        return count11(x[1:])
    
def stringClean(x):
    if len(x)==1:
        return x

    if x[-2]==x[-1]:
        return stringClean(x[:-1])
    else:
        return stringClean(x[:-1])+x[-1]

def countHi2(x):
    l=len(x)
    if x=='':
        return 0

    if x[-3:]=='xhi':
        return countHi2(x[:-3])
    if x[-2:]=='hi':
        return 1+countHi2(x[:-2])
    else:
        return countHi2(x[:-1])

def parenBit(x):
    l=len(x)
    if x=='':
        return ''

    if x[0]=='(':
        if x[l-1]==')':
            return x
        else:
            return parenBit(x[:-1])
    else:
        return parenBit(x[1:])

def nestParen(x):
    l=len(x)
    if x=='':
        return 'True'

    if x[0]=='(' or x[0]==')':
        return nestParen(x[1:])
    else:
        return 'False'

def strCount(x,y):
    w=len(y)
    if x=='':
        return 0

    if x[-w:]==y:
        return 1+strCount(x[:-w],y)
    else:
        return strCount(x[:-1],y)

def strCopies(x,y,z):
    w=len(y)
    if z==0:
        return 'True'
    if x=='':
        return 'False'

    if x[-w:]==y:
        return strCopies(x[:-w],y,z-1)
    else:
        return strCopies(x[:-1],y,z)

def strDist(x,y):
    l=len(x)
    w=len(y)
    if x=='':
        return 0

    if x[:3]==y:
        if x[-w:]==y:
            return l
        else:
            return strDist(x[:-1],y)
    else:
        return strDist(x[1:],y)

    




