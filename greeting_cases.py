'''
names = ['admin','jake','rose','kiki','julie']

for one_name in names:
    if one_name =='admin':
        print(f'Hello {one_name.title()},would you like to see a status report?')
    else:
        print(f'Hello {one_name.title()},thank you for logging in again!')
'''

names = []
if names:
    print('This list is not empty.')
else:
    print('We need to find some users!')