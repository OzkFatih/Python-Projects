class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class AuthenticationSystem:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        if username in self.users:
            print("Username already exists.")
            return False
        self.users[username] = User(username, password)
        print("Registration successful.")
        return True

    def login(self, username, password):
        if username not in self.users:
            print("Username not found.")
            return False
        if self.users[username].password == password:
            print("Login successful.")
            return True
        else:
            print("Incorrect password.")
            return False

# Example usage
auth_system = AuthenticationSystem()

while True:
    print("\nChoose an action:")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        auth_system.register(username, password)
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        auth_system.login(username, password)
    elif choice == "3":
        break
    else:
        print("Invalid choice.")
