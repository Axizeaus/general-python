class Book:
    def __init__(self, title, publisher, pages) -> None:
        self.title = title
        self.publisher = publisher 
        self.pages = pages
        
    def reveal(self):
        print('title:', self.title, '\npublisher:', self.publisher, '\npages:', self.pages)

class Ebook(Book):
    def __init__(self, title, publisher, pages, format_) -> None:
        super().__init__(title, publisher, pages)
        self.format_ = format_ 
        
    def reveal(self):
        print('format:', self.format_)
        return super().reveal()
        
ebook = Ebook(
    'Learn python, the snake', 'Programming wildlife associate', 742, 'epub'
)

book = Book(
    'Learn something', 'sommet media', 5
)

print(ebook.title, ebook.format_, ebook.pages, ebook.publisher)
ebook.reveal()
book.reveal()