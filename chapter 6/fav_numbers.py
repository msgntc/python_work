fav_number = {'nadia': [2, 3], 'judah': [41, 42], 'mom': [41,42], 'naima': [5,6], 'connor': [6,7]}
for name, numbers in fav_number.items():
    print(f"{name}'s favorite numbers are:")
    for number in numbers:
        print(number)


