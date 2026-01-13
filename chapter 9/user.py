class User:
    """
    Docstring for User
    """
    def __init__(self, first_name, last_name):
        """
        Docstring for __init__
        
        :param self: Description
        :param first_name: Description
        :param last_name: Description
        """
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """
        Docstring for describe_user
        
        :param self: Description
        """
        print(f"User: {self.first_name} {self.last_name}")

    def greet_user(self):
        """
        Docstring for greet_user
        
        :param self: Description
        """
        print(f"Hello, {self.first_name} {self.last_name}!")