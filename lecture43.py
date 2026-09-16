'''
Lecture 43 : ปฏิบัติการสร้างโปรแกรมวนซ้ำแบบ While

while True:
    print("hello") #while loopแบบนี้คือ infinity loop เพราะเงื่อนไขเป็นจริงจึงทำงานภายใต้เงื่อนไขนั่น จริงซ้ำๆ ก็จะวนไป
    #กรณีนี่ต้องหาทางให้เงื่อนไขเป็นเท็จจริงจะหยุดทำงาน



correctNumber=17
userGuess=0
while userGuess!= correctNumber : #trueนี้คือเป็นจริงเสมอ จึงต้องทำให้เป็นเท็จ
    userGuess=int(input("please guess number :"))
    if userGuess>correctNumber:
        print("too large")
    elif userGuess<correctNumber:
        print("too small")
    elif userGuess==correctNumber:
        print("That'right")


'''
correctnumber=17
userGuess=1

while userGuess!=correctnumber:
    userGuess=int(input("guess number"))
    if  userGuess==correctnumber:
        print("Correct")
    elif userGuess>correctnumber:
        print("too large")
    elif userGuess<correctnumber:
        print ("too small")







