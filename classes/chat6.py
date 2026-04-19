class Book:
    def __init__(self, title:str, author:str, available_copies:int) -> None:
        if not title.strip() or not author.strip():
            raise ValueError("Title, author cannot be empty")
        if available_copies < 0:
            raise ValueError("Available copies cannot be negative")

        self.title = title
        self.author = author
        self.available_copies = available_copies

    def borrow(self, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        if self.available_copies <= 0 or self.available_copies < quantity:
            raise ValueError("There is no available copies to borrow")
        self.available_copies -= quantity

    def return_book(self, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        self.available_copies += quantity

    def __repr__(self) -> str:
        return f"{self.title}, {self.author}, {self.available_copies}"


class Library:
    def __init__(self) -> None:
        self.books = []

    def add_book(self, book: Book) -> None:
        for b in self.books:
            if (b.title.lower() == book.title.lower() and
                b.author.lower() == book.author.lower()):
                b.available_copies += book.available_copies
                return
        self.books.append(book)

    def remove_book(self, author, title) -> None:
        for b in self.books:
            if (author.lower() == b.author.lower() and
                    title.lower() == b.title.lower()):
                self.books.remove(b)
                return
        raise ValueError("There is no book available to remove")

    def borrow_book(self, title, author, quantity) -> None:
        for b in self.books:
            if (author.lower() == b.author.lower() and
                    title.lower() == b.title.lower()):
                b.borrow(quantity)
                return
        raise ValueError("There is no book available to borrow")

    def return_book(self, title, author, quantity) -> None:
        for b in self.books:
            if (author.lower() == b.author.lower() and
            title.lower() == b.title.lower()):
                b.return_book(quantity)
                return
        raise ValueError("There is no book available to return")

    def list_books(self) -> None:
        for b in self.books:
            print(b.title, b.author, b.available_copies)

    def __repr__(self) -> str:
        return f"{self.books}"




def main():
    library = Library()

    b1 = Book("Harry Potter", "Rowling", 3)
    b2 = Book("Harry Potter", "Rowling", 2)
    b3 = Book("1984", "Orwell", 5)

    library.add_book(b1)
    library.add_book(b2)
    library.add_book(b3)

    library.list_books()

    library.borrow_book("Harry Potter", "Rowling", 4)
    library.return_book("1984", "Orwell", 1)
    library.list_books()


if __name__ == "__main__":
    main()