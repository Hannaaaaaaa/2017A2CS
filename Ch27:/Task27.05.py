import datetime
class LibraryItem:
    def __init__(self,t,a,i):
        self.__Title=t
        self.__Author__Artist=a
        self.__ItemID=i
        self.__OnLoan=False
        self.__DueDate=datetime.date.today()
        self.__borrowerid=0

    def GetTitle(self):
        return (self.__Title)

    def getauthorartist(self):
        return (self.__Author__Artist)

    def getitemid(self):
        return (self.__ItemID)

    def getonloan(self):
        return (self.__OnLoan)

    def getduedate(self):
        return (self.__DueDate)
    
    def Borrowing(self,bid):
        self.__OnLoan=True
        self.__DueDate=self.__DueDate+ datetime.timedelta(weeks=1)
        self.__borrowerid=bid

    def returning(self):
        self.__OnLoan=False

    def PrintDetails(self):
        print(self.__Title,',',self.__Author__Artist,',',end='')
        print(self.__ItemID,',',self.__OnLoan,',',self.__DueDate,',',self.__borrowerid)

class Book(LibraryItem):
    def __init__(self,t,a,i):
        LibraryItem.__init__(self,t,a,i)
        self.__IsRequested=False

    def GetIsRequested(self):
        return (self.__IsRequested)

    def setrequested(self):
        self.__IsRequested=True

    def printdetails(self):
        print('Book details: ')
        LibraryItem.PrintDetails(self)
        print(self.__IsRequested)

class CD(LibraryItem):
    def __init__(self,t,a,i):
        LibraryItem.__init__(self,t,a,i)
        self.__Genre=''

    def GetGenre(self):
        return(self.__Genre)

    def SetGenre(self,g):
        self.__Genre=g

    def printdetails(self):
        print('CD details: ')
        LibraryItem.PrintDetails(self)
        print(self.__Genre)

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

borrower=Borrower('A','a@163.com',100)
borrower.updateitemsonloan(10)
borrower.printdetails()
        

firstbook=Book('12 Rules for Life','Jordan Peterson',1)
firstbook.Borrowing(100)
firstbook.printdetails()


thirdcd=CD('Nine Track Mind','Charlie Puth',5)
thirdcd.SetGenre('Hip-Pop')
thirdcd.Borrowing(100)
thirdcd.printdetails()








