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
class Admin(User):
    """
    Docstring for Admin
    """
    def __init__(self, first_name, last_name):
        """
        Docstring for __init__
        
        :param self: Description
        :param first_name: Description
        :param last_name: Description
        """
        super().__init__(first_name, last_name)
        self.privileges = ["can do admin stuff", "can ruin other peaple day", "can do normal user stuff too"]
    def show_privileges(self):
        """
        Docstring for show_privileges
        
        :param self: Description
        """
        print("As an Admin, you:")
        for privilege in self.privileges:
            print(f"- {privilege}")
admin_user = Admin("Josiah", "Cruz")
admin_user.describe_user()
admin_user.greet_user()
admin_user.show_privileges()