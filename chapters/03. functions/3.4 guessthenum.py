# this is a program to guess the number
import random                                                                           # importing random module

secretNum = random.randint(1, 20)                                                       # choosing the random number to guess using the imported module
print("Guess the Secret Number, I'm thinking between 1 - 20")
print(" You've only 5 chances ")

guess = 5
for guess in range (guess, 0, -1):                                                      # for loop untill the user runs out of guesses
    print("Enter Your Guess (" + str(guess) + " guesses remaining):")
    userGuess = int(input())
    if userGuess < 1 or userGuess > 20:                                                 # conditions to check the guess
        print("Can't you read? The number is between 1 - 20")
    elif userGuess < secretNum:
        print("The secret number is GREATER than your guess")
    elif userGuess > secretNum:
        print("The secret number is LOWER than your guess")
    else :                                                                              # if guess are correct go out of the loop
        break

if secretNum == userGuess:                                                              # check what to print based on the guess
    print("Good Job! You have guessed my Number in " + str(5-guess) + " guesses." )
else :
    print("Sorry, but you are out of tries. You can always try again later")
