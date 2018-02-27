import pickle 
from datetime import date

class CarRecord :
   def __init__(s) :
       s.VehicleID = ""
       s.Registration = ""
       s.DateOfRegistration = None
       s.EngineSize = 0
       s.PurchasePrice = 0.00
       
def SaveData() :
    f = open('CarFile.DAT','wb')
    for i in range(100):
        pickle.dump(Car[i], f)
    f.close()
    
def LoadData() :
    f = open('CarFile.DAT','rb') 
    Car = []
    Car.append(pickle.load(f))
    Car.append(pickle.load(f))
    Car.append(pickle.load(f))
    Car.append(pickle.load(f))
    Car.append(pickle.load(f))
    f.close()
    return Car

def OutputRecords() :
   for i in range(5):
       print(car[i].VehicleID)
       

ThisCar = CarRecord()
Car =[ThisCar for i in range(100)]
Car[1].vehicleID=24
Car[1].PurchasePrice=8.00
SaveData()
car=LoadData()
OutputRecords()

i = int(input('Record Number? '))
while i != -1:
   Car[i].VehicleID = input('Vehicle ID: ')
   Car[i].Registration = input('Registration: ')
   Car[i].DateOfregistration =input('Registration Date: ');
   Car[i].EngineSize = int(input('Engine size: '))
   Car[i].PurchasePrice = float(input('Purchase price: '))
   i = int(input('next Record Number? '))

SaveData()
car=LoadData()
OutputRecords()

   
