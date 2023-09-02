from datetime import datetime, timedelta 


class User:
    UserBase = {}

    def __init__(self, firstname, lastname, email, username, password):
        self.first_name = firstname
        self.last_name = lastname
        self.email = email
        self.username = username
        self.password = password
    
    def Add_User(self):
        if self.username not in User.UserBase:
            User.UserBase[self.username] = {'first_name': self.first_name,
                                            'last_name':self.last_name,
                                            'email':self.email, 
                                            'password':self.password }
        else:
            while self.username in User.UserBase:
                  new_username = input("Username is already taken, try another: ")
                  self.username = new_username



class Book_Archive:
    archive = {}
    available_books = []
    books_due_today = []
    books_on_loan = []
    borrowed_books_dictionary = {}

    def __init__(self, title, book_number, image, description):
        self.title = title
        self.book_number = str(book_number) #To differentiate between duplicate books
        self.book_id = str(book_ID(title, book_number))
        self.image = image
        self.description = description
        available_books.append(self.book_id)
    
    def add_book(self):
        Book_Archive.archive[self.book_id] = {'title' : self.title, 
                                              'book_number' : self.book_number,
                                              'image': self.image, 
                                              'description': self.description
                                              }
    
    def new_borrowed_book(self, firstname, lastname, email, date ):
        Book_Archive.borrowed_books_dictionary[self.book_id] = {'title': self.title,
                                                                'first_name': firstname, 
                                                                'last_name': lastname,
                                                                'email': email,
                                                                'return_date': date
                                                                }



def Automatic():
    for key in Book_Archive.archive:
        Book_Archive.available_books.append(key)
    for key in Book_Archive.borrowed_books_dictionary:
        Book_Archive.books_on_loan.append(key)
    for id in Book_Archive.books_on_loan:
        if Book_Archive.borrowed_books_dictionary[id]['return_date'] == datetime.today().strftime('%Y-%m-%d'):
            Book_Archive.books_due_today.append(id)
    print (""" Welcome to Viable Data's Library app
           note: all inputs are case sensitive
           """)



def return_date():
    my_date = datetime.today()
    return (my_date + timedelta(weeks=4)).strftime('%Y-%m-%d')



def book_ID(title, book_number):
    object_list = [title, book_number]
    return str(hash(tuple(object_list)))



def homescreen():
    print("""
          Log in,
          Register""")
    answer = input("Would you like to do?: ")
    if answer == "Log in":
        login()
    elif answer == "Register":
        register()
    else:
        print("""Invalid answer, 
              please choose between Log in and Register""")
        homescreen()



def register():
    first = input("First Name:")
    last = input("Last Name:")
    email = input("Email:")
    username = input("Username:")
    password = input("Password:")
    new_account = User(first,last,email,username,password)
    User.Add_User(new_account)
    print(new_account.username + " has successfully created an account")
    homescreen()



def login():
    username = input("Username:")
    password = input("Password:")
    if username not in User.UserBase:
        print("""
              User not found
              """)
        homescreen()
    if password == User.UserBase[username]['password']:
        global current_account
        current_account = username
        print ("Welcome " + username)
        options(username)
    else:
        print ("""
               Incorrect password
               """)
        homescreen()



def options(user):
    if user == "Admin":
        pass
    else:
        print("""
              View all books,
              View available books,
              View books due today,
              View books loaned out,
              Borrow book,
              Return book,
              Logout,
              Exit 
              """)
        choice = input("What would you like to do?:")
        choice_list = ["View all books","View available books","View books due today","View books loaned out",
                       "Borrow book","Return book","Logout","Exit"]
        while choice not in choice_list:
            choice = input("Please choose a valid choice from the list:")
        if choice == "View all books":
            view_all()
        elif choice == "View available books":
            available_books()
        elif choice == "View books due today":
            due_today_books()
        elif choice == "View books loaned out":
            loaned_out_books()
        elif choice == "Borrow book":
            title = input("Title:")
            book_number = input("Book number:")
            borrow_book(title, book_number)
        elif choice == "Return book":
            title = input("Title:")
            book_number = input("Book number:")
            return_book(title, book_number)
        elif choice == "Logout":
            logout()
        elif choice == "Exit":
            exit()



def view_all():
    print("""This is an exhaustive list of all books in the library,
          along with the book number, an image and a description""")
    for key in Book_Archive.archive:
        print (Book_Archive.archive[key])
    back_button = input("Type \'Back\' to go back to options:")
    while back_button != 'Back':
        back_button = input("""Invalid input,
                            Type \'Back\' to go back to options:""")
    options(current_account)



def available_books():
    print("""This is a list of the books which are available to borrow, 
          along with the corresponding book number""")
    for key in Book_Archive.archive:
        if key in Book_Archive.available_books:
            print (Book_Archive.archive[key]['title'], Book_Archive.archive[key]['book_number'])
        else:
            pass
    back_button = input("Type \'Back\' to go back to options:")
    while back_button != 'Back':
        back_button = input("""Invalid input,
                            Type \'Back\' to go back to options:""")
    options(current_account)



def due_today_books():
    print("""This is a list of the books which are due for return today, 
          along with the details of the borrower""")
    for key in Book_Archive.borrowed_books_dictionary:
        shortcut = Book_Archive.borrowed_books_dictionary[key]
        if key in Book_Archive.books_due_today:
            print (shortcut['title'],
                   shortcut['first_name'],
                   shortcut['last_name'],
                   shortcut['email'])
        else:
            pass
    back_button = input("Type \'Back\' to go back to options:")
    while back_button != 'Back':
        back_button = input("""Invalid input,
                            Type \'Back\' to go back to options:""")
    options(current_account)



def loaned_out_books():
    print("""This is a list of the books which are currently loaned out, 
          along with the details of the borrower""")
    for key in Book_Archive.borrowed_books_dictionary:
        if key in Book_Archive.books_on_loan:
            print (Book_Archive.borrowed_books_dictionary[key])
        else:
            pass
    back_button = input("Type \'Back\' to go back to options:")
    while back_button != 'Back':
        back_button = input("""Invalid input,
                            Type \'Back\' to go back to options:""")
    options(current_account)
            


def borrow_book(title, book_number):
    global current_account
    id = book_ID(title, book_number)
    if id in Book_Archive.available_books:
        book_info = User.UserBase[current_account]
        Book_Archive.borrowed_books_dictionary[str(id)] = {'title': title,
                                                                'first_name': book_info['first_name'], 
                                                                'last_name': book_info['last_name'],
                                                                'email': book_info['email'],
                                                                'return_date': return_date()
                                                 }
        Book_Archive.available_books.remove(str(id))
        Book_Archive.books_on_loan.append(str(id))
        print("Action successfully completed " + title + " has been borrowed" )
        print("The expected date to return this book is: " + return_date())
    else:
        print("This action has been unsuccessful. Check that the correct inputs have been given and if the book is available")
    back_button = input("Type \'Back\' to go back to options:")
    while back_button != 'Back':
        back_button = input("""Invalid input,
                            Type \'Back\' to go back to options:""")
    options(current_account)



def return_book(title, book_number):
    global current_account
    id = book_ID(title, book_number)
    if str(id) in Book_Archive.books_on_loan:
        del Book_Archive.borrowed_books_dictionary[str(id)]
        Book_Archive.books_on_loan.remove(str(id))
        Book_Archive.available_books.append(str(id))
        if str(id) in Book_Archive.books_due_today:
             Book_Archive.books_due_today.remove(str(id))
        print("Action successfully completed " + title + " has been returned")
    else:
        print("This action has been unsuccessful. Check that the correct inputs have been given and if the book is available")
    back_button = input("Type \'Back\' to go back to options:")
    while back_button != 'Back':
        back_button = input("""Invalid input,
                            Type \'Back\' to go back to options:""")
    options(current_account)



def logout():
    global current_account
    current_account = None
    homescreen()
    pass


def exit():
    print("""Thank you for using the app. 
          Come back soon.""")

        










if __name__ == "__main__":
    global current_account
    current_account = None
    Automatic()
    homescreen()
    #username
    #Add dummy class which they are free to use
    #Bigger gap in the print statements
    pass