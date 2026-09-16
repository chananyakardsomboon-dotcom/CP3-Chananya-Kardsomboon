'''
Lecture 52 : ปฏิบัติการสร้างฟังก์ชันที่มีการคืนค่ากลับ (1)

def sayHello(name):
    print("Hello",name)
sayHello("May")  #ทั้งฟังก์ชั่นนี่มันไม่คืนค่ากลับมา

#return
def sayHello(name):
    return("Hello "+ name)
def hello():
     return 10
print(sayHello("May")) #มันจะไม่ขึ้นค่าอะไรกลับมามันเหมือนtype("May")

print(hello())

'''

def add_number(a,b):
    return a+b

result= add_number(10,10)
print(result)