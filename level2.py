# In level two, the game is reversed and the user picks a number and the computer then has 3 guesses to select the correct answer.

from random import randint

num = int(input('Choose a number...')) # changes to an integer to integer instead of a string

guesses = 0

while guesses < 3:
    compguess = randint(1,10)
    print('Computer guess is', compguess)
    
    guesses = guesses + 1
    
    if compguess < num:
        print('Too low, guess again.')

    if compguess > num:
        print('Too high, guess again.')
    
    if compguess == num:
        break

if compguess == num:
    print('You got it!')

if compguess != num:
    print('NOPE')