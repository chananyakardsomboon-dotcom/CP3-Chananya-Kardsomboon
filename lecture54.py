'''
Lecture 54 : ตัวอย่างการพัฒนาโปรแกรมรูปแบบฟังก์ชัน
'''
def loginSection():
    usernameInput=input("Enter Username :")
    passwordInput=input("Enter Password :")
    if usernameInput=="May" and passwordInput=="1234":
        return True
    else:
        return False   
def showMenu():
    print("------------------------Ready Cal-PRO---------------------")
    print("1.Vat7% Calulator")
    print("2.Price Caculator")
def menuSelect():
    userSelected=int(input("Select module>>>>>"))
    return userSelected
def vatCalculate(totalPrice):#โปรแกรมcal vatอย่างเดียว
    vat=7
    result=totalPrice+(totalPrice*vat/100) 
    return result
def priceCalculate():#โปรแกรมคำนวณรวมสินค้าและvat
    price1=int(input("Enter first product price>>>"))
    price2=int(input("Enter second product price>>>"))
    return vatCalculate(price1+price2)    

while not loginSection():
    print("Log in Failed,please try again")

showMenu()
userSelected=menuSelect()
if userSelected==1:
        print("--------welcome to vat7% calculator---------------------")
        print()
        totalPrice=int(input("Enter Product Price (THB)"))
        print(vatCalculate(totalPrice))
        print("---------------End of work---------------------------")
            
elif userSelected==2:
        print("------------Sum calculation program---------------------")
        print()
        print(priceCalculate())
        print()
        print("----------------End of work---------------------")
else:
        print("New Feature is coming soon")






    

