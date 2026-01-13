current_users = ['john', 'james', 'judah', 'jaydon', 'gabe']
new_users = ['John', 'james', 'michael', 'sarah', 'gabe']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Username '{new_user}' is already taken. Please choose a different username.")
    else:
        print(f"Username '{new_user}' is available.")