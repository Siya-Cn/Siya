person = {'fist_name':'Justin','last_name':'Bibber','age':28,'city':'Canada'}
print(person['fist_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

number = {'yun':9,'ziao':5,'yu':8,'huyang':6,'ru':1}
print(number['yun'])
print(number['ziao'])
print(number['yu'])
print(number['huyang'])
print(number['ru'])

for key,value in number.items():
    print(f'\nkey:{key} \nvalue:{value}')

dict = {'nile':'egypt','yrllow_river':'china','amazon_river':'brazil'}
for key,value in dict.items():
    print(f'The {key.title()} runs through {value.title()}')