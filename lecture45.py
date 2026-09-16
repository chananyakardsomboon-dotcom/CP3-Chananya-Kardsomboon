'''
Lecture 45 : ปฏิบัติการสร้างโปรแกรมวนซ้ำแบบมีจำนวนรอบแน่นอน
ลองสร้างโปรแกรมคำนวณเลขให้ทำงานอัตโนมัติ

inputRound=int(input("please enter number"))
total=0
#print(list(range()))

for x in range(inputRound):
    inputNumber=int(input("x"+(str(x+1)+":"))) #+1ไปเพื่อให้เริ่มนับที่1
    total+= inputNumber
print("sum",total)


inputnumber=int(input("Enter number"))
total=0
for x in range(0,13):
    total*=inputnumber
print(int(input,x,(int(x),"=",total)))
'''
inputround=int(input("Enter number of round")) #รับจำนวนรอบที่ต้องการกรอกข้อมูล
total=0
for x in range(inputround):
    inputnumber=int(input("x"+str(x+1)+":"))  # ปรับตรง str(x+1) ให้ใช้ f-string จะอ่านง่ายขึ้น input_number = int(input(f"x{x+1}: "))
    total+=inputnumber #บวกสะสมค่า
    print(("x"+str(x+1))+"sum",total)# แสดงรอบปัจจุบันและผลรวมสะสม (x+1 เป็น int อยู่แล้ว ไม่ต้องแปลงซ้ำ)
