import datetime
class LibraryItem:
    def __init__(self,t,a,i):
        self.__Title=t
        self.__Author__Artist=a
        self.__ItemID=i
        self.__OnLoan=False
        self.__DueDate=datetime.date.today()

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
    
    def Borrowing(self):
        self.__OnLoan=True
        self.__DueDate=self.__DueDate+ datetime.timedelta(weeks=1)

    def returning(self):
        self.__OnLoan=False

    def PrintDetails(self):
        print(self.__Title,',',self.__Author__Artist,',',end='')
        print(self.__ItemID,',',self.__OnLoan,',',self.__DueDate)

class Book(LibraryItem):
    def __init__(self,t,a,i):
        LibraryItem.__init__(self,t,a,i)
        self.__IsRequested=False
        self.__requestedby=0

    def GetIsRequested(self):
        return (self.__IsRequested)

    def setrequested(self,b):
        self.__IsRequested=True
        self.__requestedby=b

    def printdetails(self):
        print('Book details: ')
        LibraryItem.PrintDetails(self)
        if (self.__requestedby)==0:
            print('No requests')
        else:
            print('Requested by', self.__requestedby)

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






firstbook=Book('12 Rules for Life','Jordan Peterson',1)

firstbook.printdetails()

print('')
print('')
print('')
print('')
thirdcd=CD('Nine Track Mind','Charlie Puth',5)
thirdcd.SetGenre('Hip-Pop')
thirdcd.printdetails()

    

        









