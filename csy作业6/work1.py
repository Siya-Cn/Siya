from pathlib import Path
path = Path('students.txt')
information = path.read_text()
print(information)

