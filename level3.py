# In level three, the computer's guesses are optimized to refine the range on the guesses based on whether they are too high or too low. Print how many guesses it takes the computer before it correctly guesses the number.

from random import randint

num= int(input('Choose a number...'))

def compplays():
    guesses = 0 #initially had this outside of the function but threw error
    compguess = 101
    top_range = 100
    bottom_range = 1


    while compguess != int(num):
        compguess = randint(bottom_range, top_range)
        if compguess > int(num):
            print('Too high, guess again')
            print(compguess)
            top_range = compguess - 1
            guesses = guesses + 1
        elif compguess < int(num):
            print('Too low, guess again')
            print(compguess)
            bottom_range = compguess + 1
            guesses = guesses + 1
        else:
            print(compguess)
            print('I took the computer this many tries: ' + str(guesses+1))
            

compplays()