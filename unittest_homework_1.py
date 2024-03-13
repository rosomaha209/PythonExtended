# Імпортуємо необхідні модулі для unit тестування
import unittest

from homework_1 import Book, User, Member, Library


class TestBookClass(unittest.TestCase):
    def setUp(self):
        self.book = Book("Test Title", "Test Author", "Test ISBN")

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Test Title")
        self.assertEqual(self.book.author, "Test Author")
        self.assertEqual(self.book.isbn, "Test ISBN")

    def test_book_str(self):
        self.assertEqual(str(self.book), "Title: Test Title, Author: Test Author, ISBN: Test ISBN")


class TestUserClass(unittest.TestCase):
    def setUp(self):
        self.user = User("Test User", 123)

    def test_user_creation(self):
        self.assertEqual(self.user.name, "Test User")
        self.assertEqual(self.user.user_id, 123)

    def test_user_str(self):
        self.assertEqual(str(self.user), "User: Test User, ID: 123")


class TestMemberClass(unittest.TestCase):
    def setUp(self):
        self.member = Member("Test Member", 456)
        self.book = Book("Test Title", "Test Author", "Test ISBN")

    def test_checkout_book(self):
        self.member.checkout_book(self.book)
        self.assertIn(self.book, self.member.books_checked_out)

    def test_return_book(self):
        self.member.checkout_book(self.book)
        self.member.return_book(self.book)
        self.assertNotIn(self.book, self.member.books_checked_out)


class TestLibraryClass(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book = Book("Test Title", "Test Author", "Test ISBN")
        self.member = Member("Test Member", 456)

    def test_add_book(self):
        self.library.add_book(self.book)
        self.assertIn(self.book, self.library.list_of_books)

    def test_register_user(self):
        self.library.register_user(self.member)
        self.assertIn(self.member, self.library.list_of_users)

    def test_checkout_book(self):
        self.library.add_book(self.book)
        self.library.register_user(self.member)
        self.library.checkout_book(456, self.book)
        self.assertIn(self.book, self.member.books_checked_out)


# Функція для запуску усіх тестів
def run_tests():
    unittest.main(argv=[''], exit=False)


class TestLibraryCheckoutBook(unittest.TestCase):
    def setUp(self):
        # Створення тестової бібліотеки та користувачів
        self.library = Library()
        self.user1 = Member("User One", 1)
        self.user2 = Member("User Two", 2)
        self.book1 = Book("Book One", "Author One", "ISBN1")
        self.book2 = Book("Book Two", "Author Two", "ISBN2")
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.register_user(self.user1)
        self.library.register_user(self.user2)

    def test_checkout_book_already_checked_out(self):
        # Сценарій, коли книга вже взята іншим користувачем
        self.library.checkout_book(self.user1.user_id, self.book1)
        with self.assertRaises(Exception) as context:
            self.library.checkout_book(self.user2.user_id, self.book1)
        self.assertTrue('This book is already checked out' in str(context.exception))

    def test_checkout_book_to_unregistered_user(self):
        # Спроба взяти книгу незареєстрованим користувачем
        unregistered_user = Member("Unregistered User", 99)
        with self.assertRaises(Exception) as context:
            self.library.checkout_book(unregistered_user.user_id, self.book1)
        self.assertTrue('User not registered' in str(context.exception))

    def test_checkout_book_not_in_library(self):
        # Спроба взяти книгу, якої немає в бібліотеці
        non_existent_book = Book("Non-Existent Book", "No Author", "No ISBN")
        with self.assertRaises(Exception) as context:
            self.library.checkout_book(self.user1.user_id, non_existent_book)
        self.assertTrue('Book not in library' in str(context.exception))


# Додавання нових тестів до функції запуску
def run_additional_tests():
    # Тест на випадок, коли книга вже взята
    # Тест на спробу взяти книгу незареєстрованим користувачем
    # Тест на спробу взяти книгу, якої немає в бібліотеці
    unittest.main(argv=[''], exit=False)


# Приклад виклику функції запуску тестів
run_tests()
# Приклад виклику функції запуску додаткових тестів
run_additional_tests()
