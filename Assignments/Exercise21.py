'''
Exercise 21 : เรียนรู้การสร้างโปรแกรม GUI

ให้ทำการพัฒนาโปรแกรมต่อจาก Lecture ที่แล้วโดยเพิ่มการแสดงผลแทนตัวเลขด้วยคำจำกัดความ โดยมีหลักเกณฑ์การแบ่งจากค่า BMI เป็นดังนี้
อ้วนมาก 30.0 ขึ้นไป
อ้วน 25.0 - 29.9
น้ำหนักเกิน 23.0 - 24.9
น้ำหนักปกติ เหมาะสม 18.6 - 22.9
ผอมเกินไป น้อยกว่า 18.5

'''
from tkinter import *
import math

def leftClickButton(event):
    BMI=(float(weightBox.get())/math.pow(float(heightBox.get())/100,2))
    if BMI >=30.0:
        labelResult.configure(text="อ้วนมาก")
    elif BMI >=25.0:
         labelResult.configure(text="อ้วน")
    elif BMI>=23.0:
        labelResult.configure(text="น้ำหนักเกิน")
    elif BMI>=18.6:
        labelResult.configure(text="น้ำหนักปกติ เหมาะสม")
    else:
        labelResult.configure(text="ผอมเกินไป")
MainWindow=Tk()
MainWindow.title("คำนวณBMI")

labelHeight=Label(MainWindow,text="ส่วนสูง(cm.)")
labelHeight.grid(row=0,column=0)
heightBox=Entry(MainWindow)
heightBox.grid(row=0,column=1)

labelWeight=Label(MainWindow,text="น้ำหนัก (Kg.)")
labelWeight.grid(row=1,column=0)
weightBox=Entry(MainWindow)
weightBox.grid(row=1,column=1)

calculateButton=Button(MainWindow,text="คำนวณ")
calculateButton.grid(row=2)

calculateButton.bind('<Button-1>',leftClickButton)

labelResult=Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)

MainWindow.mainloop()