from pathlib import Path
cat = Path('cats.txt')
print(cat.read_text())

dog = Path('dogs.txt')
print(dog.read_text())