'''
Lecture 46 : การทำงานแบบการวนซ้ำที่ซ้อนกัน

print("2 x 1 = 2")
print("2 x 2 = 4")
print("2 x 3 = 6")
print("2 x 4 = 8")
print("2 x 5 = 10")
print("2 x 6 = 12")
print("2 x 7 = 14")
print("2 x 8 = 16")
print("2 x 9 = 18")
print("2 x 10 = 20")
print("2 x 11 = 22")
print("2 x 12 = 24")

x=1
y=2*x
print("2 x",x,"=",y)
x=x+1
y=2*x
print("2 x",x,"=",y)


#แบบฉบับเต็มของอาจารย์
for x in range(12): 
    x=x+1 #มันคือค่า0+1=1 (ตัวคูณ) และเรียงบวกเพิ่มไป 1+1=2, 2+1=3 ต่อไปจนถึง12
    y=2*x
    print("2 x",x,"=",y)

#แบบฉบับย่อ
for x in range(12):
    print("2 x",x+1,"=",2*(x+1))

#ฉบับinput
inputnum=(int(input("enter num")))
for x in range(12):
    print(inputnum,"x",x+1,"=",(inputnum*(x+1)))

#ฉบับวนloopในตัวมันเอง NOTE ใส่ทดไว้กรณีนี้printออกมาสูตรคูณจะเริ่มที่แม่0 ถึงแม่11 
เพราะค่าxเริ่มต้นที่ศูนย์ ศูนย์+หนึ่งได้=หนึ่ง ศูนย์+สอง=สอง
for x(0)in range(12): #loopใหญ่ สูตรคูณแม่ เริ่มที่แม่2ไปถึงแม่12
    for y(0) in range(12):#loopเล็ก ภายในสูตรคูณตัวหารเริ่มที่1 ถึง 12
        print(x(0),"x",y(0)+1,"=",x(0)*(y+1))



#ฉบับวนloopในตัวมันเอง ครบ12แม่
for x in range(12): #loopใหญ่ สูตรคูณแม่ เริ่มที่แม่2ไปถึงแม่12
    for y in range(12):#loopเล็ก ภายในสูตรคูณตัวหารเริ่มที่1 ถึง 12
        print(x,"x",y+1,"=",(x*y+1)+x-1)
    
    


for x in range(12):
    
    for y in range(12):
        print(x+1,"x",y+1,"=",(x+1)*(y+1))


print("2 x 1 =2")
print("2 x 2 =4")

#สูตรคูณแม่สอง
for x in range(12):
    print(2,"x",x+1,"=",2*(x+1))
for x in range(12):
    print(3,"x",x+1,"=",3*(x+1))
for x in range(12):
    print(4,"x",x+1,"=",4*(x+1))
'''
for x in range(12):
    for y in range(12):
        print(x+1,"x",y+1,"=",(x+1)*(y+1)) 
        

