#Algorithm
##Generate a random number in the selected range.
#Calculate the maximum allowed guesses using the binary search formula.
#Run a loop to take user guesses:
#If the guess is too high, print: "Try Again! You guessed too high."
#If the guess is too low, print: "Try Again! You guessed too small."
#If the guess is correct, print: "Congratulations!" and exit the loop.
#If the user runs out of chances, display the correct number and a message: "Better Luck Next Time!"


import random

print("hi! welcome to number guessing game")

low = int(input("Enter the lower Bound: "))
high = int(input("enter the upper bound: "))

print(f"\n you have 7 chance to guess the number between {low} and {high}. Lets's start!")

num = random.randint(low,high)
ch = 7
gc = 0

while gc < ch:
    gc += 1
    guess = int(input('Enter your guess: '))

    if guess == num:
        print(f'correct ! The number is {num}. you guessed it in {gc}  attempts.')
        break
    elif gc >= ch and guess != num:
        print(f'sorry! the number was {num}. Better luck next time.')

    elif guess>num:
        print('too high! try a lower number.')

    elif guess < num:
        print('too low! try a higher number.')
