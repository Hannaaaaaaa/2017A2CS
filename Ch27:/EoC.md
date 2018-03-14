{\rtf1\ansi\ansicpg936\cocoartf1561\cocoasubrtf200
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 \
# Chapter 27 \
## End of Chapter Questions\
### Hanna Gao Option1\
1. (a)\
```mermaid\
graph LR\
A[Bank Account] --> B[Personal Account]\
A --> C[Saving Account]\
```\
(b)\
class bankaccount:\
> def __ init__ (self,i):\
> >  self.__accountholdername=''\
> > self.__IBAN=i\
\
> def setaccountholdername(self,n):\
> > self.__accountholdername=n\
\
> def getaccountholdername(self):\
> > return(self.__accountholdername)\
\
> def getIBAN(self):\
> >return (self.__IBAN)\
\
(c.) i. \
Attributes: MonthlyFee; OverdraftLimit\
Method: constructor(); getMonthlyFee(); setOverdraftLimit(); getOverdraftLimit()\
ii.\
Attributes: InterestRate\
Method: constructor(); getInterestRate(); setInterestRate()\
iii.\
Encapsulation\
\
2. (a)\
EmailAddress: STRING\
getHolderName():\
getEmailAddress():\
\
account: CURRENCY\
constructor()\
getAmount()\
setAmount()\
\
MonthlyFee: CURRENCY\
getMonthlyFee()\
\
(b).i \
So the attributes can only be changed through the declared class methods\
ii. \
So the methods can be accessed by users to change class private attributes\
\
(c.)\
NewCustomer=ContrastTicketHolder('A.Smith', 'xyz@abc.xx', '10')\
\
\
3. (a)\
Containment\
\
(b)\
class NodeClass:\
> def __ init__ (self):\
> > self.__data=''\
> > self.__pointer=-1\
\
>def setdata(self,n):\
>> self.__data=n\
\
>def getdata(self):\
>> return (self.__data)\
\
>def setpointer(self,p):\
>> self.__pointer=p\
\
>def getpointer(self):\
>> return (self.__pointer)\
\
(c.)\
class QueueClass:\
> def __ init__ (self):\
> > self.__queue=[NodeClass() for i in range(51)]\
> > self.__head=-1\
> >sefl.__tail=-1\
\
(d)\
def JoinClass(self,d):\
> if head=-1:\
> > head=0\
> \
> else:\
> >i=self.__tail\
>> self.__queue[i].setdata(d)\
>>self.__tail+=1\
\
}