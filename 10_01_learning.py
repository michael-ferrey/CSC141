from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

lines = contents
for line in lines: 
    print(line)