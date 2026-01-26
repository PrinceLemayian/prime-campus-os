class User:
    def __init__(self, role):
        self.role = role

def user():
    print("--Welcome to Greater Heights School--")
    print("[1] Student")
    print("[2] Admin")
    print("[3] Staff ")
    print("[4] Exit")

    choice = input("Select your role: ")

    if choice == "1" or choice.lower() == "student":
        return User("Student")
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

def show_menu(user):
    if user is None:
        return
    
    if user.role == "Student":
        print("---Student Menu---")
        print("1.View Courses")
        print("2. Enroll")
        print("3. Fees")


    elif user.role == "Admin":
        print("---Admin page---")
        print("1.Staff")
        print("2.Students")
        print("3.Courses")
        print("4.Finance")

    elif user.role == "Staff":
        print("---Staff---")
        print("---Credentials---")

current_user = user()
show_menu(current_user)

