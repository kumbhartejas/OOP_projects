# ================= BOOK ==================
class Book:
    def __init__(self, book_id, name, author, copies):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.copies = copies

    def borrow(self):
        if self.copies > 0:
            self.copies -= 1
            print("Book borrowed")
            return True
        print("No copies available")
        return False

    def return_book(self):
        self.copies += 1
        print("Book returned")

    def __str__(self):
        return f"{self.book_id} | {self.name} | {self.author} | Copies: {self.copies}"


# ================= LIBRARY ==================
class Library:
    books = {}   # shared database

    @classmethod
    def add_book(cls, book):
        if book.book_id not in cls.books:
            cls.books[book.book_id] = book
            print(book.name, "added")
        else:
            print("Book ID already exists")

    @classmethod
    def get_book(cls, bid):
        return cls.books.get(bid)

    @classmethod
    def all_books(cls):
        for book in cls.books.values():
            print(book)


# ================= USER ==================
class User:
    def __init__(self):
        self.users = {}
        self.cart = {}   # { user_id : [book_ids] }
        self.current_user = None

    # -------- Account --------
    def create_user(self, uid, name, email, pin):
        self.users[uid] = {"name": name, "email": email, "pin": pin}
        print("User created")

    def login(self, uid, pin):
        if uid in self.users and self.users[uid]["pin"] == pin:
            self.current_user = uid
            print("Login successful")
        else:
            print("Invalid credentials")

    def logout(self):
        self.current_user = None
        print("Logged out")

    # -------- Issue Book --------
    def issue_mybook(self, bid):
        if self.current_user is None:
            print("Login first")
            return

        book = Library.get_book(bid)
        if not book:
            print("Book not found")
            return

        if book.borrow():
            self.cart.setdefault(self.current_user, []).append(bid)
            print("Book issued")

    # -------- Return Book --------
    def return_mybook(self, bid):
        if self.current_user is None:
            print("Login first")
            return

        if self.current_user in self.cart and bid in self.cart[self.current_user]:
            book = Library.get_book(bid)
            book.return_book()
            self.cart[self.current_user].remove(bid)
        else:
            print("This book is not in your cart")

    # -------- View Cart --------
    def check_mycart(self):
        if self.current_user is None:
            print("Login first")
            return

        books = self.cart.get(self.current_user, [])
        if not books:
            print("Cart is empty")
            return

        print("Your Books:")
        for bid in books:
            print(Library.books[bid])


# ================= LOAD LIBRARY ==================
Library.add_book(Book(1,"1984","George Orwell",3))
Library.add_book(Book(2,"Gatsby","Fitzgerald",2))
Library.add_book(Book(3,"AI","Andrew",4))
Library.add_book(Book(4,"URI","Om",1))


# ================= TEST ==================
u1 = User()
u1.create_user(1,"Tejas","a@gmail.com",123)
u1.login(1,123)

u1.issue_mybook(4)
u1.issue_mybook(4)    # No stock
u1.check_mycart()

u1.logout()

u1.create_user(2,"Rahul","r@gmail.com",111)
u1.login(2,111)
u1.check_mycart()    # Empty → not Tejas's books
