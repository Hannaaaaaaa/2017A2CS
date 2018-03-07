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

    def Borrowing(self):
        self.__OnLoan=False

    def PrintDetails(self):
        print(self.__Title,',',self.__Author__Artist,',',end='')
        print(self.__ItemID,',',self.__OnLoan,',',self__DueDate)

class Book(LibraryItem):
    def __init__(self,t,a,i):
        LibraryItem.__init__(self,t,a,i)
        self.__IsRequested=False
        self.__RequestedBy=0

    def GetIsRequested(self):
        self.__IsRequested=True

class CD(LibraryItem):
    def __init__(self,t,a,i):
        LibraryItem.__init__(self,t,a,i)
        self.__Genre=''

    def GetGenre(self):
        return(self.__Genre)

    def SetGenre(self,g):
        self.__Genre=g

firstbook=Book()





