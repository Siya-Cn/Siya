orders = [
    {'buyer_name':'Pony','product':'MacBook'},
    {'buyer_name':'Bill','product':'AirPods'},
    {'buyer_name':'Hank','product':'iPhone'}
]

buyer = []
product = []

#简单方法有吗 为什么最后只接收了Hank一个
def deliver_mail(buyer,product):
    print('')

'''
        buyer.append(one_order['buyer_name'])
        product.append(one_order['product'])
        for one_buyer in buyer:
            greeting = f'Dear {one_buyer},'
        for one_product in product:
            body = f'Your purchased product:{one_product} is delivered!'
        print(f'{greeting} \n  {body} \n  Thanks for your choosing!')
        '''

deliver_mail(buyer,product)

for one_order in orders :
        deliver_mail(one_order['buyer_name'],one_order['product']) 
    
print(f'''{f'Dear {one_order['buyer_name']},'} 
      \n  {f'Your purchased product:{one_order['product']} is delivered!'} 
      \n  Thanks for your choosing!''')