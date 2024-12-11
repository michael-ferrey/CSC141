from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines: 
    print(line)

message = "I like python"
message.replace('python', 'C') 
print(message.replace)
