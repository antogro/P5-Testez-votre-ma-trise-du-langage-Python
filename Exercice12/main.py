class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Titre: {self.title}, Author: {self.author}, Year: {self.year}"


class Library:
    def __init__(self):
        self.books: list[Book] = []
        self.borrow_books: list[Book] = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                return
        print(f"Le livre {book_title} n'est pas dans la bibliothèque.")

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.remove_book(book)
                self.borrow_books.append(book)
                return
        print(f"Le livre {book_title} n'est pas dispo pour emprunt.")

    def return_book(self, book_title):
        for book in self.borrow_books:
            if book.title == book_title:
                self.borrow_books.remove(book)
                self.add_book(book_title)
                return
        print(f"Le livre {book_title} n'est pas emprunté")

    def available_books(self):
        if not self.books:
            print("Pas de livre disponible")
        for book in self.books:
            print(book)

    def borrowed_books(self):
        if not self.borrow_books:
            print("Aucun livre emprunter!")
        for book in self.borrow_books:
            print(book)

def main():

    library = Library()

    # Ajout de livres
    book1 = Book("1984", "George Orwell", 1949)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    print("Livres disponibles :")
    library.available_books()

    # Emprunt d'un livre
    library.borrow_book("1984")

    print("\nLivres disponibles après emprunt :")
    library.available_books()

    print("\nLivres empruntés :")
    library.borrowed_books()

    # Retour d'un livre
    library.return_book("1984")

    print("\nLivres disponibles après retour :")
    library.available_books()

    print("\nLivres empruntés après retour :")
    library.borrowed_books()


if __name__ == "__main__":
    main()
