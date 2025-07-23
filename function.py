def display_message():
    print('The topic of this unit is function.')

display_message()

def favorite_book(title) :
    print(f'One of my favorite book is {title}.')

favorite_book('Gone with the wind')

def make_shirt(size,character='I love Python'):
    print(f'The shirt is in size{size} with {character}')

make_shirt('big')
make_shirt('small')
make_shirt('medium','Python')

def describe_city(city,country):
    print(f'{city.title()} is in {country.title()}.')

describe_city('beijing','china')

def city_country(city,country):
    message = f'{city},{country}'
    return message.title()

text = city_country('beijing','china')
print(text)

def make_album(singer,name):
    album = {'singer':singer.title(),'name':name.title()}
    return album

finished_album = make_album('jolin','倒带')
print(finished_album)

prompt = '请输入歌手名：'
prompt += '请输入专辑名'
message = ''
while message != 'quit' :
    print()