class Restaurant:
    """
    Docstring for Restaurant
    """
    def __init__(self, restaurant_name, cuisine_type):
        """
        Docstring for __init__
        
        :param self: Description
        :param restaurant_name: Description
        :param cuisine_type: Description
        
       """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restrount(self):
        """
        Docstring for describe_restrount
        
        :param self: Description
        """
        print(f"this restount is called {self.restaurant_name}")
        print(f"it serves {self.cuisine_type} food")
    def open_restueant(self):
        """
        Docstring for open_restueant
        
        :param self: Description
        """
        print("the restount is open")
restaurant = Restaurant("Bub's Burgers and Ice Cream", "americen")
restaurant.open_restueant() 
restaurant.describe_restrount()
restaurant = Restaurant("51 Rainbow Indian Grill & Momo House", "indian")
restaurant.open_restueant() 
restaurant.describe_restrount()
restaurant = Restaurant("Sushi Yama", "japanese")
restaurant.open_restueant() 
restaurant.describe_restrount()