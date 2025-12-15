from random import choice
print("please play responsibly!")
lottery = ['3', '7', '9', '2', '5', '1', '4', '6', '8', '0', 'd', 'c', 'b', 'a', 'f']
lottery_numbers = choice(lottery) + choice(lottery) + choice(lottery) + choice(lottery)
print("Your lottery numbers are: ", lottery_numbers)