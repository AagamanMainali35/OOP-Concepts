class Book:
    def __init__(self, BookID, Title, Author, Copies):
        self.BookID = BookID
        self.Title = Title
        self.Author = Author
        self.Copies = int(Copies)


class Library:
    def __init__(self, Name):
        self.Name = Name
        self.booklist = []

    def add_book(self):
        book_ID = input("Enter book ID: ")
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
            print(f'{"SN":<3} {"Book Name":<32} {"Author Name":<30} {"Copies"}')
            print("-" * 75)
            for i, b in enumerate(self.booklist, 1):
                print(f"{i:<4} {b.Title[:20]+"...":<30}  {b.Author:<30} {b.Copies}")


library = Library("MyLibrary")
# NOTE: For testing purpose only
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
        print("1. Add Book")
        print("2. Show Available Books")
        print("3. Quit")

        choice = input("Enter your choice: ")
        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.list_books()
        elif choice == "3":
            print("Thanks for coming!")
            break
        else:
            print("Invalid choice. Try again.")


main()
