class course:
    def __init__(self,t,m):
        self.__coursetitle=t
        self.__maxstudents=m
        self.__numberoflessons=0
        self.__courselesson=[]
        self.__courseassessment=assessment

    def addlesson(self,t,d,r):
        self.__numberoflessons+=1
        self.__courselesson.append(lesson(t,d,r))

    def addassessment(self,t,m):
        self.__courseassessment=assessment(t,m)

    def outputcoursedetails(self):
        print(self.__coursetitle, 'maximum number: ', self.__maxstudents)
        for i in range(self.__numberoflessons):
            self.__courselesson[i].outputlessondetails()
        self.__courseassessment.outputassessmentdetails()
        

class lesson:
    def __init__(self,t,d,r):
        self.__lessontitle=t
        self.__durationminutes=d
        self.__requireslab=r

    def outputlessondetails(self):
        print(self.__lessontitle,' Duration:', self.__durationminutes)

class assessment:
    def __init__(self,t,m):
        self.__assessmenttitle=t
        self.__maxmarks=m

    def outputassessmentdetails(self):
        print(self.__assessmenttitle," Max marks:",self.__maxmarks)


Course1 = course("Chemistry", 10)
Course1.addassessment("Orgainc", 100)
Course1.addlesson("Inorganic", 60, False)
Course1.addlesson("Analytical", 120, True)
Course1.addlesson("Equilibrium", 60, False)
Course1.outputcoursedetails()

