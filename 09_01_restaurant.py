class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f'{self.name} is a {self.cuisine_type}restaurant.')

    def open_restaurant(self):
        print(f'{self.name}is open tonight.')


restaurant_1 = Restaurant('Perkin"s ','breakfeast ')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
