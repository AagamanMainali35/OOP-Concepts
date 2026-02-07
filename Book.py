class book():
    total_Books=0
    def __init__(self):
        book.total_Books += 1
        
    def booksCounter(self):
        print(f'The total books created till now is {book.total_Books}')
        
        
Book1=book()
Book2=book()
Book3=book()
Book4=book()
Book5=book()
Book5.booksCounter()
