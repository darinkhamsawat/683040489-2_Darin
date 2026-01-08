from P1 import Book, TextBook, Magazine

# Test program
if __name__ == "__main__":
    book = Book("Harry Potter", "B001", "J.K. Rowling")
    book.set_pages(350)
    book.display_info()
    print("-----")

    textbook = TextBook("Physics", "T001", "Serway", "Science", 12)
    textbook.set_pages(500)
    textbook.check_out()
    textbook.display_info()
    print("-----")

    magazine = Magazine("Time", "M001", 202)
    magazine.display_info()