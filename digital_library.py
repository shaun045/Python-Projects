from typing import Optional, List

#Blueprint
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"You borrowed '{self.title}' by {self.author}.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"You returned '{self.title}'.")
        else:
            print(f"'{self.title}' wasn't borrowed.")

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} --- {status}"


class Library:
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")

    def show_books(self):
        print("\n Library Catalog:")
        for book in self.books:
            print(" -", book)
        print()

    def find_book(self, title: str) -> Optional[Book]:
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None


def handle_borrow(library):
    """ONE job: Handle the borrowing process"""
    title = input("What book would you like to borrow? ").strip()
    if not title:
        print("Title cannot be empty")
        return

    book = library.find_book(title)
    if book:
        book.borrow()
    else:
        print("Book not found")


def handle_return(library):
    """ONE job: Handle the returning process"""
    title = input("Enter the title of the book you want to return: ").strip()
    if not title:
        print("Title cannot be empty")
        return

    book = library.find_book(title)
    if book:
        book.return_book()
    else:
        print("Book not found")


def get_user_choice():
    """ONE job: Get and validate user's main choice"""
    return input("Would you like to borrow a book? (yes/no/exit): ").lower().strip()


if __name__ == "__main__":
    library = Library()

    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)


while True:
    library.show_books()

    choice = get_user_choice()

    if choice == "yes":
        handle_borrow(library)
    elif choice == "no":
        if input("Would you like to return a book? (yes/no): ").lower() == "yes":
            handle_return(library)
    elif choice == "exit":
        print("Thanks for visiting the Library!")
        break
    else:
        print("Invalid input, please try again!")
