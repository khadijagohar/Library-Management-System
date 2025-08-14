from admin import Admin
from user import User
class login(Admin ,User):
    def __init__(self , name, password):
        self.name = name 
        self.password = password
    
    def checking(self):
        if (self.name == "admin" and self.password == "sunday"):
            choice = int(input("What do you want to do :- \n1. Add book\n2. Remove book\n3. View all book  \nEnter : "))
            if(choice == 1):
                name = input("Enter book name : ")
                author = input("Enter book's author name : ")
                a = Admin(name , author)
                a.add_book()
            elif(choice == 2):
                name_remove = input("Enter book name you want to remove: ")
                Admin.remove_book(name_remove)
            elif(choice == 3):
                Admin.show()
            else:
                print("Invalid Choice")
        else:
            found = False
            try:
                with open("file.txt" , "r") as file:
                    for line in file:
                        word = line.strip().split(",")   
                        if (len(word)>=2 and word[0] == self.name and word[1] == self.password  ):
                            a = int(input("What do you want to do?  \n1.Borrow a book \n2.Return a book \n3. View currently borrowed books\nEnter : ") )
                            if (a == 1 ):
                                name_of_book = input("Enter name of book you want to borrow:")
                                User.borrow( name_of_book)
                            elif(a == 2 ):
                                book_return = input("Enter name of book you want to return:")
                                User.return_book(book_return)
                            elif(a == 3):
                                User.show()
                                

                            found = True
                            break

                    if not found:
                        print("Wrong username or password")        
                    

            except FileNotFoundError:
                    print("file don't exist")  
while True:
    a = input("login or sign up?\nEnter: ") 
    if a == "login":
        name_of_user = input("Enter username: ")
        passcode = input("Enter password: ")
        l = login(name_of_user , passcode)
        l.checking()
    elif a == "sign up":
        name_n = input("Enter username: ")
        passcode_n = input("Create a password: ")
        with open("file.txt", "a") as file:
            writing = file.write(name_n +","+ passcode_n + "\n")
    else:
        print("Invalid input")


            

        