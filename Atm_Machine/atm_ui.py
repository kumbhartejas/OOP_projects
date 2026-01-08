import streamlit as st

class Atm:
    def __init__(self):
        self.__pin = ""
        self.__balance = 0

    def check_pin(self, temp):
        return temp == self.__pin

    def create_pin(self, a, b):
        if a == b:
            self.__pin = a
            return "✅ Pin set successfully"
        else:
            return "❌ Pin does not match"

    def deposit(self, pin, amount):
        if self.check_pin(pin):
            self.__balance += amount
            return f"✅ Rs {amount} deposited successfully"
        else:
            return "❌ Incorrect pin"

    def withdraw(self, pin, amount):
        if self.check_pin(pin):
            if amount <= self.__balance:
                self.__balance -= amount
                return f"✅ Rs {amount} withdrawn successfully"
            else:
                return "❌ Insufficient balance"
        else:
            return "❌ Incorrect pin"

    def check_balance(self, pin):
        if self.check_pin(pin):
            return f"💰 Your balance is Rs {self.__balance}"
        else:
            return "❌ Incorrect pin"







# --- Streamlit UI ---
st.title("🏦 SBI ATM Simulator")
st.space()

# Create a single ATM instance
if "atm" not in st.session_state:
    st.session_state.atm = Atm()

atm = st.session_state.atm

col1,col2=st.columns([1,3])
with col1:
 st.space()
 st.space()
 st.space()
 menu = st.radio(
    "Choose an option:",
    ["Create Pin", "Deposit", "Withdraw", "Check Balance"]
 )
with col2:
 if menu == "Create Pin":
    st.subheader("🔑 Create Pin")
    a = st.text_input("Enter new pin", type="password")
    b = st.text_input("Re-enter pin", type="password")
    if st.button("Set Pin"):
        st.success(atm.create_pin(a, b))

 elif menu == "Deposit":
    st.subheader("💵 Deposit Money")
    pin = st.text_input("Enter pin", type="password")
    amount = st.number_input("Enter amount", min_value=1, step=1)
    if st.button("Deposit"):
        st.info(atm.deposit(pin, amount))

 elif menu == "Withdraw":
    st.subheader("💸 Withdraw Money")
    pin = st.text_input("Enter pin", type="password")
    amount = st.number_input("Enter amount", min_value=1, step=1)
    if st.button("Withdraw"):
        st.warning(atm.withdraw(pin, amount))

 elif menu == "Check Balance":
    st.subheader("📊 Check Balance")
    pin = st.text_input("Enter pin", type="password")
    if st.button("Check"):
        st.success(atm.check_balance(pin))

 
