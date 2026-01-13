user_input = input("Enter a number: ")
user_number = int(user_input)
if user_number % 5 == 0:
    print(f"{user_number} is divisible by 5")
else:
    print(f"{user_number} is not divisible by 5")