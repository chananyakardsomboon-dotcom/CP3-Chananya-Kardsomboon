'''
Lecture 33 : การประยุกต์ใช้งาน Input กับ โปรแกรมที่ใช้งานจริง



#โปรแกรมคำนวณภาษีมูลค่าเพิ่มของสินค้า
price=10000
vat=7
result=price+(price*vat/100) #result+=0.70
print(result)
'''


price=float(input("Enter Product Price (THB)")) #เราแปลงตั้งแต่ข้อมูลเข้ามา
vat=7
result=price+(price*vat/100) 
print(result)

print(type(price))


'''

price=(input("Enter Product Price (THB)")) #กรณที่เราไม่ได้แปลงข้อมูลตอนนำเข้าเป็นstr
vat=7
result=int(price)+(int(price)*vat/100) #ต้องมาแปลงเข้าอีกที และต้องครบทุกตัวแปรไม่งั้นไม่สามารถประมวลผล
print(result)

print(type(price))
'''