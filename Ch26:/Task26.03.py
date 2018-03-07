import pickle 
from datetime import date

class CarRecord :
   def __init__(s) :
       s.VehicleID = ""
       s.Registration = ""
       s.DateOfRegistration = None
       s.EngineSize = 0
       s.PurchasePrice = 0.0
       
def SaveData(Car) :
   f = open('CarFile.DAT','wb')
   for i in range(100):
       pickle.dump(Car[i], f)
   f.close()
   
def LoadData() :
    f = open('CarFile.DAT','rb')
    Car = []  
    EoF = False
    while not EoF :  
        try :
            Car.append(pickle.load(f))
        except :
            EoF = True
    f.close()
    return Car

def OutputRecords(Car) :
   for i in range(100):
       print(Car[i].VehicleID)

def enter():
    i=int(input('Add a new record: '))
    while i != -1 :
        Car[i].VehicleID = input('Vehicle ID: ')
        Car[i].Registration = input('Registration: ')
        Car[i].DateOfregistration =(input('Registration Date: '))
        Car[i].EngineSize = int(input('Engine size: '))
        Car[i].PurchasePrice = float(input('Purchase price: '))
        i = int(input('next Record Number? '))
    return Car
    
       

ThisCar = CarRecord()
Car =[ThisCar for i in range(100)]
Car[0].VehicleID=1

SaveData(Car)  
Car2 = LoadData() 
OutputRecords(Car2)

Car=enter()
SaveData(Car)
Car2=LoadData()
OutputRecords(Car2)

   

