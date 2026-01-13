class Restaurant:
    """this is a class about a restrount"""
    def __init__(self, restaurant_name, cuisine_type):
        """this does restorount stuff"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restrount(self):
        """this describes a restourant"""
        print(f"this restount is called {self.restaurant_name}")
        print(f"it serves {self.cuisine_type} food")
    def open_restueant(self):
        """this tells us the restuont is open"""
        print("the restount is open")
        
    def served_number(self):
        """
        Docstring for number_served
        
        :param self: Description
        """
        print(f"{self.number_served} people have been served")
    def set_number_served(self, num_served):
        """
        Docstring for set_number_served
        
        :param self: Description
        :param num_served: Description
        """
        self.number_served = num_served
    def increment_number_served(self, day_served):
        """
        Docstring for increment_number_served
        
        :param self: Description
        :param day_served: Description
        """
        self.number_served += day_served
restaurant = Restaurant("food", "americen")

restaurant.open_restueant() 
restaurant.describe_restrount()
restaurant.served_number()
restaurant.set_number_served(7485)
restaurant.served_number()
restaurant.increment_number_served(325)
restaurant.served_number()