class Student:
  def __init__(self,name):
    self.name=name
    self.role="Student"
    self.courses=[]

  def enroll(self, course):
    if course in self.courses:
      print(f"{self.name} is already enrolled in {course.course_name}")
      return
    
    self.courses.append(course)
    print(f"{self.name} enrolled in {course.course_name}")
    
  def view_courses(self):
    if not self.courses:
      print("No courses enrolled yet.")
      return 
    
    print(f"{self.name}'s Courses:")
    for course in self.courses:
      print(f"- {course.course_code}: {course.course_name}")
    
class Course:
  def __init__(self,course_code,course_name):
    self.course_code=course_code
    self.course_name=course_name

