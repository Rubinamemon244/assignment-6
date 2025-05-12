# 11. Class Method:
#Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
      total_books = 0

      @classmethod
      def increment_book_count(cls):
          cls.total_books +=1

      def __init__(self, title, author):
          self.title = title
          self.author = author

          Book.increment_book_count()

book1 = Book("Harry Potter", "Goblat Of Fire")
book2 = Book("1997", "J.K Rolling")

print(f"Total Books : {Book.total_books}")