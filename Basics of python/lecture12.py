#Guessing Game

import random
number = random.randint(1,20)
print(number)

guess = int(input("Guess a number: "))
counter = 1

while guess != number:
    if guess < number:
        print("Your guess is too low. Try again.")
    elif guess > number:
        print("Your guess is too high. Try again.")
    guess = int(input("Guess a number: "))
    counter += 1

print("Congratulations! You guessed the number correctly.")
print("It took you", counter, "attempts to guess the number.")   
