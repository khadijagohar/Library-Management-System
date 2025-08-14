class Admin:
    library = []
    def __init__(self , name, author ):
        self.name = name
        self.author = author
        Admin.library.append((name , author))
    @classmethod
    def add_book(cls):
        with open("fileofbooks.txt", "a") as file:
            for i in cls.library:
                file.write(f"Book name : {i[0]} , Author name : {i[1]} \n")
    @classmethod
    def remove_book(cls , name_rev):
        found = False
        with open("fileofbooks.txt", "r") as file:
            lines = file.readlines()
        with open("fileofbooks.txt", "w") as file:
            for line in lines:
                if name_rev not in line:
                    file.write(line)
                else:
                    found = True
        if found:
            print(f"{name_rev} removed successfully")
        else:
            print(f"{name_rev} not found")
    @staticmethod
    def show():
        with open("fileofbooks.txt", "r") as file:
            a = file.read()
            print(a)