
class Book:
    def __init__(self,book_id,book_name,author,copies):
        self.book_id=book_id
        self.book_name=book_name
        self.author=author
        self.copies=copies
        
        

    def borrow(self):
            if self.copies>0:
             self.copies-=1
             print(f"Book borrowed successfully \n")
             return True
            else:
             return False
             

    def return_book(self):
          self.copies+=1
          print("Book return successfully\n")



    def check_avaliablity(self):
          if self.copies>0:
             print("Book is available\n")
             return True
          else :
             print("Book not available\n")
             return False


    def __str__(self):
        return f"{self.book_id}: {self.book_name} by {self.author} ({self.copies} copies)"

  


#----------------------------------------------------------



class Library(Book):
  
  def __init__(self):
     self.books={}
   
  def add_book(self,book:Book):
     if book.book_id not in self.books:
      self.books[book.book_id]=book
      print(f"{book.book_name} book added successfully")
     else:
       print( "\n This book_id is used please choose another id \n")


  def add_booklist(self, books_list):
       for book in books_list:
            self.add_book(book)
       print("\n")

  def remove_book():
      pass

  def view_book(self,id):
     if id in self.books:
        print(f"Book details:\n id:{self.books[id]} \n")
     else:
        print("Id not found \n")

 
  def all_books(self):
        if not self.books:
            print("No books in library\n")
        else:
            print("All books in library:")
            for book in self.books.values():
                print(book)
            


   
lib = Library()
lib.add_booklist([
    Book(1, "1984", "George Orwell", 3),
    Book(2, "The Great Gatsby", "F. Scott Fitzgerald", 2),
    Book(3, "To Kill a Mockingbird", "Harper Lee", 4)
])
#lib.all_books()
# lib.view_book(1)
# lib.view_book(2)
lib.add_book(Book(4,"uri","om",1))



#---------------------------------------------------------------


class User(Book):
    def __init__(self):
       self.user={}
       self.cart={}
       self.current_user=None



#account  (((((((((((((((((((((((
    def create_user(self,id,name,email,password):
       if id in self.user:
          print("user already exist")
       self.user[id]={"name":name,"email":email,"pin":password}
       print("\n user created successfully\n")
      


    def login(self,id,password):
       if id in self.user and self.user[id]["pin"]==password:
          self.current_user=id
          print("login successfully\n")
       else:
          print("Invalid credentials")

    def logout(self):
          if self.current_user is not None:
           self.current_user=None
           print("logout successfully\n")
          else:
           print("No login found")


    def check_login(func):
       def wrap(self,*args,**kwargs):
          if self.current_user is None:
             print("Please login first")
             return
          else:
            user_id = self.current_user
            if user_id in self.user:
                print(f"user: {self.user[user_id]['name']}")

          return func(self,*args,**kwargs)
       return wrap
    
#))))))))))))))))))))))))))))



#User data ((((((((((((((((

    @check_login
    def user_details(self,id):
       if id in self.user:
          print(self.user[id]["name"],self.user[id]["email"],"\n")
       else:
          print("user not found")

    @check_login
    def delete_user(self,id):
       if id in self.user:
          del self.user[id]
          if self.current_user == id:
                self.current_user = None
          print("user deleted successfully \n")
       else:
          print("user not found\n")


#))))))))))))))




#books cart ((((((((((((((((((
   #  @check_login
   #  def issue_mybook(self, library: Library, bid):
   #      if bid in library.books:
   #          book = library.books[bid]
   #          if self.current_user not in self.cart:
   #                  self.cart[self.current_user] = []
   #          self.cart[self.current_user].append(bid)

   #      else:
   #          print("Book_id does not exist\n")

    @check_login
    def issue_mybook(self, library: Library, bid):
     if bid in library.books:
        book = library.books[bid]

        if book.borrow():
            if self.current_user not in self.cart:
                self.cart[self.current_user] = []

            self.cart[self.current_user].append(bid)
        else:
            print("No copies available")
     else:
        print("Book id not present")


    @check_login
    def return_mybook(self, library: Library, bid):
     if self.current_user in self.cart and bid in self.cart[self.current_user]:
        book = library.books[bid]
        book.return_book()
        self.cart[self.current_user].remove(bid)
     else:
        print("This book is not in your cart")

     

    @check_login
    def check_mycart(self, library: Library):
     user_id = self.current_user

     if user_id not in self.cart or not self.cart[user_id]:
        print("Cart is empty")
     else:
        print(f"Cart for {self.user[user_id]['name']}:")
        for bid in self.cart[user_id]:
            book = library.books[bid]
            print(book)


#))))))))))))))))))   




                        
u1=User()
u1.create_user(1,"tejas","abc@gmail.com",123)
u1.login(1,123)
u1.issue_mybook(lib,4)
u1.issue_mybook(lib,4)
# u1.return_mybook(lib,4)
u1.check_mycart(lib)
# u1.issue_mybook(lib,1)
# # u1.delete_user(1)
u1.logout()
u1.create_user(3,"tej","abc@gmail.com",123)
u1.login(3,123)
u1.check_mycart(lib)

# u1.issue_mybook(lib,1)
# u1.user_details(1)






class Admin(User):
    def __init__(self):
        super().__init__()
        pass


