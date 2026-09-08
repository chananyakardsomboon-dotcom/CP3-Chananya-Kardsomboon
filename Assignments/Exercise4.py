'''
Exercise 4 : ปฏิบัติการทดสอบการใช้งานตัวแปร
1.ตั้งชื่อไฟล์ Exercise4_ชื่อ_ตัวอักษรแรกของนามสกุล.py
2.โจทย์: วันนึงได้รับมอบหมายจากอาจารย์ที่ปรึกษาให้พัฒนาโปรแกรมให้กับทางคณะ โดย ระบบดังกล่าวจะมีการเก็บคะแนนรายบุคคลของผู้เรียนแต่ละท่าน 
ของนักศึกษาชั้นปีที่ 2 เทอม 1" โดยมีรายชื่อวิชาดังนี้

Foundation English
General Business
Introduction to Computer Systems
Computer Programming 
โดยให้ผู้เรียนพัฒนาโปรแกรมโดยสร้างตัวแปรสำหรับเก็บคะแนนผู้เรียนในรายวิชาดังกล่าว โดยคะแนนจะสามารถเป็นตัวเลขทศนิยมได้ และ 
เมื่อได้ตัวแปรมาแล้วให้ทำการแสดงผลออกมาให้ผู้ใช้งานได้เห็นในรูปแบบ

--- Your Score ---
Foundation English : คะแนนที่ได้
General Business    : คะแนนที่ได้
Introduction to Computer Systems : คะแนนที่ได้
Computer Programming : คะแนนที่ได้
'''
#Answer1
foundation_english_score= float(input("Foundation English : คะแนนที่ได้"))
general_business_score=float(input("General Business: คะแนนที่ได้"))
introduction_to_computer_systems_score=float(input("Introduction to Computer Systems : คะแนนที่ได้"))
computer_programming_score=float(input("Computer Programming : คะแนนที่ได้"))

print("-------------------------------Your Score--------------------------------------------")
print("Foundation English               : คะแนนที่ได้",foundation_english_score)
print("General Business                 : คะแนนที่ได้",general_business_score)
print("Introduction to Computer Systems : คะแนนที่ได้",introduction_to_computer_systems_score)
print("Computer Programming             : คะแนนที่ได้",computer_programming_score)

#Answer2
Foundation_English_Score=("") 
General_Business_Score=("")
Introduction_to_Computer_Systems_Score=("")
Computer_Programming_Score=("")
print("----------------------------------Your Score-----------------------------------------")
print("Foundation English               : คะแนนที่ได้",Foundation_English_Score) 
print("General Business                 : คะแนนที่ได้",General_Business_Score)
print("Introduction to Computer Systems : คะแนนที่ได้",Introduction_to_Computer_Systems_Score)
print("Computer Programming             : คะแนนที่ได้",Computer_Programming_Score)