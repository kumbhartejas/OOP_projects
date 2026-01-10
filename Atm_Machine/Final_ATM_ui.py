import streamlit as st 
import time

class Atm:
    def __init__(self):
        self.__users={}
        self.__current_user=None

    def Create_Acc(self,id,pin1,pin2):
        if id in self.__users:
            return "This user already exist"
        if pin1==pin2:
            self.__users[id]={"pin":pin1,"balance":0}
            return "Account created successfully"
        else:
            return "Password not match"

    def login(self,id,pin):
        if id in self.__users and self.__users[id]["pin"]==pin:
            self.__current_user=id
            return "login successfully"
        else:
            return "incorrrect Credentials"

    def logout(self):
        if self.__current_user:
            user=self.__current_user
            self.__current_user=None
            return f"User {user} logged out successfully"
        else:
            return "No Login found"

    def deposit(self,amount):
        if self.__current_user:
            self.__users[self.__current_user]["balance"]+=amount
            return f"Rs {amount} Deposited successfully"
        return "No user Logged in"

    def withdraw(self,amount):
        if self.__current_user:
            self.__users[self.__current_user]["balance"]-=amount
            return f"Rs {amount} Withdraw successfully"
        return "No user Logged in"

    def check_bal(self):
        if self.__current_user:
            return f"Current balance is Rs {self.__users[self.__current_user]["balance"]}"
        else:
            return "No user Logged in"

    def change_pin(self,pin1,pin2):
        if self.__current_user:
            if pin1==pin2:
                self.__users[self.__current_user]["pin"]=pin1
                return "Password changed successfully"
        else:
            return "No user Logged in"





#____________________________________________________________________________________________________

st.markdown(
    "<h1 style='text-align: center; color: navy;'>🏦 ATM Simulator 🏦</h1>",
    unsafe_allow_html=True
)



if "atm" not in st.session_state:
    st.session_state["atm"] = Atm()

atm = st.session_state["atm"]





st.space()
st.space()
col1,col2=st.columns([1,3])

with col1:
    st.space()
    
    menu=st.radio(
        "Choose operation",
        ["Home","Create Account","Deposit money","Withdraw Money","Check Balance","Change Password"]
    )
    if st.button("Logout"):
            st.success(atm.logout())
    


with col2:
    if menu=="Home":
        st.subheader("Welcome to SBI ATM Simmulator")
        st.markdown(" There You can create your Bank Account,Deposit and Withdraw your money")
        st.space()
        st.text("Login with your account")
        id=st.text_input("Enter Your Account no")
        password=st.text_input("Enter Your Password",type="password")
        if st.button("Login"):
         st.success(atm.login(id,password))

    elif menu=="Create Account":
        st.subheader("Create New Account")
        id=st.text_input("Enter Account no")
        pass1=st.text_input("Set Password",type="password")
        pass2=st.text_input("Re-enter Password",type="password")
        if st.button("Create"):
            st.success(atm.Create_Acc(id,pass1,pass2))
        
    elif menu=="Deposit money":
        st.subheader("Deposit money")
        amount=st.number_input("Enter Your Amount",min_value=1)
        if st.button("Deposit"):
            st.success(atm.deposit(amount))

    elif menu=="Withdraw Money":
        st.subheader("Withdraw Money")
        amount=st.number_input("Enter Your Amount",min_value=1)
        if st.button("Withdraw"):
            st.success(atm.withdraw(amount))

    elif menu=="Check Balance":
        st.subheader("Check Balance")
        if st.button("Check Balance"):
            st.success(atm.check_bal())

    elif menu=="Change Password":
        st.subheader("Change Password")    
        new_pass1=st.text_input("Change Password",type="password")
        new_pass2=st.text_input("Re-enter Password",type="password")
        if st.button("Submit"):
            st.success(atm.change_pin(new_pass1,new_pass2))



