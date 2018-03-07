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
        print(self.__ItemID,',',self.__OnLoan,',',self.__DueDate)

class Book(LibraryItem):
    def __init__(self,t,a,i):
        LibraryItem.__init__(self,t,a,i)
        self.__IsRequested=False
        self.__RequestedBy=0

    def GetIsRequested(self):
        self.__IsRequested=True

    def PrintDetails(self):
        print('Book Details')
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

    def PrintDetails(self):
        print('CD Details')
        LibraryItem.PrintDetails(self)
        print(self.__Genre)
        

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








