'''
Lecture 99 : เริ่มต้นสร้างโปรแกรมที่ใช้งานได้จริงด้วย Python
'''
from tkinter import *
import math

def leftClickButton(event):
    print(float(weightBox.get())/math.pow(float(heightBox.get())/100,2))
    labelResult.configure(text=float(weightBox.get())/math.pow(float(heightBox.get())/100,2))

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