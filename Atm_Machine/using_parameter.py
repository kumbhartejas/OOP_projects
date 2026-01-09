
class Atm:
    def __init__(self):
        self.__users={}
        self.__current_user=None

    def create_acc(self,id,pin1,pin2):
        if id in self.__users:
            return "User already exist"
        if pin1==pin2:
            self.__users[id]={"pin":pin1,"balance":0}
            return "Account created Successfully"
        else:
            return "Password does not match"
        
    def login(self,id,pin):
        if id in self.__users and self.__users[id]["pin"]==pin:
            self.__current_user=id
            return "Login successfully"
        else:
            return "Incorrect Credentials"
        

    def logout(self):
     if self.__current_user:
        user = self.__current_user
        self.__current_user = None
        return f"User {user} logged out successfully"
     else:
        return "No user is currently logged in"

        
    def deposit(self,amount):
        if self.__current_user:
            self.__users[self.__current_user]["balance"]+=amount
            return f"Rs {amount} deposited successfully"
        return "no user logged in"
        
    def withdraw(self,amount):
        if self.__current_user:
            self.__users[self.__current_user]["balance"]-=amount
            return f"Rs {amount} withdraw successfully"
        return "no user logged in"
        
    def check_bal(self):
        if self.__current_user:
            return f"Your current balance is Rs {self.__users[self.__current_user]["balance"]} "
        return "no user logged in"
    
    def change_pass(self,pin1,pin2):
        if self.__current_user:
            if pin1==pin2:
                self.__users[self.__current_user]["pin"]=pin1
                return "Password changed successfully"
            else:
                return "Password does not match"
        else:
         return "no user logged in"

sbi=Atm()
print(sbi.create_acc("tejas","123","123"))
print(sbi.login("tejas", "123"))
print(sbi.deposit(500))
print(sbi.withdraw(50))
print(sbi.check_bal())
print(sbi.change_pass("111","111"))
print(sbi.logout())
print(sbi.deposit(500))


