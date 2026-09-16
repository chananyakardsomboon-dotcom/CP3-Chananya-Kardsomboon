'''
Lecture 40 : การใช้งานเงื่อนไขซ้อนเงื่อนไข (Nested Condition)

if True:
    {print("Hello Welcome !") #ถ้าเงื่อนไขถูกต้องจะทำงานบล็อกใหญ่นี่
    if True: #การTabเท่ากันกับเงื่อนไขข้างบนซึ่งมันทำงานอยู่ในกรอบเดียวกัน เสมือนว่า{เครื่องหมายปีกาprintแรกกับสิ้นสุดconditionที่สอง}
        print("Yo ! Beauty girl")} #กรอบเล็ก
        if True:
            print("Haha")

if False: #ถ้าเป็นfalseจะไม่แสดงผลเพราะไม่ตรงตามเงื่อนไขทุกตัว
    print("Hello Welcome !") #ถ้าเงื่อนไขถูกต้องจะทำงานบล็อกใหญ่นี่
    if True: #การTabเท่ากันกับเงื่อนไขข้างบนซึ่งมันทำงานอยู่ในกรอบเดียวกัน เสมือนว่า{เครื่องหมายปีกาprintแรกกับสิ้นสุดconditionที่สอง}
        print("Yo ! Beauty girl") #กรอบเล็ก
        if True:
            print("Haha")

'''

usernameInput=input("Enter Username :")
passwordInput=input("Enter Password :")
if usernameInput=="May" and passwordInput=="1234":
    print("Log in successfully")

    print("----------Ready Cal-PRO--------")
    print("1.Vat7% Calulator")
    print("2.Price Caculator")

    userSelected=int(input("Select module>>>>>"))
    if userSelected==1:
        print("--------welcome to vat7% calculator--------------------")
        print()
        price=int(input("Enter Product Price (THB)")) #เราแปลงตั้งแต่ข้อมูลเข้ามา
        vat=7
        result=price+(price*vat/100) 
        print(result)
        print("---------------End of work---------------------------")
            
    elif userSelected==2:
        print("------------Sum calculation program-------------------")
        print()
        price1=int(input("Enter first product price>>>"))
        price2=int(input("Enter second product price>>>"))
        result1=(price1+price2)
        
        print(price1,("+"),price2,"Total:",result1)
        
        print()
        print("----------------End of work---------------------------")
    else:
        print("New Feature is coming soon")

elif usernameInput=="Admin" and passwordInput=="1234567":
    print("Log in as Admin")
    print("----------Ready Cal-PRO--------")
    print("1.Vat7% Calulator")
    print("2.Price Caculator")

    userSelected=int(input("Select module>>>>>"))
    if userSelected==1:
        print("--------welcome to vat7% calculator--------------------")
        price=int(input("Enter Product Price (THB)")) #เราแปลงตั้งแต่ข้อมูลเข้ามา
        vat=7
        result=price+(price*vat/100) 
        print(result)
        print("---------------End of work---------------------------")
              
    elif userSelected==2:
        print("------------Sum calculation program-------------------")
        print()
        price1=int(input("Enter first product price>>>"))
        price2=int(input("Enter second product price>>>"))
        result1=(price1+price2)
        
        print(price1,("+"),price2,"Total:",result1)
        
        print()
        print("-------Thank you for using us----------")
    else:
        print("New Feature is coming soon")
else : 
    print("Login fail")

