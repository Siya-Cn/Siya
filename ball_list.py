list = ['mom','dad','yun','yu']
print(f'Dear {list[0]}, \n  Would you like to enjoy a meal with me?')
print(f'Dear {list[1]}, \n  Would you like to enjoj a meal with me?')
print(f'Dear {list[2]}, \n  Would you like to enjoj a meal with me?')
print(f'Dear {list[3]}, \n  Would you like to enjoj a meal with me?')

print(list.pop())
print(list)

list.append('ziao')
print(list)

list.insert(0,'huyang')
list.insert(3,'ru')
list.append('ming')
print(list)
print(f'Dear {list[0]}, \n  Would you like to enjoy a meal with me?')
print(f'Dear {list[1]}, \n  Would you like to enjoy a meal with me?')
print(f'Dear {list[2]}, \n  Would you like to enjoy a meal with me?')
print(f'Dear {list[3]}, \n  Would you like to enjoy a meal with me?')
print(f'Dear {list[4]}, \n  Would you like to enjoy a meal with me?')
print(f'Dear {list[5]}, \n  Would you like to enjoy a meal with me?')
print(f'Dear {list[6]}, \n  Would you like to enjoy a meal with me?')

message = "Sorry,I had to tell you that I can just invite 2 person."
print(message)

person1 = list.pop()
print(f'Dear {person1}, \n{message}')

person2 = list.pop()
print(f'Dear {person2}, \n{message}')

person3 = list.pop()
print(f'Dear {person3}, \n{message}')

person4 = list.pop()
print(f'Dear {person4}, \n{message}')

person5 = list.pop(0)
print(f'Dear {person5}, \n{message}')

print(list)