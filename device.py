from typing import List, Dict

class Device():
    """ Its an generic device class to connect and disconnect. """

    def __init__(self, name: str, connected_by: str):
        self.name = name
        self.connected_by = connected_by
        self.is_connected = True

    def __str__(self):
        return f"Device {self.name} is connected by {self.connected_by},\
        \nconnection status: {self.is_connected}"

    def disconnect(self):
        self.is_connected = False
        print(F"Device {self.connected_by} disconnected successfully 😒")


class Printer(Device):
    """Its an Printer class that prints data passesd"""

    def __init__(self, name: str, connected_by: str, capacity: int):
        super().__init__(name=name, connected_by=connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} \n{self.remaining_pages} pages remaining"

    def print_pages(self, page: int, data: list[str]):
        if self.is_connected:
            self.remaining_pages -= page
            print(data)
        else:
            print("Printer is not connected 😡")


class BookShelf:
    def __init__(self):
        self.books: List  = []
    
    def add_books(self, book):
        self.books.append(book)

    def get_books(self):
        new_shelf = []
        for book in self.books:
            book_dict = {}
            book_dict[book.title] = book.__dict__
            new_shelf.append(book_dict)
        return new_shelf

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books.\nBooks: {', '.join(self.books)}"
    

class Book():
    def __init__(self, title: str, total_pages: int, author: str, price: float):
        self.title = title
        self.total_pages = total_pages
        self.author = author
        self.price = price


    def __str__(self):
        return f"title: {self.title}, \nauthor: {self.author}\nprice: {self.price}\ntotal_pages: {self.total_pages}"
    

class BookStore(BookShelf):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return f"book shelfs: A-Z\nbooks: {','.join(self.books)}"
    
    def rent_books(self, title: str, quantity: int = 1):
        # check if book is availabe in the store
        for book in self.bookShelf:
            print(book)
