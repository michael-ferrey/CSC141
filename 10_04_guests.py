from pathlib import Path
path = Path('10_files_and_exceptions/guest.txt')
name = input('What is your name: ')
path.write_text(name) 
