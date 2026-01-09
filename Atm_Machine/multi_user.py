class Atm :
    def __init__(self):
        self.__users={}
        self.menu()

    def menu(self):
        print("Welcome to Atm")
        while True:
         print("""
            Please Choose the operation to proceed
              1.Create New Account
              2.Deposit Money
              3.Withdraw Money
              4.Check Balance
              5.Change Password
              6.Exit
""")
         user_input=int(input("Choice: "))
         if user_input==1:
             self.create_account()
         elif user_input==2:
             self.deposit()
         elif user_input==3:
             self.withdraw()
         elif user_input==4:
             self.check_balance()
         elif user_input==5:
             self.change_password()
         elif user_input==6:
             break
         else:
             print("Invalid input")


    def create_account(self):
        print("\n ___Create New Account___")
        Acc_no=input("Enter Account no: ")
        if Acc_no in self.__users:
           print("Account already exist")
           return
        pin1=input("Enter new password: ")
        pin2=input("Re-enter new password: ")
        if pin1==pin2:
            self.__users[Acc_no]={"pin":pin1,"balance":0}
            print("Account created successfully")
        else:
            print("Password does not match")

    def __check_user(self):
        Acc_no=input("Enter your account no: ")
        password=input("Enter your password: ")
        if Acc_no in self.__users and self.__users[Acc_no]["pin"]==password:
            print("Login successfully")
            return Acc_no
        else:
            print("Invalid credentials")


    def deposit(self):
        print("\n ___Deposit Money___")
        user=self.__check_user()
        if user:
            credit=int(input("Enter Amount: "))
            self.__users[user]["balance"]+=credit
            print(f"Rs {credit} deposited successfully")


    def withdraw(self):
        print("\n ___Withdraw Money___")
        user=self.__check_user()
        if user:
            debit=int(input("Enter Amount: "))
            if debit<=self.__users[user]["balance"]:
                self.__users[user]["balance"]-=debit
                print(f"Rs {debit} Withdraw successfully")

    def check_balance(self):
        print("\n ___Check Balance___")
        user=self.__check_user()
        if user:
            print(f"Your current balance is Rs {self.__users[user]["balance"]}")

    def change_password(self):
        print("\n ___Change Password___")
        user=self.__check_user()
        if user:
            new_pin1=input("Enter new password: ")
            new_pin2=input("Re-enter new password: ")
            if new_pin1==new_pin2:
                self.__users[user]["pin"]=new_pin1
                print("Password changed successfully")

            else:
                print("Password does not match")


#object
sbi=Atm()