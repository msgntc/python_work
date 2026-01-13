seats = int(input("How many seats do you need? "))
if 8 < seats < 50:
    print("you will have to wait for a table")
elif seats >= 50:
    print("you're gonna need a bigger restaurant")
else:
    print("Your table is ready")