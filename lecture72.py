'''
Lecture 72 : การนำ Collection ต่าง ๆ ไปประยุกต์ใช้งาน (2)
'''
menuList=[] 
textFormat="My food"
def showBill():
    print(textFormat.center(20,"-"))
    for number in range(len(menuList)):
        print(menuList[number][0])
        total=0
        for number in range(len(menuList)):
            total=total+int(menuList[number][1])
    print("ยอดรวมสินค้า",total)
    totalprice=total
    vat=7
    result=totalprice+(totalprice*vat/100)
    print("ยอดสุทธิรวม vat",result)
while True:
    menuName=input("Please Enter Menu :")
    if menuName.lower()=="exit":
        break
    else:
        menuPrice=int(input("Price :"))
        menuList.append([menuName,menuPrice])

showBill()









        
       



