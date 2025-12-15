while True:
    try:
        if input("Would you like to add two numbers? (yes/no): ").lower() != 'yes':
            print("Goodbye!")
            break
        number_one = int(input("Enter a number: "))
        number_two = int(input("Enter another number: "))
        sum = number_one + number_two
        print(f"The sum of {number_one} and {number_two} is {sum}.") 
    except ValueError:
        print("Please only use integers.")
