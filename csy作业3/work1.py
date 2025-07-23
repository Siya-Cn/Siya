month = int(input('Please input the month: ')) 

if month>0 and month<4 :
    print('The season is spring.')
elif month<7 :
    print('The season is summer.')
elif month<10 :
    print('The season is autumn.')
elif month<13 :
    print('The season is winter.')
else:
    print('Machine Failure!')


