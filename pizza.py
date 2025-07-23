pizzas = ['apple pizza','cheese pizza','sassage pizza']

for one_pizza in pizzas:
    print(f'I like {one_pizza}')
    print(f'{one_pizza.title()} is of great taste.')

print("I really love pizza!")

friend_pizzas = pizzas[:]
pizzas.append('cream pizza')
friend_pizzas.append('banana pizza')
print(pizzas)
print(friend_pizzas)

for a_pizza in pizzas:
    print(a_pizza)

for b_pizza in friend_pizzas:
    print(b_pizza)