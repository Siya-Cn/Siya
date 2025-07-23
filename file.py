from pathlib import Path
path = Path('guest_book.txt')

message = '请输入您的姓名：'
message += '\n退出请输入“quit”'

text = ''
contents = ''
while text != 'quit' :
    text = input(message)
    print(text) 
    if text == 'quit':
        break
    contents += text+'\n'

path.write_text(contents)    


