import random
random_number = random.randint(1, 1000)
print("I have selected a number between 1 and 1000. Can you guess it? \n(P.S only use integers)")
i = 0 
while True:
    try:
        i += 1
        your_guess = int(input("Enter your guess: "))
        if your_guess < random_number:
            print("Too low")
        elif your_guess > random_number:
            print("Too high")
        elif your_guess > 1000:
            print("That numder is to high.")   
        elif your_guess < 0:
            i -= 1
            print("That numder is to low") 
            i -= 1
        else:
            print("You win. It took you", i, "guesses")
            break
    except ValueError:
        i-= 1
        print("Please use an integer")