current_users = ['conner', 'elisha', 'eli', 'cason', 'noah']
new_users = ['josiah', 'jhon', 'Conner', 'james', 'tyler']
lower_new =[item.lower() for item in new_users]
lower_current = [item.lower() for item in current_users]
print(lower_new)
for new_user in new_users:
    if new_user in current_users:
        print("that username is alredy taken please enter a new one.")
    else:
        print("nice username.")