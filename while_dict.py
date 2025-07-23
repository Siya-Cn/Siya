sandwich_orders = ['pastrami','chicken','salad',
                   'beef','pastrami','pastrami']
finished_sandwiches = []

print('The pastrami has sold out!')
while 'pastrami' in sandwich_orders :
    sandwich_orders.remove('pastrami')
    print(sandwich_orders)

while sandwich_orders:
    sandwiches = sandwich_orders.pop()
    finished_sandwiches.append(sandwiches)
    print(finished_sandwiches)
    print('I made your tuna sandwiches!')
    
print(finished_sandwiches)
print('All the sandwiches have been finished!')
