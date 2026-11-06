import sqlite3
from datetime import datetime

class To_do_list:

    def __init__(self):
        self.conn = sqlite3.connect("todo.db")
        self.cur = self.conn.cursor()

        self.cur.execute("""
        create table if not exists users(
            userid text primary key,
            name text,
            email text,
            password text not null
        )
        """)
        self.cur.execute("""
        create table if not exists tasks(
            task_id integer primary key autoincrement,
            userid text,
            task text,
            date date,
            status text,
            foreign key (userid) references users(userid)
        )
        """)
        self.conn.commit()

        self.__current_user = None

    def menu(self):
        while True:
            try:
                choice = int(input("""
1. Create Account
2. Login
3. Add task
4. Display Tasks
5. Mark complete
6. Detele Task
7. Logout
8. Exit

Enter Choice: """))
            except ValueError:
                print("Invalid Input")
                continue

            if choice == 1:
                self.create_account()

            elif choice == 2:
                self.login()

            elif choice == 3:
                self.add_task()
            
            elif choice == 4:
                self.display_task()

            elif choice == 5:
                self.mark_completed()
            
            elif choice == 6:
                self.delete_task()

            elif choice == 7:
                self.logout()
    
            elif choice == 8:
                print("Thank You")
                break

            else:
                print("Invalid Choice")

    def create_account(self):
        while True:
            userid = input("\n Create User ID: ")

            self.cur.execute(
                "select * from users where userid=?",
                (userid,)
            )

            if self.cur.fetchone():
                print("User ID already exists!")
            else:
                break

        name = input("Enter Name: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")

        self.cur.execute(
            "insert into users(userid,name,email,password) values(?,?,?,?)",
            (userid, name, email, password)
        )
        self.conn.commit()
        print("Account Created Successfully")

    def login(self):
        userid = input("Enter User ID: ")
        password = input("Enter Password: ")

        self.cur.execute(
            "select * from users where userid=? and password=?",
            (userid, password)
        )

        if self.cur.fetchone():
            self.__current_user = userid
            print("\n Login Successful")
        else:
            print("\n Invalid User ID or Password")


    def logout(self): 
        self.__current_user=None
        if self.__current_user==None:
            print("\n Logout successfully")

    def add_task(self):
        if self.__current_user is None:
            print("Login require")
            return
        print("\n --- Add New Task ---")
        user=self.__current_user
        task=input("Task: ")
        date=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        status="Pending"

        self.cur.execute(
            "insert into tasks(userid,task,date,status) values(?,?,?,?)",
            (user,task,date,status)
        )
        self.conn.commit()
        print("Task added successfully")
        

    def display_task(self):
        if self.__current_user is None:
            print("Login require")
            return
        print("\n --- Display Tasks ---")
        user=self.__current_user

        self.cur.execute(
            "select * from tasks where userid == ? order by date",(user,)
        )
        alltasks = self.cur.fetchall()
        for task in alltasks :
          print(f"task_id = {task[0]} | '{task[2]}'   | status - {task[4]}         |  created on '{task[3]}' ")

        self.conn.commit()
       
    


    def mark_completed(self):
        if self.__current_user is None:
            print("Login require")
            return
        user=self.__current_user

        print("\n --- Mark Task Completed ---")
     
 
        try:
         task_id = int(input("Enter Task ID: "))

         self.cur.execute(
        "update tasks set status = ? where task_id = ? and userid = ?",
        ("Completed", task_id, user)
    )

         if self.cur.rowcount == 0:
           print("Task ID not found")
         else:
          self.conn.commit()
          print("Task marked as completed")

        except ValueError:
           print("Please enter a valid Task ID")


    
    def delete_task(self):
        if self.__current_user is None:
            print("Login require")
            return
        print("\n --- Delete Task ---")
        user=self.__current_user

        try:
         task_id = int(input("Enter Task ID: "))

         self.cur.execute(
        "delete from tasks where task_id = ? and userid = ?",
        (task_id, user)
    )

         if self.cur.rowcount == 0:
           print("Task ID not found")
         else:
          self.conn.commit()
          print("Task Deleted")

        except ValueError:
           print("Please enter a valid Task ID")
        

 
obj = To_do_list()
obj.menu()
