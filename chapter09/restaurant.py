class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        
    def open_restaurant(self):
        print(self.name.title() + " is now open to serve fine " + self.cuisine.title() + " cuisine!")
