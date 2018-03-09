import datetime
class Borrower:
    def __init__(self,n,e,b):
        self.__borrowername=n
        self.__emailaddress=e
        self.__borrowerid=b
        self.__itemsonloan=0

    def getborrowername(self):
        return (self.__borrowername)

    def getemailaddress(self):
        return (self.__emailaddress)

    def getborrowerid(self):
        return (self.__borrowerid)

    def getitemsonload(self):
        return (self.__itemsonloan)

    def updateitemsonloan(self,i):
        self.__itemsonloan=self.__itemsonloan+i

    def printdetails(self):
        print(self.__borrowername,self.__emailaddress,self.__borrowerid,self.__itemsonloan)

class LibraryItem:
    def __init__(self,t,a,i):
        self.__Title=t
        self.__Author__Artist=a
        self.__ItemID=i
        self.__OnLoan=False
        self.__borrowerid=0
        self.__DueDate=datetime.date.today()

    def GetTitle(self):
        return (self.__Title)

    def getaa(self):
        return (self.__Author__Artist)

    def getitemid(self):
        return (self.__ItemID)

    def getonloan(self):
        return (self.__OnLoan)

    def getborrowerid(self):
        return (self.__borrowerid)
        
    def Borrowing(self,i,x):
        self.__OnLoan=True
        self.__borrowerid=x.getborrowerid()
        self.__DueDate=self.__DueDate+datetime.timedelta(weeks=1)
        x.updateitemsonloan(1)
        
    def PrintDetails(self):
        print(self.__Title,',',self.__Author__Artist,',',end='')
        print(self.__ItemID,',',self.__OnLoan,',',self.__DueDate)

    def returning(self,i,x):
        self.__OnLoan=False
        x.updateitemsonloan(-1)

class Book(LibraryItem):
    def __init__(self,t,a,i):
        LibraryItem.__init__(self,t,a,i)
        self.__IsRequested=False
        self.__RequestedBy=0

    def GetIsRequested(self):
        return (self.__IsRequested)

    def setrequest(self,i,x):
        self.__IsRequested=True
        self.__RequestedBy=x.getborrowerid()

    def getrequestedby(self):
        return (self.__RequestedBy)

    def PrintDetails(self):
        print('Book Details')
        LibraryItem.PrintDetails(self)
        if (self.__IsRequested)==True:
            print('Requested by',self.__RequestedBy)
        else:
            print('No requests')
            
class CD(LibraryItem):
    def __init__(self,t,a,i):
        LibraryItem.__init__(self,t,a,i)
        self.__Genre=''

    def GetGenre(self):
        return(self.__Genre)

    def SetGenre(self,g):
        self.__Genre=g

    def PrintDetails(self):
        print('CD Details')
        LibraryItem.PrintDetails(self)
        print(self.__Genre)

def menu():
    print('1: Add a new borrower')
    print('2: Add a new book')
    print('3: Add a new CD')
    print('4: Borrow a book')
    print('5: Return a book')
    print('6: Borrow a CD')
    print('7: Return a CD')
    print('8: Request book')
    print('9: Print all details')
    print('99: Exit program')


end=False
nbi=1
nboi=1
nci=1
while end==False:
    menu()
    a=int(input('Enter your choice: '))
    if a==1:
        n=input('Borrower name: ')
        e=input('Borrower email address: ')
        b=nbi
        nbi+=1
        borrower=Borrower(n,e,b)
    if a==2:
        t=input('Book title: ')
        a=input('Book author: ')
        itemid=nboi
        nboi+=1
        book=Book(t,a,itemid)
    if a==3:
        t=input('CD name: ')
        a=input('CD artist: ')
        itemid=nci
        nci+=1
        CD=CD(t,a,nci)
    if a==4:
        bi=input('Borrower ID: ')
        itemid=input('Book ID: ')
        book.Borrowing(itemid,bi)
    if a==5:
        bi=input('Borrower ID: ')
        itemid=input('Book ID: ')
        book.returning(itemid,bi)
    if a==6:
        bi=input('Borrower ID: ')
        itemid=input('CD ID: ')
        CD.Borrowing(itemid,bi)
    if a==7:
        bi=input('Borrower ID: ')
        itemid=input('CD ID: ')
        CD.returning(itemid,bi)
    if a==8:
        bi=input('Borrower ID: ')
        itemid=input('Book ID: ')
        book.setrequest(itemid,bi)
    if a==9:
        print('Borrower')
        borrower.printdetails()
        print('')
        print('Book')
        book.PrintDetails()
        print('')
        print('CD')
        CD.PrintDetails()
    if a==99:
        end=True
    
    
        
    
    


        
    
