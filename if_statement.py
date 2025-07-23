car = 'subaru'
print("If car == 'subaru'? I predict True")
print(car =='subaru')

print("If car == 'audi'? I predict False")
print(car == 'audi')

cars = ['subaru','audi','bmw','byd','porsche','xiaomi']
for one_car in cars:
    if one_car == car:
        print(True)
    else:
        print(False)


age = 8
if age<2 :
    print('This is a baby.')
elif age<4 :
    print('This is a little kid.')
elif age<13 :
    print('This is a kid.')
elif age<18 :
    print('This is a teenage.' )
elif age<65 :
    print('This is an adult.')
else:
    print('This is a senior.')