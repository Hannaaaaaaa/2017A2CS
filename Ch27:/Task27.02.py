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

    def GetIsRequested(self):
        return (self.__IsRequested)

    def setrequested(self):
        self.__IsRequested=True

class CD(LibraryItem):
    def __init__(self,t,a,i):
        LibraryItem.__init__(self,t,a,i)
        self.__Genre=''

    def GetGenre(self):
        return(self.__Genre)

    def SetGenre(self,g):
        self.__Genre=g

firstbook=Book('12 Rules for Life','Jordan Peterson',1)
firstbook.PrintDetails()
secondbook=Book('White Fang','Jack London',2)
secondbook.PrintDetails()
firstcd=CD('And Justice For All','Metallica',3)
firstcd.PrintDetails()
secondcd=CD('Dark Side of the Moon','Pink Floyd',4)
secondcd.PrintDetails()
thirdcd=CD('Nine Track Mind','Charlie Puth',5)
thirdcd.SetGenre('Hip-Pop')
thirdcd.PrintDetails()
print(thirdcd.GetGenre())






