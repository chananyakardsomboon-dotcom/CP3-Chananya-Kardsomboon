'''
Exercise 11 : การพัฒนาโปรแกรมจริงที่ใช้งานวนซ้ำ

'''

text=""
rows=int(input("Let's build our pyramid!!"))
for i in range(rows):
    text=""
    print(" " *(rows-i-1)+("* "*(i+1)))
    print(text)
   
print("--Thank you for play with me !!--")
