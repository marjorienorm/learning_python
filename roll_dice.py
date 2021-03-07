import random

roll = random.randint(1, 6)

guess = int( input( "Guess the dice roll for the computer:\n"))

if guess == roll:
    print("Correct, the computer rolled a " + str(roll))
else:
    print("Wrong!  The computer rolled a " + str(roll))