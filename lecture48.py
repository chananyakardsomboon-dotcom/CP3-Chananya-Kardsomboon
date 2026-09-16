'''
Lecture 48 : ตัวอย่างการพัฒนาโปรแกรมแบบวนซ้ำ
1
*
2
**
3
***
4
****
5
*****

โจทย์: ต้องการให้ดอกจันออกมาเท่ากับตัวเลขที่พิมพ์ไปแต่ละครั้ง
#กรณีใช้loop
inputnum=(int(input("enter num")))
text=""
for i in range(inputnum):
    text=text+"*"

print(text)


#กรณีไม่ใช้loop
#tirck:จำนวนตัวดอกจันจะเท่ากับจำนวนตัวเลขที่กรอกเข้ามา
inputnumber=(int(input("enter num")))
print(inputnumber*"*") #การคูณกับstrคือการทำซ้ำกับสตริงไปเรื่อยๆ


โจทย์ต่อมาคือถ้าผู้ใช้งานกรอกเลข3ก็จะพิมพ์ขั้นบรรไดมา3ตัว
enter number:3
*
**
***

#วิธีที่1:
inputnum=(int(input("enter num")))
text=""
for i in range(inputnum):
    text=text+"*"
    print(text)


โจทย์:เรียงดอกจันตามขั้นบันได ตามตัวเลขที่ใส่ไป
example: enter number 3:
*
**
***

text=""
inputnum=int(input("Enter num"))
for i in range(inputnum):
    text="" #ใส่textว่างเปล่าให้เบรคดาวน์
    for j in range(i+1):
        text+="*"
    print(text)

#คำตอบแบบสั้น
inputnum=int(input("Enter num"))
for i in range(inputnum):
    print("*"*(i+1))

    

inputnum=(int(input("enter num")))
for i in range(inputnum):
    print("*"*(i+1))

text= ""
print(text)


#ฉบับเต็ม
inputnum=(int(input("enter number")))
text= ""
for x in range(inputnum):
    text=text+"*"
print(text)

#ฉบับย่อ
number=int(input("enter num"))
print(number*"*") #การคูณกับstrคือการทำตัวstrทำไปเรื่อยๆ


3
*
**
***
#ฉบับย่อ
number=int(input("enter num"))
for i in range(number):
    for j in range(i-1)
    print("*"*(i+1)*)



#ฉบับเต็ม
number=int(input("enter num"))
text=""
for i in range(number):
    text=""
    for j in range(i+1):
        text+="*"
    print(text)
'''





