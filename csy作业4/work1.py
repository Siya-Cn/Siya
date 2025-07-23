prompt = '请输入客户姓名和购买商品'
prompt += '\n退出请输入“!”'
print(prompt)
user = ''
product = ''

while True :
    user = input('用户姓名：')
    if user == '!' :
        break
    product = input('产品名：')
    greeting = f'Dear {user.title()}'
    body = f'Your purchased product:{product} is delivered!'
    gratitude = 'Thanks for your choosing!'
    email= f'{greeting} \n  {body} \n  {gratitude}'
    print(email)
    

