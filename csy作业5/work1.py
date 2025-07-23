orders = [
    {'buyer_name':'Pony','product':'MacBook','email':'pony@qq.com','phone':13812341234},
    {'buyer_name':'Bill','product':'AirPods','email':'bill@ms.com','phone':13812341235},
    {'buyer_name':'Hank','product':'iPhone','email':'hank@xyz.com','phone':13812341239}
]

class Order:
    def __init__(self,buyer_name,product_name,email,phone):
        self.buyer = buyer_name
        self.product = product_name
        self.email = email
        self.phone = phone

    def deliver_mail(self):
        print(f'''to {self.email} \nDear {self.buyer.title():}
             \nYour purchased product:{self.product} is delivered!
             \nThanks for your choosing!''')
        
    def deliver_sms(self):
        print(f'''to {self.phone} \nDear {self.buyer.title():}
             \nYour purchased product:{self.product} is delivered!
             \nThanks for your choosing!''')
        
for one_order in orders:
    message = Order(one_order['buyer_name'],one_order['product'],
                    one_order['email'],one_order['phone'])
    message.deliver_mail()
    message.deliver_sms()


