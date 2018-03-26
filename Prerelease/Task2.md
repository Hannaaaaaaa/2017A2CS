#Task2
2.1
toy:
Name: STRING
ID: STRING
Price: CURRENCY
MinimumAge: INTEGER
constructor()
getName()
getID()
getPrice()
getMinAge()
setName()
setID()
setPrice()
setMinAge()
outputDetails()

computergame:
category: STRING
console: STRING
constructor()
getCategory()
getConsole()
set(Category)
setConsole()

vehicle:
type: STRING
Height: FLOAT
Length: FLOAT
Weight: FLOAT
constructor()
getType()
getHeight()
getLength()
getWeight()
setType()
setHeight()
setLength()
setWeight()


2.2
Inheritance: allattributes and methods of the base class are copied to the subclass
Arrows extend from computergame and vehicle to toy
Computergame and vechile are subclass
Toy is base class

2.3
Class Toy:
>def __init__(self,n,i,p,a):
>>self.__name=n
>>self.__id=i
>>self.__price=p
>>self.__minimumage=a

>def getName(self):
>>return(self.__name)
>
>def getID(self):
>>return(self.__id)
>
>def getPrice(self):
>>return(self.__price)

>def getMinAge(self):
>>return(self.__minimumage)

>def setName(self,n):
>>self.__name=n

>def setID(self,i):
>>self.__id=i

>def setPrice(self,p):
>>self.__price=p

>def setMinAge(self,a):
>>self.__minimumage=a

2.4
Class computergame:
>def __init__(self,n,i,p,a):
>>Toy.__init__(self,n,i,p,a)
>>self.__ca=''
>>self.__co=''

>def getCa(self):
>>return (self.__ca)

>def getCo(self):
>>return(self.__co)

>def setCa(self,ca):
>>self.__ca=ca

>def setCo(self,co):
>>self.__co=co

Class vehicle:
>def __init__(self,n,i,p,a):
>>Toy.__init__(self,n,i,p,a)
>>self.__type=''
>>self.__height=0.0
>>self.__length=0.0
>>self.__weight=0.0

>def getType(self):
>>return (self.__type)
>
>def getHeight(self):
>>return (self.__height)
>
>def getLength(self):
>>return (self.__length)

>def getWeight(self):
>>return (self.__weight)

>def setType(self,x):
>>self.__type=t

>def setHeight(self,x):
>>self.__height=t

>def setLength(self,x):
>>self.__length=t

>def setWright(self,x):
>>self.__weight=t

2.5
Class toy
>def __init__(self,n,i,p,a):
>>self.__name=n
>>self.__id=i
>>self.__price=p
>>self.__minimumage=a #0-18

>def setname(self,name):
>>if not(str(name)):
>>>print(‘Not string’)
>>if len(name)<1:
>>>print(‘invalid’)
>>self._name=name

Class computergame:
>def __init__(self,n,i,p,a):
>>Toy.__init__(self,n,i,p,a)
>>self.__ca=''
>>self.__co=''

>def setca(self,ca):
>>if not(str(ca)):
>>>print(‘Not string’)
>>if len(ca)<1:
>>>print(‘invalid’)
>>self._ca=ca


Class vehicle:
>def __init__(self,n,i,p,a):
>>Toy.__init__(self,n,i,p,a)
>>self.__type=''
>>self.__height=0.0
>>self.__length=0.0
>>self.__weight=0.0

>def settype(self,type):
>>if not(str(type)):
>>>print(‘Not string’)
>>if len(type)<1:
>>>print(‘invalid’)
>>self._type=type


2.6 
v1=vehicle('Read Sports Car', "RSC13", 15.00, 6)
v1.setType('Car')
v1.setHeight(3.3)
v1.setLength(12.1)
v1.setWeight(0.08)

c1.computergame('PUBG', 'TEN12', '50.00', 10)
c1.setCa('Running Dead')
c1.setCo('MAC')

toy=[]
Toy.append(v1)
Toy.append(c1)

2.7
def outputdetails(self):
>ID=find()
>print(’Name: ', toy[ID].name,'  Price: ', toy[ID].price, 'Minimum Age: ', toy[ID].minimumage)

def outputcg(self):
>print(‘Category: ’, toy[ID].ca,’Console: ’,toy[ID].co)

def outputve(self):
>print(‘Type: ’, toy[ID].type,’Height: ’,toy[ID].height,’Length: ’, toy[ID].length,’Weight: ’,toy[ID].weight)

def find(self):
>id=input(‘Enter the ID: ’)
>for i in toy:
>>if i.ID()=id:
>>>return i
>print(‘ERROR’)


2.8
def discount(self):
>d=int(input('Enter the discount rate: '))
>p=toy.getPrice()
>toy.setPrice(p*(d/100))

2.9
Bubble sort is to go through the whole list and each time take the biggest or smallest valus in correct position, then repeat until all the values are in correct order. Insertion sort is to take one random value to its correct position directly.

2.10
def sorting(self):
>n=len(ComputerGame)-1
>for i in range(len(ComputerGame)-1):
>>for j in range n:
>>>if ComputerGame[j].id>ComputerGame[j+1].id:
>>>temp=ComputerGame[j]
>>>ComputerGame[j]=ComputerGame[j+1]
>>>ComputerGame[j+1]=temp
>n-=1
