import random

class Bank:
    def __init__(self):
      self.__database={}
      self.__current_user=None
      

    
    def menu(self):
     while True:
        print("\n1. Create Account")
        print("2. Login")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Check Balance")
        print("6. Change Password")
        print("7. User Details")
        print("8. Logout")
        print("9. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            self.create_acc()
        elif choice == 2:
            self.login()
        elif choice == 3:
            self.deposit()
        elif choice == 4:
            self.withdraw()
        elif choice == 5:
            self.check_bal()
        elif choice == 6:
            self.change_password()
        elif choice == 7:
            self.user_details()
        elif choice == 8:
            self.logout()
        elif choice == 9:
            print("Thank You")
            break
        else:
            print("Invalid Choice")

    def create_acc(self):
        print("----Create New Account----")
        while True:
          name=input("Enter your full name: ")
          dob=input("Enter your DOB (dd-mm-yyyy): ")  # can add date format
          phone=int(input("Enter your phone no: "))   # can add 10 digit num checker
          address=input("Enter your address: ")

          while True:
                acc_no = random.randint(10000000, 99999999)
                if acc_no not in self.__database:
                    break
          
          userid=acc_no

          pass1=input("Enter new Password: ")
          pass2=input("Re-enter the Password: ")

          # Can add code to check password is 8 digit min with uppercase,lowercase,symbol
          if pass1==pass2:
            self.__database[acc_no] = {
                    "name": name,
                    "dob": dob,
                    "phone": phone,
                    "address": address,
                    "password": pass1,
                    "balance": 0
                }
            print("Account created successfully")
            print("Name:",self.__database[acc_no]['name'])
            print("Account number:",acc_no)
            break
          else:
            print("password does not match")

                      
          
    def login(self):
      print()
      print("--- Login ---")
      account_no=int(input("Enter your account number: "))
      password=input("Enter your pin: ")
      
      if account_no in self.__database:
        if self.__database[account_no]['password']==password:
         print("login successfully")
         self.__current_user=account_no  
        else:
            print("Wrong Password")
      else:
        print("Invalid Credentials")



    def logout(self):
        print()
        self.__current_user=None
        if self.__current_user is None:
         print("Logout Successfully")


    def check_login(func):
     def wrapper(self):
        if self.__current_user is None:
            print()
            print("Login Required")
            return
        
        
        print(f"User: {self.__database[self.__current_user]['name']} [{self.__current_user}]")
        return func(self)
     return wrapper


    @check_login
    def deposit(self):
     print()
     print("--- Deposit money ---")
     acc_no = self.__current_user
     
     amount = int(input("Enter Amount: "))
     if amount>0:
       self.__database[acc_no]["balance"] += amount
       print("Amount Deposited Successfully")
     else :
       print("You can not deposit amount in negative")
     
     print("Current Balance:", self.__database[acc_no]["balance"])


    @check_login
    def withdraw(self):
      print()
      print("--- Withdraw money ---")

      acc_no = self.__current_user
      amount = int(input("Enter Amount: "))

      if amount <= self.__database[acc_no]["balance"]:
        self.__database[acc_no]["balance"] -= amount
        print("Amount Withdrawn Successfully")
      else:
        print("Insufficient Balance")

    
      print("Current Balance:", self.__database[acc_no]["balance"])


    @check_login
    def check_bal(self):
     print()
     print("---check Balance---")
     
     acc_no = self.__current_user
     print("Current Balance:",
          self.__database[acc_no]["balance"])



    @check_login
    def change_password(self):
      print()
      print("--- Change Password ---")
      acc_no = self.__current_user

      pass1=input("Enter new Password: ")
      pass2=input("Re-enter the Password: ")
      if pass1==pass2:
        self.__database[acc_no]["password"]=pass1
        print("Password updated successfully")
      else:
        print("Password does not match")


    @check_login
    def user_details(self):
      print()
      print("--- User Details ---")
      acc_no = self.__current_user

      print(f"User Name: {self.__database[acc_no]['name']} ")
      print(f"Phone number: {self.__database[acc_no]['phone']} ")
      print(f"DOB: {self.__database[acc_no]['dob']} ")
      print(f"Address: {self.__database[acc_no]['address']} ")
      print(f"Password: {self.__database[acc_no]['password']} ")
      



u1=Bank()
u1.menu()





