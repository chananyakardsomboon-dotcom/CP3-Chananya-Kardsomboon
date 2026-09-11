'''
Exercise 8 : ปฏิบัติการสร้างโปรแกรมจริงบนเงื่อนไข
เขียนโปรแกรมร้านขายของโดยดัดแปลงจากโปรแกรมใน Lecture 40

ในการเข้าใช้งานโปรแกรมให้ผู้ล็อคอินโดยใช้ Username และ Password(ผู้เรียนกำหนดเอง)
หากสำเร็จ โปรแกรมจะขึ้นหน้าต้อนรับและแสดงรายการสินค้าพร้อมราคา (ผู้เรียนกำหนดเอง)
เมื่อเลือกสินค้าที่ต้องการเรียบร้อยแล้ว โปรแกรมจะถามจำนวนที่ต้องการซื้อ
หลังจากผู้ซื้อเลือกเรียบร้อยแล้ว โปรแกรมจะทำการแสดงสรุปราคารวมของรายการสั่งซื้อทั้งหมด

if elif eles (nested condition)
'''
usernameInput=input("Enter Username :")
passwordInput=input("Enter Password :")
if usernameInput=="May" and passwordInput=="1234":

    print("Log in successfully")

    print("----------Welcome to Summer Store--------")
    print()
    print("----------Product list-------------------")
    print("1.Banana:            8 THB.")
    print("2.Apple:            20 THB.")
    print("3.Watermelon:       60 THB.") 
    print("4.Eggs:             80 THB. **Out of Stock**")
    print("5.Hotdogs:          45 THB. **Out of Stock**")
    print("6.Ice cream:       199 THB. **Out of Stock**")
    print("7.Chocolate:       100 THB. **Out of Stock**")
    print("8.Coconut:         140 THB. **Out of Stock**")
    print("9.Lemon:           25 THB.  **Out of Stock**")
    print("10.Onion:          15 THB.  **Out of Stock**")

    bananaPrice=(8)
    applePrice=(20)
    watermelonPrice=(60)

    userSelected=int(input("Please select item number you want>>>>"))
    if userSelected==1:
        print("1. Banana",bananaPrice,"THB")
        quanlity=int(input("How many pieces you want?>>>>"))
        sumtotal_item1=(bananaPrice*quanlity)
        print("Banana",bananaPrice,"x",quanlity,":",sumtotal_item1)
        print("Anything else? >>>")
        print("[2] [3] [0]")
        userSelected=int(input("Please select second item number you want?>>>"))
        if userSelected==2:
            print("2. Apple",applePrice,"x","THB")
            quanlity=int(input("How many pieces you want?>>>>"))
            sumtotal_item2=(applePrice*quanlity)
            print("Apple",applePrice,"x",quanlity,":",sumtotal_item2)
            print("------------------Cashier Department------------------------------------------")
            print("--ATTENTION: Total includes tax for cash and credit card payments.------------")
            sum_product=(sumtotal_item1+sumtotal_item2)
            vat=7
            totalIncludingVat=sum_product+(sum_product*vat/100)
            result=totalIncludingVat
            print(sumtotal_item1,"+",sumtotal_item2,"=",sum_product)
            print("Total included vat7%",result)
            print("--------------------Thank you for shoping with Us-----------------------------")

        elif userSelected==3:
            print("3. Watermelon",watermelonPrice,"x","THB")
            quanlity=int(input("How many pieces you want?>>>>"))
            sumtotal_item3=(watermelonPrice*quanlity)
            print("Watermelon",watermelonPrice,"x",quanlity,":",sumtotal_item3)
            print("------------------Cashier Department------------------------------------------")
            print("--ATTENTION: Total includes tax for cash and credit card payments.------------")
            sum_product=(sumtotal_item1+sumtotal_item3)
            vat=7
            totalIncludingVat=sum_product+(sum_product*vat/100)
            result=totalIncludingVat
            print(sumtotal_item1,("+"),sumtotal_item3,"=",sum_product)
            print("Total included vat7%",result)
            print("--------------------Thank you for shoping with Us-----------------------------")
        else:
            sumtotal_item1=(bananaPrice*quanlity)
            vat=7
            totalIncludingVat=(sumtotal_item1+(sumtotal_item1*vat/100))
            result=totalIncludingVat
            print("------------------Cashier Department------------------------------------------")
            print("--ATTENTION: Total includes tax for cash and credit card payments.------------")
            print("Banana",bananaPrice,"x",quanlity,":",sumtotal_item1)
            print("Total included vat7%",result)
            print("--------------------Thank you for shoping with Us-----------------------------")

            
            
            
    elif userSelected==2:
        print("2. Apple",applePrice,"x","THB")
        quanlity=int(input("How many pieces you want?>>>>"))
        sumtotal_item2=(applePrice*quanlity)
        print("Apple",applePrice,"x",quanlity,":",sumtotal_item2)
        print("[1] [3] [0]")
        userSelected=int(input("Please select second item number you want?>>>"))
        if userSelected==1:
            print("1. Banana",bananaPrice,"THB")
            quanlity=int(input("How many pieces you want?>>>>"))
            sumtotal_item1=(bananaPrice*quanlity)
            print("Banana",bananaPrice,"x",quanlity,":",sumtotal_item1)

            print("------------------Cashier Department------------------------------------------")
            print("--ATTENTION: Total includes tax for cash and credit card payments.------------")
            sum_product=(sumtotal_item2+sumtotal_item1)
            vat=7
            totalIncludingVat=sum_product+(sum_product*vat/100)
            result=totalIncludingVat
            print(sumtotal_item2,"+",sumtotal_item1,"=",sum_product)
            print("Total included vat7%",result)
            print("--------------------Thank you for shoping with Us-----------------------------")
        elif userSelected==3:
            print("3. Watermelon",watermelonPrice,"x","THB")
            quanlity=int(input("How many pieces you want?>>>>"))
            sumtotal_item3=(watermelonPrice*quanlity)
            print("Watermelon",watermelonPrice,"x",quanlity,":",sumtotal_item3)

            print("------------------Cashier Department------------------------------------------")
            print("--ATTENTION: Total includes tax for cash and credit card payments.------------")
            sum_product=(sumtotal_item3)
            vat=7
            totalIncludingVat=sum_product+(sum_product*vat/100)
            result=totalIncludingVat
            print(sumtotal_item2,("+"),sumtotal_item3,"=",sum_product)
            print("Total included vay7%",result)
            print("--------------------Thank you for shoping with Us-----------------------------")
        else:
            sumtotal_item2=(applePrice*quanlity)
            vat=7
            totalIncludingVat=(sumtotal_item2+(sumtotal_item2*vat/100))
            result=totalIncludingVat
            print("------------------Cashier Department------------------------------------------")
            print("--ATTENTION: Total includes tax for cash and credit card payments.------------")
            print("Apple",applePrice,"x",quanlity,":",sumtotal_item2)
            print("Total included vat7%",result)
            print("--------------------Thank you for shoping with Us-----------------------------")
            
            

    elif userSelected==3:
            print("3. Watermelon",watermelonPrice,"x","THB")
            quanlity=int(input("How many pieces you want?>>>>"))
            sumtotal_item3=(watermelonPrice*quanlity)
            print("Watermelon",watermelonPrice,"x",quanlity,":",sumtotal_item3)
            print("[1] [2] [0]")
            userSelected=int(input("Please select second item number you want?>>>"))
            if userSelected==1:
                print("1. Banana",bananaPrice,"THB")
                quanlity=int(input("How many pieces you want?>>>>"))
                sumtotal_item1=(bananaPrice*quanlity)
                print("Banana",bananaPrice,"x",quanlity,":",sumtotal_item1)
                print("------------------Cashier Department------------------------------------------")
                print("--ATTENTION: Total includes tax for cash and credit card payments.------------")
                sum_product=(sumtotal_item3+sumtotal_item1)
                vat=7
                totalIncludingVat=sum_product+(sum_product*vat/100)
                result=totalIncludingVat
                print(sumtotal_item3,"+",sumtotal_item1,"=",sum_product)
                print("Total included vat7%",result)
            elif userSelected==2:
                print("2. Apple",applePrice,"x","THB")
                quanlity=int(input("How many pieces you want?>>>>"))
                sumtotal_item2=(applePrice*quanlity)
                print("Apple",applePrice,"x",quanlity,":",sumtotal_item2)

                print("------------------Cashier Department------------------------------------------")
                print("--ATTENTION: Total includes tax for cash and credit card payments.------------")
                sum_product=(sumtotal_item3+sumtotal_item2)
                vat=7
                totalIncludingVat=sum_product+(sum_product*vat/100)
                result=totalIncludingVat
                print(sumtotal_item3,"+",sumtotal_item2,"=",sum_product)
                print("Total included vat7%",result)
                print("--------------------Thank you for shoping with Us-----------------------------")
            else:
            
                sumtotal_item2=(watermelonPrice*quanlity)
                vat=7
                totalIncludingVat=(sumtotal_item2+(sumtotal_item2*vat/100))
                result=totalIncludingVat
                print("------------------Cashier Department------------------------------------------")
                print("--ATTENTION: Total includes tax for cash and credit card payments.------------")
                print("Watermelon",watermelonPrice,"x",quanlity,":",sumtotal_item3)
                print("Total included vat7%",result)
                print("--------------------Thank you for shoping with Us-----------------------------")

                
else:
        print("Log in failed")
        print("Incorrect username or password.please try again!!")
