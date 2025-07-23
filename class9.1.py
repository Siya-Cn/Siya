class Restaurant :
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'The restaurant is named {self.name.title()}')
        print(f'The restaurant  cusine is {self.type}')

    def open_restaurant(self):
        print('The restaurant is oppenning!')

    def get_number_served(self):
        print(f'There are {self.number_served} customers that are served.')

    def inrement_number_served(self,number):
        self.number_served = self.number_served + number

#9.6练习内容
class IceCreamStand(Restaurant) :
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocalate','strawberry','banana']
         
    def show_flavor(self):
        for one_flavor in self.flavors :
            print(one_flavor)

my_icecream_stand = IceCreamStand('icepop','icecream')
my_icecream_stand.show_flavor()


'''  "9.1练习内容
restaurant = Restaurant('spicy','sichuan cuisine')
print(restaurant.name)
print(restaurant.type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.number_served = 100
restaurant.get_number_served()
restaurant.inrement_number_served(50)
restaurant.get_number_served()

other_restaurant = Restaurant('hot','hunan cuisine')
other_restaurant.describe_restaurant()

another_restaurant = Restaurant('light','guangdong cuisine')
another_restaurant.describe_restaurant()
'''

