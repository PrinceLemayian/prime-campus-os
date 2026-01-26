class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role # student or admin

def login(users):
    username = input("Enter your username: ")
    
    for user in users:
        if user["username"] == username:
            print(f"Welcome, {username}!, logged in as {user['role']}")
            return User(username, user["role"])
        else:
            print("User not found!")
            return None
            
    