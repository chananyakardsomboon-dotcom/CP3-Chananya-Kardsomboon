'''
Lecture 53 : ปฏิบัติการสร้างฟังก์ชันที่มีการคืนค่ากลับ (2)
'''
def vatCalculate(totalprice):
    result=totalprice+(totalprice*7/100)
    return result #ข้างหลังreturn คือ ข้อมูลจะเป็นint,float,str,function,objectจะเป็นตัวแปรหรือตัวอื่นก็ได้


print(vatCalculate(int(input("Enter your price")))) #กรณีเพ่ิมคำถามให้ผู้ใช้งานกรอก
