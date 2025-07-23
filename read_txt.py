from pathlib import Path
path = Path('learning_python.txt')
contents = path.read_text()
print(contents)


for line in contents.splitlines(): 
    print(line.replace('python','c'))

message = 'I really like dogs.'
print(message.replace('dog','cat'))
    

