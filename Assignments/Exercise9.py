'''
Exercise 9 : แบบทดสอบการวนซ้ำแบบ While
'''

#ตัวอย่างเกมทายคำ
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


#while loopโปรแกรมรหัสผ่าน
usernameInput=(input("Enter username:"))
passwordInput=int(input("Enter password"))
while usernameInput!=("admin") or passwordInput!=(1234): #เหตุผลที่ต้องเริ่มconditionแรกด้วย!=ไม่เท่ากับ เพราะต้องทำให้ค่าเป็นไม่จริงดักไว้เพื่อจะตัดloop
    print ("Log in Failed,Please Try again")
    usernameInput=(input("Enter username:"))
    passwordInput=int(input("Enter password"))
print("Log in successfully") #เพราะมันไม่ได้อยู่ลบที่เป็นเท็จตาม!=ข้างบน มันเลยแสดงค่าออกมา


