def make_sandwich(*ingredients):
    print(f'Your ordered sandwich with {ingredients} is yammy!')

make_sandwich('sassage')
make_sandwich('mushrooms','beef')
make_sandwich('tomatoes','chicken')


def build_profile(first_name,last_name,*descriptions):
    print(f'Hello {first_name.title()} {last_name.title()} who is')
    for one_description in descriptions:
        print(f'---a(an) {one_description}')

build_profile('taylor','swift','American','singer')
    

def make_car(manufacturer,type,**other_information):
    other_information['manufacturer'] = manufacturer
    other_information['type'] = type
    return other_information

over_car = make_car('subaru','outback',color='blue',tow_package=True)
print(over_car)

