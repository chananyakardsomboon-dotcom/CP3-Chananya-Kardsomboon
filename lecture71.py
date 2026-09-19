'''
Lecture 71 : การนำ Collection ต่าง ๆ ไปประยุกต์ใช้งาน (1)
'''
menuList=[] 
priceList=[]
textFormat="My food"
def showBill():
    print(textFormat.center(20,"-"))
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])       
def total():
    total=0
    for number in range(len(priceList)):
        total+=priceList[number]
    return total
def vatCal():
    vat=7
    totalprice=total()
    result=totalprice+(totalprice*vat/100)
    print("ยอดสุทธิรวม vat",result)

while True:
    menuName=input("Please Enter Menu :")
    if menuName.lower()=="exit":
        break
    else:
        menuPrice=int(input("Price :"))
        menuList.append(menuName)
        priceList.append(menuPrice)        
showBill()
print("ยอดรวมสินค้า",total()) 
vatCal()









        
       



