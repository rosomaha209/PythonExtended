# Визначаємо клас Book
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"


# Визначаємо базовий клас User
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return f"User: {self.name}, ID: {self.user_id}"


# Створюємо класи наслідування для User: Member та Librarian
class Member(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)
        self.books_checked_out = []

    def checkout_book(self, book):
        self.books_checked_out.append(book)

    def return_book(self, book):
        self.books_checked_out.remove(book)


class Librarian(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)

    def list_checked_out_books(self, user):
        """Функція для виведення списку книг, взятих користувачем.

        Параметри:
        user (User): Користувач, список книг якого потрібно вивести.
        """
        if hasattr(user, 'books_checked_out'):
            print(f"Книги, взяті користувачем {user.name}:")
            for book in user.books_checked_out:
                print(book)
        else:
            print("Цей користувач не має книг.")


# Клас Library для управління бібліотекою
class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_users = []

    def add_book(self, book):
        self.list_of_books.append(book)

    def register_user(self, user):
        self.list_of_users.append(user)

    def checkout_book(self, user_id, book):
        user = next((user for user in self.list_of_users if user.user_id == user_id), None)
        if isinstance(user, Member):
            user.checkout_book(book)


# Приклад використання
book1 = Book("Python Programming", "Eric Matthes", "123456789")
book2 = Book("The Art of Computer Programming", "Donald Knuth", "987654321")
book3 = Book("The C Programming Language", "Brian Kernighan and Dennis Ritchie", "135792468")
book4 = Book("The C++ Programming Language", "Bjarne Stroustrup", "246810121")
book5 = Book("The C# Programming Language", "Microsoft", "369258147")
# створюємо користувачів
user1 = Member("John Doe", 1)
user2 = Member("Jane Smith", 2)
user3 = Member("Bob Johnson", 3)
# створюємо бібліотекаря
librarian = Librarian("Librarian Smith", 9)
# створюємо бібліотеку
library = Library()
# додаємо книги до бібліотеки
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)
# додаємо користувачів до бібліотеки
library.register_user(user1)
library.register_user(user2)
library.register_user(user3)
# додаємо бібліотекаря до бібліотеки
library.register_user(librarian)
# виписати книги
library.checkout_book(1, book1)
library.checkout_book(1, book5)
library.checkout_book(2, book2)
library.checkout_book(3, book3)
# вивести список книг, взятих користувачем
librarian.list_checked_out_books(user1)
# вивести список книг, взятих користувачем
librarian.list_checked_out_books(user2)
# вивести список книг, взятих користувачем
librarian.list_checked_out_books(user3)
# здати книгу взятим користувачем
user1.return_book(book1)
# вивести список книг, взятих користувачем
librarian.list_checked_out_books(user1)
