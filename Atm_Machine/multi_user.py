class Atm :

    def __init__(self):
        self.__users={}
        self.menu()
    
    def menu(self):
        print("                                      Welcome To Atm                                 ")
        while True:
         print("""
          Please select the operation
                 1.Create new Account
                 2.Deposit Money
                 3.Withdraw Money
                 4.Check Balance
                 5.Exit
""")
         choice=input("choice: ")
         
         if choice=='1':
            self.create_user()
         elif choice=='2':
            self.deposit()
         elif choice=='3':
            self.withdraw()
         elif choice=="4":
            self.check_balance()
         elif choice=="5":
          print("Thank you for using Atm")
          break
         
         else:
            print("Invalid input")


          
    
    def create_user(self):
        print("\n Create new Account")

        Acc_no=input("Enter New Account no: ")
        if Acc_no in self.__users:
           print("This User Id already exists")
           return
        
        pin1=input("Enter New pin: ")
        pin2=input("Re-Enter your Pin: ")
        if pin1==pin2:
           self.__users[Acc_no]={"pin":pin1,"balance":0}
           print("User created successfully")
        else:
           print("Pin does not match")



    def check_user(self):
          Acc_no=input("Enter your Account no:")
          pas=input("Enter your password:")
          if Acc_no in self.__users and self.__users[Acc_no]["pin"] == pas:
             print("login successfully\n")
             return Acc_no
          else:
             print("Incorrect credentials")
             




    def deposit(self):
       print("\n Deposit Money")
       user=self.check_user()
       if user:
          depo=int(input("Enter Amount: "))
          self.__users[user]["balance"]+=depo
          print(f"Rs {depo} deposited successfully")
                

    def withdraw(self):
       print("\n Withdraw Money")
       user=self.check_user()
       if user:
          take=int(input("Enter Amount: "))
          if take<=self.__users[user]["balance"]:
             self.__users[user]["balance"]-=take
             print(f"Rs {take} Withdraw successfully")
          else:
           print("Insufficient Balance") 


    def check_balance(self):
       print("\n Check Balance")
       user=self.check_user()
       if user:
          print(f"Your current balance is {self.__users[user]["balance"]} Rs")





sbi=Atm()


 
  

