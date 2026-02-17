import random
import string
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
        
    def register(self,Fullname):
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
                print(f"{i:<4} {b.Title[:20]+"...":<30}  {b.Author:<30} {b.Copies}")
              
    def borrow_Book(self,member_ID,BookID,BorrowingTime):
        pass

library = Library("MyLibrary")
# NOTE: Loading sample data before program initialization
names = [
    "Aagaman Mainali", "John Doe", "Jane Smith", "Alice Brown", "Bob Johnson",
    "Charlie Davis", "Diana Evans", "Ethan Foster", "Fiona Green", "George Harris"
]
for name in names:
    library.register(name)

library.booklist.extend([
    Book("B1", "Atomic Habits", "James Clear", 5),
    Book("B2", "Clean Code", "Robert C. Martin", 3),
    Book("B3", "The Alchemist", "Paulo Coelho", 4),
    Book("B4", "Deep Work", "Cal Newport", 6),
    Book("B5", "Rich Dad Poor Dad", "Robert Kiyosaki", 2),
    Book("B6", "Thinking, Fast and Slow", "Daniel Kahneman", 4),
    Book("B7", "The Pragmatic Programmer", "Andrew Hunt", 3),
    Book("B8", "Sapiens", "Yuval Noah Harari", 5),
    Book("B9", "1984", "George Orwell", 2),
    Book("B10", "The Power of Habit", "Charles Duhigg", 4),
    Book("B11", "Meditations", "Marcus Aurelius", 3),
    Book("B12", "The Lean Startup", "Eric Ries", 4),
    Book("B13", "How to Win Friends and Influence People", "Dale Carnegie", 2),
    Book("B14", "The Subtle Art of Not Giving a F*ck", "Mark Manson", 3),
    Book("B15", "Principles", "Ray Dalio", 5)
])

def main():
    while True:
        print("\n===== Library Menu =====")
        print("1. Register as a member")
        print("2. List all member")
        print("3. Add Book")
        print("4. Show Available Books")
        print("5. Borrow a Book")
        print("6. Quit")

        choice = input("Enter your choice: ")
        if choice=="1":
            name=input('Enter Your Full Name : ')
            library.register(name)
            print('Memeber registration sucessfull')
        elif choice=="2":
            library.list_members()
        elif choice == "3":
            library.add_book()
        elif choice == "4":
            library.list_books()
        elif choice=="5":
            pass
        elif choice == "6":
            print("Thanks for coming!")
            break
        else:
            print("Invalid choice. Try again.")
            
main()




