class Book:
    def __init__(self, title, publisher, pages) -> None:
        self.title = title
        self.publisher = publisher
        self.pages = pages

class EBook(Book):
    def __init__(self, title, publisher, pages, format_) -> None:
        self.title = title
        self.publisher = publisher
        self.pages = pages 
        self.format_ = format_