import random

class Student:
    def __init__(self, ชื่อเต็ม, ชื่อเล่น):
        self.name = ชื่อเต็ม
        self.nickname = ชื่อเล่น
        self.value = random.randint(2, 10) 

    def score(self):
        if self.value >= 5:
            print(f"ชื่อ-นามสกุล = {self.name} ชื่อเล่น = {self.nickname} คะแนน = {self.value} สอบผ่าน")
        else:
            print(f"ชื่อ-นามสกุล = {self.name} ชื่อเล่น = {self.nickname} คะแนน = {self.value} ไม่ผ่าน")
student1 = Student("นาย ชิติภัทร โสขะรัตน์", "ไนท์")
student2 = Student("นาย โยธินันท์ แป้นสุข", "ไอก้อง")
student3 = Student("นาย หนึ่งตะวัน แสงสูงเนิน", "กล้า")
student4 = Student("นาย อิทธิพล แสงสว่าง", "บอส")
student5 = Student("นางสาว ปภาดา สุขสำราญ", "นัท")

student1.score()
student2.score()
student3.score()
student4.score()
student5.score()
