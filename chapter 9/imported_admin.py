from privliges import Admin, Privileges
admin_user = Admin("Josiah", "Cruz")
admin_user.describe_user()
admin_user.greet_user()
admin_privileges = Privileges()
admin_privileges.show_privileges()  