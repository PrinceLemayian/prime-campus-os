import json
from logic.domain_logic import Course, Student

# Loading the courses from courses.json
def load_courses():
    with open("data/courses.json", "r") as file:
        data = json.load(file)
        
    return [Course(c["course_code"], c["course_name"]) for c in data]

def load_users():
    with open("data/users.json", "r") as file:
        return json.load(file)

AVAILABLE_COURSES = load_courses()
class User:
    def __init__(self, username, role):
        self.role = role
        self.username = username


def user():
    
        # loading users
        users = load_users()
        username = input("Enter username: ")

        print("--Welcome to Greater Heights School--")
        for user in users:
            if user["username"].lower() == username.lower():
                role = user["role"].lower()
                
                if role == "student":
                    return Student(user["username"])
                else:
                    return User(role.capitalize())
                
        print("User not found.")
        return None
    
'''
        print("[1] Student")
        print("[2] Admin")
        print("[3] Staff ")
        print("[4] Exit")

        choice = input("Select your role: ")

        if choice == "1" or choice.lower() == "student":
            return Student("Student User")
        elif choice == "2" or choice.lower() == "admin":
            return User("Admin")
        elif choice == "3" or choice.lower() == "staff":
            return User("Staff")
        elif choice == "4" or choice.lower() == "exit":
            print("Goodbye")
            return None
        else:
            print("Invalid choice!!")
            return None

'''
# adding course display + selection helpers

def show_courses(courses):
    print("\n== Available Courses ==")
    for course in courses:
        print(f"{course.course_code} - {course.course_name}")
        
def select_course(courses):
    code = input("Enter course code to enroll: ")
    
    for course in courses:
        if str(course.course_code) == code:
            return course
        
    print("Invalid course code.")
    return None


def show_menu(user):
    if user is None:
        return
    

    while True:


        if user.role == "Student":
            print("---Student Menu---")
            print("1.View Courses")
            print("2. Enroll")
            print("3. Fees")
            print("4. Home")

            choice = input("Enter option: ")

            if choice == "1" or choice.lower() == "view courses":
                show_courses(AVAILABLE_COURSES)
            elif choice == "2" or choice.lower() == "enroll":
                show_courses(AVAILABLE_COURSES)
                course = select_course(AVAILABLE_COURSES)
                
                # Passes the selected course object to enroll()
                if course:
                    user.enroll(course)
            elif choice == "3" or choice.lower() == "fees":
                pass
            elif choice == "4" or choice.lower() == "home":
                return True
            else:
                print("Invalid choice!!")
                



        elif user.role == "Admin":
            print("---Admin page---")
            print("1.Staff")
            print("2.Students")
            print("3.Courses")
            print("4.Finance")
            print("5.Add users")
            print("6. Home")

            choice = input("Enter option: ")

            if choice == "1" or choice.lower() == "staff":
                pass
            elif choice == "2" or choice.lower() == "students":
                pass
            elif choice == "3" or choice.lower() == "courses":
                pass
            elif choice == "4" or choice.lower() == "finance":
                pass
            elif choice == "5" or choice.lower() == "add users":
                pass
            elif choice == "6" or choice.lower() == "home":
                return True
            else:
                print("Invalid choice!!")



        elif user.role == "Staff":
            print("---Staff---")
            print("1.Credentials")
            print("2.Class schedules")
            print("3. Class attendance")
            print("4. Home")

            choice = input("Enter option: ")

            if choice == "1" or choice.lower() == "credentials":
                pass
            elif choice == "2" or choice.lower() =="class schedules":
                pass
            elif choice == "3" or choice.lower() == "class attendance":
                pass
            elif choice == "4" or choice.lower() == "home":
                return True
            else:
                print("Invalid choice!!")
            


        
def run_system():
    while True:
        current_user = user()
        if current_user is None:
            break

        if not show_menu(current_user):
            break

        print("\n...Redirecting user to login page....\n.")

