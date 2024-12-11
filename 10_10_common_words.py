from pathlib import Path

book = Path("10_files_and_exceptions/books.txt")

book = book.read_text()
book.splitlines()
try:
    print('\nApproximation of the word the:')
    print(book.count('the'))
    print('\nNumber of the word the:')
    print(book.count('the '))
except FileNotFoundError:
    pass
