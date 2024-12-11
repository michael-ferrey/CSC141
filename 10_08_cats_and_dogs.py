from pathlib import Path

cats = Path('10_files_and_exceptions/cats.txt')
dogs = Path('10_files_and_exceptions/dogs.txt')

try:
    print("\nCat names:")
    cats = cats.read_text()
    print(cats) 
except FileNotFoundError:
    print("Sorry we couldn't find your file.")

try:
    print("\n Dog names:")
    dogs = dogs.read_text()
    print(dogs)
except FileNotFoundError:
    print("Sorry we couldn't find your file.")
