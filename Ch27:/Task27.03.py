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

borrower=Borrower('A','a@163.com',1)
borrower.updateitemsonloan(10)
borrower.printdetails()
borrower.updateitemsonloan(10)
borrower.printdetails()


        
    
