places = ['iceland','britain','sanya','xinjiang','norway']
print(places)

#临时排序
print(sorted(places))
print(places)

#临时反向排序
print(sorted(places,reverse=True))
print(places)

#列表反向
places.reverse()
print(places)

places.reverse()
print(places)

#首字母排序(永久)
places.sort()
print(places)

places.sort(reverse=True)
print(places)

print(f'The first three places in the list are:{places[0:3]}')
print(f'The three places from the middle of the list are:{places[1:4]}')
print(f'The last three places in the list are:{places[2:]}')

