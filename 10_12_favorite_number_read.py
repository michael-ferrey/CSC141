from pathlib import Path
import json

path = Path('number.json')
contents = path.read_text()
number = json.loads(contents)
print(f"I remember your favorite number its {number}!")
