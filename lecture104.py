'''
Lecture 104 : ลงมือปฏิบัติการ Class, Attribute, Behavior และ Object
'''

class Customer:
    name=""
    lastName=""
    age=0 #ค่าdefaltที่0

    def addCart(self):       
        print("Added Product to",self.name,self.lastName,"'s cart") #เวลาจะดึงข้อมูลในclassมาใช้ในdefใช้self.name หรือself.ข้อมูลอะไรก็ตาม

customer1=Customer()
customer1.name=("May")
customer1.lastName=("Kardsomboon")

customer2=Customer()
customer2.name=("Patrick")
customer2.lastName=("Jane")

customer3=Customer()
customer3.name=("Terasa")
customer3.lastName=("Lisbon")

customer4=Customer()
customer4.name=("Grace")
customer4.lastName=("Van Pelt")

customer5=Customer()
customer5.name=("Wayne")
customer5.lastName=("Rigsby")

customer1.addCart()
customer2.addCart()
customer3.addCart()
customer4.addCart()
customer5.addCart()