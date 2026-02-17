import random
import string
from datetime import datetime , timedelta
class Memeber:
    def __init__(self,FullName,ID):
        self.FullName=FullName
        self.ID=ID

class Book:
    def __init__(self, BookID, Title, Author, Copies):
        self.BookID = BookID
        self.Title = Title
        self.Author = Author
        self.Copies = int(Copies)

class Library:
    def __init__(self, Name):
        self.Name = Name
        self.member_list=[]
        self.booklist = []
        self.borrower_list={}
        
    def register(self,Fullname,id=None):
        if id is None:
            id="".join(random.choices(string.ascii_letters+string.digits,k=9))
        self.member_list.append(Memeber(FullName=Fullname,ID=id))
        
    def list_members(self):
        print("-"*35)
        print(f"{"SN":<5} {"MemeberID":<15}{"Name"} ")
        print("-"*35)
        for index,persons in enumerate(self.member_list):
            print(f'{index+1:<5}{persons.ID:<15}{persons.FullName}')
            
    def add_book(self):
        book_ID = print("".join(random.choices(string.ascii_letters+string.digits,k=9)))
        book_title = input("Enter book title: ")
        book_author = input("Enter book author: ")

        try:
            book_copies = int(input("Enter book copies amount: "))
        except ValueError:
            print("Copies must be a number.")
            return

        self.booklist.append(Book(book_ID, book_title, book_author, book_copies))
        print("Book added successfully.")

    def list_books(self):
        if not self.booklist:
            print("No books available.")
            return
        else:
            print(f'{"SN":<3} {"Book Name":<32} {"Author Name":<30} {"Available_Copies"}')
            print("-" * 75)
            for i, b in enumerate(self.booklist, 1):
                print(f"{b.BookID:<4} {b.Title[:20]+"...":<30}  {b.Author:<30} {b.Copies}")
              
    def borrow_Book(self):
        book_id = input("Enter Book ID: ")
        member_id = input("Enter Member ID: ")
        borrowing_days = int(input("Enter Borrowing Time in Days: "))
        borrowing_ID="".join(random.choices(string.ascii_letters+string.digits,k=9))
        borrowed_time = datetime.now()  
        returning_time = borrowed_time + timedelta(days=borrowing_days) 
        self.borrower_list[borrowing_ID] = {
            "book_id": book_id,
            "member_id": member_id,
            "BorrowedTime": borrowed_time.strftime("%Y-%m-%d %H:%M:%S"),
            "ReturningTime": returning_time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
    def show_borrower_list(self):
        print(self.borrower_list)
    

