'''
Lecture 32 : การใช้งานคำสั่ง Input เพื่อรับค่าจากผู้ใช้
คำสั่งinputจะให้ค่าออกมาเป็น strเสมอ ไม่ว่าเราจะใส่ตัวเลขหรือตัวอักษร
'''

#โปรแกรม Helloชื่อ
name=input("First name :")
lastName=input("what is your lastname? ")
print("Hello!",name,lastName)


#Homework ทำโปรแกรมบวกเลข
print("-------Welcome to caculator----------")
number1=int(input("Enter your number"))
number2=int(input("Enter your second number"))
print("Total:",number1+number2)