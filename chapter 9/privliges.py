"""this is a module docstring for privliges.py"""
from user import User
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
class Privileges:
    """
    Docstring for Privileges
    """
    def __init__(self):
       """
       Docstring for __init__
       
       :param self: Description
       :param privileges: Description
       """
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
admin_privileges = Privileges()
admin_privileges.show_privileges()  