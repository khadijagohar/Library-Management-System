class User:
    borrowed_books = []

    @classmethod
    def borrow(cls, book_name):
        cls.borrowed_books.append(book_name)
        with open("borrowed.txt", "a") as file:
            file.write(book_name + "\n")
        print(f"You have borrowed '{book_name}'")
    @classmethod
    def return_book(cls, book_return):
        found = False
        with open("borrowed.txt", "r") as file:
            lines = file.readlines()
        with open("borrowed.txt", "w") as file:
            for line in lines:
                if book_return not in line:
                    file.write(line)
                else:
                    found = True
        if found:
            print("Removed successfully")
        else:
            print("Not found")
    @classmethod
    def show(cls):
        try:
            with open("borrowed.txt", "r") as file:
                lines = file.readlines()
                if not lines:
                    print("No book borrowed")
                else:
                    for line in lines:
                        print(line.strip())

        except FileNotFoundError:
            print("File not found")
            


