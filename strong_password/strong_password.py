class Account:

    def __init__(self):
        self.user = {}

    def create_login(self):
        print("----Create Account----")

        id1 = input("Create New User ID: ")
        if len(id1) < 6:
            print("User ID must be at least 6 characters long.")
            return

        pass1 = input("Create New Password: ")
        pass2 = input("Re-enter Password: ")

        if pass1 != pass2:
            print("Both passwords should be equal.")
            return

        if len(pass1) < 8:
            print("Password must be at least 8 characters long.")
            return

        no = "0123456789"
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = lower.upper()
        symbol = "@#$%^&*_-+|\\/?.,"

        # Check for at least one digit
        if not any(ch in no for ch in pass1):
            print("Password must contain at least one digit.")
            return

        # Check for at least one lowercase letter
        if not any(ch in lower for ch in pass1):
            print("Password must contain at least one lowercase letter.")
            return12

        # Check for at least one uppercase letter
        if not any(ch in upper for ch in pass1):
            print("Password must contain at least one uppercase letter.")
            return

        # Check for at least one symbol
        if not any(ch in symbol for ch in pass1):
            print("Password must contain at least one special symbol.")
            return

        self.user[id1] = pass1
        print("Account created successfully!")


u1 = Account()
u1.create_login()