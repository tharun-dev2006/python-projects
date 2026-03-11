# Project: Number Guessing Game
# Author: Tharun
# Description: A command line game where the user tries to guess
#              a randomly generated number with multiple attempts.


import random

a = random.randint(1,10)
count = 0
chance = 3
while count < chance:
    guess = int(input("guess a random number between 1 to 10"))
    count += 1

    if guess == a:
        print("the number you guessed = ", guess , "is corrrect")
        break

    else:
        print("you guessed wrong!", "correct guess was =" , a)


