
class Atm: 
    def __init__(self):
        self.__pin=""
        self.__balance=0
        self.menu()

    
    def menu(self):
        while True:
         user_input=input("""
                        Hello, how would you like to proceed?
                         1.Enter 1 to create pin
                         2.Enter 2 to deposit
                         3.Enter 3 to withdraw
                         4.Enter 4 to check balance
                         5.Enter 5 to change pin
                         5.Enter 6 to exit
                        
     """)
         if user_input=="1":
            self.create_pin()
         elif user_input=='2':
            self.deposit()
         elif user_input=="3":
            self.withdraw()
         elif user_input=='4':
            self.check_balance()
         elif user_input=="5":
            self.set_pin()
         elif user_input=="6":
            break
         elif user_input=="7":
            self.get_pin()
            

    def check_pin(self):
      temp=input("Enter your pin:")
      if temp==self.__pin:
         return True
      else:
         print("Incorrect password")

    def create_pin(self):
        print("\n create pin")
        a=input("Please enter your pin: ")
        b=input("Please re-enter your pin: ")

        if a==b:
         print("Pin set successfully")
         self.__pin=a
        else:
         print("pin does not match")
        
    def deposit(self):
        print("\n Deposit money")
        if self.check_pin():
           amount=int(input("Enter your amount: "))
           self.__balance=self.__balance+amount
           print("Deposit successfully")
        

    
    def withdraw(self):
       print("\n Withdraw money")
       if self.check_pin():
          a=int(input("Amount: "))
          if a<=self.__balance:
             self.__balance=self.__balance-a
             print(f"Rs{a} withdraw successfully")
          else:
             print("Insufficient balance")            
          

    def check_balance(self):
        print("\n Check balance")
        if self.check_pin():
           print(self.__balance)

    def get_pin(self):
       print(self.__pin)
     
    def set_pin(self):
       if self.check_pin():
         new_pin=input("Enter New pin") 
         reenter=input("Re-enter New pin") 
         if new_pin==reenter:
          self.__pin=new_pin
          print("Pin changed successfully")
         else:
            print("pin not match")

sbi=Atm()


  

