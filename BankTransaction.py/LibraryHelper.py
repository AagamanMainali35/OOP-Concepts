from library import Library,Book
import random , string
library = Library("MyLibrary")
library.register('aagaman',"123")
# # NOTE: Loading sample data before program initialization
# names = ["John Doe", "Jane Smith", "Alice Brown", "Bob Johnson"]

# for name in names:
#     library.register(name)

def generate_book_id():
    return "".join(random.choices(string.ascii_letters + string.digits, k=9))
library.booklist.extend([
    Book(generate_book_id(), "Atomic Habits", "James Clear", 0),
    Book(generate_book_id(), "Clean Code", "Robert C. Martin", 3),
    Book(generate_book_id(), "The Alchemist", "Paulo Coelho", 4),
    Book(generate_book_id(), "Deep Work", "Cal Newport", 6),
    Book(generate_book_id(), "Rich Dad Poor Dad", "Robert Kiyosaki", 2),
    Book(generate_book_id(), "Thinking, Fast and Slow", "Daniel Kahneman", 4),
    Book(generate_book_id(), "The Pragmatic Programmer", "Andrew Hunt", 3),
    Book(generate_book_id(), "Sapiens", "Yuval Noah Harari", 5),
    Book(generate_book_id(), "1984", "George Orwell", 2),
    Book(generate_book_id(), "The Power of Habit", "Charles Duhigg", 4),
    Book(generate_book_id(), "Meditations", "Marcus Aurelius", 3),
    Book(generate_book_id(), "The Lean Startup", "Eric Ries", 4),
    Book(generate_book_id(), "How to Win Friends and Influence People", "Dale Carnegie", 2),
    Book("B14", "The Subtle Art of Not Giving a F*ck", "Mark Manson", 2),
    Book(generate_book_id(), "Principles", "Ray Dalio", 5)
])

def main():
    while True:
        print("\n===== Library Menu =====")
        print("1. Register as a member")
        print("2. List all member")
        print("3. Add Book")
        print("4. Show Available Books")
        print("5. Borrow a Book")
        print("6. Show Borrowed Books ")
        print("7. Quit")

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
            library.borrow_Book()
        elif choice=="6":
            library.show_borrower_list()
        elif choice == "7":
            library.return_book()
        elif choice == "8":
            print("Thanks for coming!")
            break
        else:
            print("Invalid choice. Try again.")
            
main()

# library.register("Hima","123")
# library.list_books()
# library.list_members()
# library.borrow_Book()
# library.show_borrower_list()
# library.list_books()
