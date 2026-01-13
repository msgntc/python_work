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
class IceCreamStand(Restaurant):
    """
    Docstring for IceCreamStand
    """
    def __init__(self, restaurant_name, cuisine_type="ice cream"):
        """
        Docstring for __init__
        
        :param self: Description
        :param restaurant_name: Description
        :param cuisine_type: Description
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
       """
       Docstring for display_flavors
       
       :param self: Description
       :param flavors: Description
       """
       self.flavors = ["vanilla", "chocolate", "strawberry", "mint chip", "cookie dough"]

restaurant = IceCreamStand("the best ice cream ever totally not a marcketing tool to make you come here")
restaurant.open_restueant()
restaurant.describe_restrount()
restaurant.display_flavors()
print("we have the following flavors available:")
for flavor in restaurant.flavors:
    print(f"- {flavor}")
