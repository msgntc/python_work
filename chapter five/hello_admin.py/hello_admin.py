names = ['jhon', 'james', 'judah', 'jaydon', 'admin']
for name in names:
    if name.lower() == 'admin':
        print("welcome Admin would you like to see status report?")
    else:
        print(f"Welcome {name.title()} thanks for logging in.")