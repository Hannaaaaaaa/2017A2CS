import pickle 
from datetime import date
RECORDSIZE=50

class CarRecord :
   def __init__(self) :
       VehicleID = ""
       VehicleID = VehicleID.ljust(20)
       self.VehicleID = VehicleID.encode('utf-8')
       Registration = " "
       Registration = Registration.ljust(10)
       self.Registration = Registration.encode('utf-8')
       self.DateOfRegistration = None
       self.EngineSize = 0
       self.PurchasePrice = 0.00
       
def InitialiseFile() :
    CarFile = open('CarFile.DAT','wb')
    for i in range(100):  
      Address = i * RECORDSIZE + 1
      CarFile.seek(Address, 0)
      pickle.dump(CarRecord(), CarFile)
    CarFile.close()  
   
def InputNewRecordData() :
    Car = CarRecord()
    VehicleID = input('Vehicle ID: ')
    VehicleID = VehicleID.ljust(20)
    Car.VehicleID = VehicleID.encode('utf-8')
    Registration = input('Registration: ')
    Registration = Registration.ljust(10)
    Car.Registration = Registration.encode('utf-8')
    Car.DateOfregistration =(input('Registration Date: '));
    Car.EngineSize = int(input('Engine size: '))
    Car.PurchasePrice = float(input('Purchaseprice: '))
    return Car

def Hash(reg) :
    address = ord(reg[1]) * RECORDSIZE + 1
    return address

def SaveToFile() :
    Address = Hash(Car.Registration.decode('utf-8'))
    CarFile.seek(Address, 0)
    pickle.dump(Car, CarFile)
    
def OpenFileForUpdate() :
    CarFile = open('CarFile.DAT','rb+') 
    return CarFile

def FindRecord(reg, CarFile) :
    Address = Hash(reg)
    CarFile.seek(Address, 0)
    Car = pickle.load(CarFile) 
    return Car

def OutputData(Car) :
    print("The Vehicle ID is",Car.VehicleID)

    

InitialiseFile()
CarFile = OpenFileForUpdate()
Car = CarRecord()
Answer = input('add record or not： ')
while Answer != 'no' :
   Car = CarRecord()
   Car = InputNewRecordData()
   SaveToFile()
   Answer = input('add another record or not：  ')
Answer = input('find record or not： ')
while Answer != 'no' :
   Reg = input('enter vehicle registration number: ')
   Car = FindRecord(Reg, CarFile)
   OutputData(Car)
   Answer = input('find another record or not：')
CarFile.close()

