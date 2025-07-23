customer_name = input("Please input the customer's name:  ")

product_name = input("Please input the product name: ")

greeting = f' Dear {customer_name.title()},'

body = f'Your purchased product: {product_name} is delivered!'

gratitude = ' Thanks for your choosing!' \

email = f'{greeting} \n {body}\n{gratitude}'

print(email)