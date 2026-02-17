class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, additional_served):
        self.number_served += additional_served


restaurant = Restaurant("The Coastal Grill", "Seafood")

print(f"Customers served: {restaurant.number_served}")

restaurant.number_served = 25
print(f"Customers served after update: {restaurant.number_served}")

restaurant.set_number_served(40)
print(f"Customers served after using set_number_served(): {restaurant.number_served}")

restaurant.increment_number_served(15)
print(f"Customers served after increment: {restaurant.number_served}")