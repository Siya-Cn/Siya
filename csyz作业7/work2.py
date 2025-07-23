import itertools

prompt ='请输入一个整数n(3<=n<=7)'
prompt += '退出输入“q”\n'

number_list = list(range(1,8))
message = ''
output = []

while message != 'q':
    message = input(prompt)
    if message != 'q':
        for number in number_list:
            if number <= int(message):
                output.append(number)
        result = itertools.permutations(output)
        print(result)
    else:
        break


           
             
       


