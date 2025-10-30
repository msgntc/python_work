while True:
    ticket = int(input("Enter your age: "))
    if ticket < 3:
        print("Your ticket is free.")
    elif 3 <= ticket <= 12:
        print("Your ticket costs $10.")
    elif ticket > 12:
        print("Your ticket costs $15.")
    else:
        print("Invalid age. Please try again.") 
    continue_ = input("Do you want to check another age? (yes/no): ")
    if continue_ != 'yes':
        break
