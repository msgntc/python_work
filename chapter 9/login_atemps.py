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
        self.login_attempts = 0

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
    def increment_login_attempts(self):
        """
        Docstring for increment_login_attempts
        
        :param self: Description
        """
        self.login_attempts += 1
    def reset_login_attempts(self):
        """
        Docstring for reset_login_attempts
        
        :param self: Description
        """
        self.login_attempts = 0
user = User("baned", "person")
user.describe_user()
user.greet_user()
user = User("2344h34he1su2i1dju1", "totaly a normal name")
user.describe_user()
user.greet_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")
user.reset_login_attempts()
print(f"Login attempts: {user.login_attempts}")
