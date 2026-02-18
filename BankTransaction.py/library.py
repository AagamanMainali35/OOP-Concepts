import random
import string
from datetime import datetime , timedelta
class Member:
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
        self.member_list.append(Member(FullName=Fullname,ID=id))
        print(f"Member {Fullname} registered with ID: {id}")

        
    def list_members(self):
        print("-"*35)
        print(f"{"SN":<5} {"MemeberID":<15}{"Name"} ")
        print("-"*35)
        for index,persons in enumerate(self.member_list):
            print(f'{index+1:<5}{persons.ID:<15}{persons.FullName}')
            
    def add_book(self):
        book_ID = "".join(random.choices(string.ascii_letters+string.digits,k=9))
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
            print(f'{"SN":<15} {"Book Name":<20} {"Author Name":<25} {"Copies"}')
            print("-" * 75)
            for i, b in enumerate(self.booklist, 1):
                print(f"{b.BookID:<15} {b.Title[:12]+"...":<20}  {b.Author:<25} {b.Copies}")
              
    def borrow_Book(self):
        book_id = input("Enter Book ID: ")
        member_id = input("Enter Member ID: ")
        borrowing_days = int(input("Enter Borrowing Time in Days: "))
        book_found = None
        member_found = None

        for i in self.booklist:
            if book_id == i.BookID:
                book_found = i
                break
        

        for j in self.member_list:
            if member_id == j.ID:
                member_found = j
                break

        if not book_found and not member_found:
            print("Invalid Book ID and Member ID provided.")
        elif not book_found:
            print("Invalid Book ID provided.")
        elif book_found.Copies < 1:
            print('Not Enough Copies of the book please try again later')
        elif not member_found:
            print("Invalid Member ID provided.")
        else:
            book_found.Copies-=1
            borrowing_ID = "".join(random.choices(string.ascii_letters + string.digits, k=9))
            borrowed_time = datetime.now()
            returning_time = borrowed_time + timedelta(days=borrowing_days)
            self.borrower_list[borrowing_ID] = {
                "book_id": book_id,
                "member_id": member_id,
                "BorrowedTime": borrowed_time.strftime("%Y-%m-%d %H:%M:%S"),
                "ReturningTime": returning_time.strftime("%Y-%m-%d %H:%M:%S")
            }

            print("Book borrowed successfully.")

    def show_borrower_list(self):
        print(self.borrower_list)
        
    def return_book(self):
        Borowwer_ID = input('Enter Your BorowwerId : ')
        Delete = False
        
        for key, value in self.borrower_list.items():
            if key == Borowwer_ID:
                Delete=True
                returning_time = datetime.strptime(value['ReturningTime'], "%Y-%m-%d %H:%M:%S")
                bookId = value['book_id']
                for i in self.booklist:
                    if i.BookID == bookId:
                        i.Copies += 1
                        Delete = True
                        print('Thanks for Reading !')
                        break  
               
                if datetime.now() > returning_time:
                    print('Fine worth 25$ has been initiated')
        if Delete:
            self.borrower_list.pop(Borowwer_ID)
        else: 
            print('Invalid Borrower ID provided')
