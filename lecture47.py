'''
Lecture 47 : การใช้งาน Break และ Continue
ิbreak=คำสั่งออกจากloop
continue=คำสั่งให้มีการข้ามคำสั่งต่อไปในloop forรอบนั้นๆ


example:break ในแต่ละposition
for x in range(12):
    break #ใส่breakไว้ตรงนี้ loopข้างล่างจะไม่ทำงาน ทุกอย่างจะถูกfreeze
    for y in range(12):
        print(x+1,"x",y+1,"=",(x+1)*(y+1)) 
    #break ลองใส่breakไว้ตรงนี้ ผลลัพธ์จะคูณแค่แม่1เพราะtabเข้ามา1tabอยู่ในเงื่อนไขของfor x พอทำงานครบloop12รอบ 
        #break ใส่ตรงนี้ผลลัพธ์จะทำงานx+1=0+1 รันไป ถึง12ในขณะที่yถูกfreezingไว้ที่y+1=0+1=1เท่านั้นไม่วนกลับไปทำloop
             #ออกมันloop y แต่loop xยังวิ่งอยู่  

''' 

#continue
for val in "hello":
    if val=="l":
        #break ถ้าใส่breakพอเจอค่าlแล้วก็จะหยุดทำงาน
        continue #พอเจอค่าlแล้วก็จะข้ามไปแล้วทำงานที่ตัวอื่นต่อ
    print(val)
print("The end")
