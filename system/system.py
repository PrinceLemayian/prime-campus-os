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
    

    while True:


        if user.role == "Student":
            print("---Student Menu---")
            print("1.View Courses")
            print("2. Enroll")
            print("3. Fees")
            print("4. Home")

            choice = input("Enter option: ")

            if choice == "1" or choice.lower() == "view courses":
                pass
            elif choice == "2" or choice.lower() == "enroll":
                pass
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
            


        

while True:
    current_user = user()
    if current_user is None:
        break

    if not show_menu(current_user):
        break

    print("\n...Redirecting user to login page....\n.")

