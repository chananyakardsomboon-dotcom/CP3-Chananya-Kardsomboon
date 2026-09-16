'''
Lecture 49 : ฟังก์ชันคืออะไร ? แล้วในโปรแกรมมันช่วยอะไร ?
function คือรูปแบบของคำสั่งที่มีจุดมุ่งหมายเดียวกัน ใช้def (define คือการประกาศฟังก์ชั่นว่ามีชื่นว่าอะไร เว้นวรรค ตามด้วยฟังก์ชั่นที่เราคิด)
ชื่อdef+(ชื่อฟังก์ชั่น ต้องสื่อความหมาย ลงท้ายประโยคด้วย: และบรรทัดต่อมาเว้นวรรคtab1)
ในบรรทัดของการแสดงผลprintเรากำหนดค่าไว้ เช่น hello world ต่อมาเราลองพิมพ์บรรทัดใหม่ 
ระบบก็จะแจ้งฟังก์ชั่น addNumber() และออกค่ามาเป็นคำว่า hello world

'''
def sayHelloWorld():
    print("Hello world")
    sayHelloMay()
    print("Woooo")
def sayHelloMay():
    print("Hello May")
    print("Hahaa")
    sayHelloWorld()



sayHelloWorld()
sayHelloMay()


