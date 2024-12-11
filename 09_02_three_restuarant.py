class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f'{self.name} is a {self.cuisine_type} restaurant.')

    def open_restaurant(self):
        print(f'{self.name} is now open.')

restaurant_1 = Restaurant('Perkin"s ','breakfeast ')
restaurant_2 = Restaurant("Burger King", 'Fast Food')
restaurant_3 = Restaurant('Apple bee"s', 'Burger and Fries')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
