class library():
    def __init__(self,list_of_books,lib_name):
        self.lend_data={}
        self.list_of_books=list_of_books
        self.lib_name=lib_name
        
        for books in self.list_of_books:
            self.lend_data[books]=None
    
    def add(self,book_name):
        self.list_of_books.append(book_name)
        self.lend_data[book_name]=None
        
    def display(self):
        for books in enumerate(self.list_of_books):
            print(books)
    def lend_book(self,book_name,book_author):
        if book_name in self.list_of_books :
            if self.lend_data[book_name] is None:
                self.lend_data[book_name]=book_author
            else:
                print("The Book is Taken by",self.lend_data[book_name])

        else:
            print("You Entered book is not here")
        
    def return_book(self,book_name,book_author):
        if book_name in self.list_of_books:
            if self.lend_data[book_name] is not None and self.lend_data[book_name]==book_author:
                self.lend_data[book_name]=None
                print("Return Successful")
            else:
                print("Sorry this book is lended")
        else:
            print("you have written wrong book name")        
    def delete(self,book_name):
        self.list_of_books.remove(book_name)
        self.lend_data.pop(book_name)
    
 
def main():
    list_of_books=['Java','Python','Kotlin','Scala']
    lib_name="Welcome to National Library"
    secret_key=123456
    my_library=library(list_of_books,lib_name)
    print("Welcome to National Library \nFor Display press '1' \nFor Add Book press '2' \nFor Lend Book press '3' \nFor Return Book press '4' \nFor Delete Book press '5' \nFor Exit press '6'")


    exit=False
    while(exit is not True):
        option=int(input("Enter the Option :"))
    
       
        if option==6:
            exit=True
            print("Thank You")
    
        elif option==1:
            my_library.display()  

        elif option==3:
            book_name=input("Which book do you want to lend:")
            book_author=input("Enter the  name:")
            my_library.lend_book(book_name,book_author)  

        elif option == 4:
            book_name=input("Which do you want to return :")
            book_author=input("Enter the name: ") 
            my_library.return_book(book_name,book_author)
        
        elif option == 2:
            book_name=input("Which book do you want to add :")
            my_library.add(book_name)

        elif option == 5:
            password=int(input("Enter the password:"))
            if secret_key==password:
                book_name=(input("Enter the Book Name :"))
                my_library.delete(book_name)
            else:
                print("Wrong Password")


if __name__ =="__main__":
    main()


    