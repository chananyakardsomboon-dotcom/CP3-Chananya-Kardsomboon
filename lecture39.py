'''
Lecture 39 : ตัวอย่างการตัดสินใจหลากหลายเงื่อนไข
'''
#โปรแกรมคำนวณเกรด
score=int(input("Score out of (100) :"))
if score>=80:
    print("Grade A") #ถ้ามันเข้าเงื่อนไขใดเงื่อนใขนึงแล้วมันจะไม่เข้าelifต่อจากนี้ ถ้ามันเจอTrueมันทำเงื่อนนั้นเสร็จมันก็ออกมา
elif score>=75:
    print("Grade B+")
elif score>=70:
    print("Grade B")
elif score>=65:
    print("Grade C+")
elif score>=60:
    print("Grade C")
elif score>=55:
    print("Grade D+")
elif score>=50:
    print("Grade D")
else:
    print("Grade F")
'''
ให้สร้างโปรแกรมสำหรับตัดเกรดจากคะแนนโดยที่
A คือ มากกว่าหรือเท่ากับ 80 คะแนน จนถึง 100 คะแนน
B คือ มากกว่าหรือเท่ากับ 70 คะแนน
C คือ มากกว่าหรือเท่ากับ 60 คะแนน
D คือ มากกว่าหรือเท่ากับ 50 คะแนน
F คือ ต่ำกว่า 50 คะแนน จนถึง 0 คะแนน
นอกจากนั้นให้แสดงว่า error
'''