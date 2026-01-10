class Atm:
    def __init__(self):
       self.__users={}
       self.__current_user=None

    def create_account(self,id,pin1,pin2):
        if id in self.__users:
            print("user alreay exist")
        if pin1==pin2:
            self.__users[id]={"pin":pin1,"balance":0}
            print("user created successfully")
        else:
            print("password does not match")
    
    def login(self,id,pin1):
        if id in self.__users and self.__users[id]["pin"]==pin1:
            self.__current_user=id
            print("login successfully")
            return True
        else:
            print("Invalid credentials")
        
    def logout(self):
        self.__current_user=None
        
    def login_required(func):
        def wrapper(self, *args, **kwargs):
            if self.__current_user is None:
                print("Please login first.")
                return
            func(self, *args, **kwargs)
        return wrapper
    
    @login_required
    def deposit(self,amount):
        if amount>0:
            self.__users[self.__current_user]["balance"]+=amount
            print(f"Rs {amount} withdraw successfully")
        else:
            print("Min 1 rs")
    
    @login_required
    def withdraw(self,amount):
        if amount<=self.__users[self.__current_user]["balance"]:
            self.__users[self.__current_user]["balance"]-=amount
            print(f"Rs {amount} withdraw successfully")
        else:
            print("Insufficient balance")
    
    @login_required
    def check_balance(self):
        print(self.__users[self.__current_user]["balance"])

    @login_required
    def change_password(self,new_pin1,new_pin2):
        if new_pin1==new_pin2:
            self.__users[self.__current_user]["pin"]=new_pin1
            print("new password set successfully")

    


sbi=Atm()
sbi.create_account("tejas",123,123)
sbi.login("tejas",123)
sbi.deposit(100)
sbi.withdraw(10)
sbi.check_balance()
sbi.change_password(111,111)
sbi.logout()
sbi.login("tejas",123)
sbi.deposit(100)

