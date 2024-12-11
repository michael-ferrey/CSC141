class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):

        print(f"\nThe restaurant is called {self.restaurant_name} and serves {self.cuisine_type}")
    
    def open_restaurant(self):

        print(f"\n{self.restaurant_name} is now open")

    def set_number_served(self, number_served):

        self.number_served = number_served

    def increment_number_served(self, additional_served):

        self.number_served += additional_served

    
restaurant = Restaurant('Perkins', 'breakfest')
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(f"\nThey have served {restaurant.number_served} people")
restaurant.set_number_served(100)
print(f"\nThey have now served {restaurant.number_served} people")
restaurant.increment_number_served(450)
print(f"\nThey have now served {restaurant.number_served} people")
