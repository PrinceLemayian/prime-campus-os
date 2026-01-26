class Student:
  def __init__(self,name):
    self.name=name
    self.courses=[]

  def enroll_student(self):
   print(f"{self.name} is pursuing {self.courses}")

class Course:
  def __init__(self,course_code,course_name):
    self.course_code=course_code
    self.course_name=course_name

course_1=Course(1100,"python")
course_2=Course(1200,"c++")
course_3=Course(1300,"javascript")
course_4=Course(1400,"assembly")