'''
Lecture 37 : ตัวอย่างการใช้งานการตัดสินใจใน Python 3
เครื่องหมาย=(ตัวเดียว)หมายถึงการกำหนดค่า
เครื่องหมาย==(สองตัว)หมายถึงการเปรียบเทียบ ซ้ายมือกับขวามือ 


#ลองทำโปรแกรมเข้าสู่ระบบ
usernameInput=(input("Enter Username :"))
passwordInput=int(input("Enter Password :"))
if usernameInput==("chananya.kardsomboon@gmail.com"):
    print()
if passwordInput==12345:
    print("Log in successfully")
else:
    print("Login failed")
'''
usernameInput=input("Enter Username :")
passwordInput=input("Enter Password :")
if usernameInput=="goodday@dd.com" and passwordInput=="1234":
    print("Log in successfully")
else:
    print("log in failed")

