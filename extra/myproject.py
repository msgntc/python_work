
user_input = input("Enter a number don't spell it: ")
while user_input.isdigit():
 print("yes that is a number")
 user_input = input("Enter a number: ")
 
else:
 print("That is not a number or you spelled it, you lose. Goodbye!") 