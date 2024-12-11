from pathlib import Path
path = Path('10_files_and_exceptions/guest_book.txt')

print("Enter q to quit")
names = ''
while True:
    names += input("What is your name: ")
    names += ('\n')
    if 'q' in names:
        break
names = names.replace("q", '')
names.strip
path.write_text(names)
