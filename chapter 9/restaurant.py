class Restaurant:
    """this is a class about a restrount"""
    def __init__(self, restaurant_name, cuisine_type):
        """this does restorount stuff"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restrount(self):
        """this describes a restourant"""
        print(f"this restount is called {self.restaurant_name}")
        print(f"it serves {self.cuisine_type} food")
    def open_restueant(self):
        """this tells us the restuont is open"""
        print("the restount is open")
restaurant = Restaurant("food", "americen")

restaurant.open_restueant() 
restaurant.describe_restrount()