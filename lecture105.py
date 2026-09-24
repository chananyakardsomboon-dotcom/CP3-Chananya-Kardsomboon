'''
Lecture 105: รู้จักกับการสืบทอดของโปรแกรม Polymorphism
'''
class Vehicle: #classแม่
    licenseNumber=""
    serialCode=""
    def showLicenNumber(self):
        print(self.licenseNumber)
    def showSerial(self):
        print(self.serialCode)
    def turnOnAirConditional(self):
        print("Turn On : Air")

class Car(Vehicle): #classลูกดึงclassแม่มาใช้
    def sayHello(self):
        print("Hello World")

class PickUp(Vehicle): #classลูก
    def loadCargo(self):
        print("Loading cargo...")
class Van(Vehicle): #classลูก
    def openSlideDoor(self):
        print("Open sliding door")
   
class EstateCar(Vehicle): #classลูก
    def openSunRoof(self):
        print("Open sun roof")

car1=Car()
car1.serialCode="py788"
car1.showSerial()
car1.turnOnAirConditional()
car1.sayHello()

PickUp1=PickUp()
PickUp1.turnOnAirConditional()
PickUp1.loadCargo()

Van1=Van()
Van1.turnOnAirConditional()
Van1.openSlideDoor()

EstateCar1=EstateCar()
EstateCar1.turnOnAirConditional()
EstateCar1.openSunRoof()





