#In level one, the computer generates a random number between 1 and 10 and the user has 3 guesses to pick the correct number. The computer will tell you if you are too high or too low.

from random import randint

num = randint(1,10) #creating a random number between 1 and 10

guesses = 0 #starting point for number of guesses taken

while guesses < 3:
    print('Take a guess')
    guess=input() #setting guess to the input of whatever I type

    guesses = guesses + 1 #increments the number of guesses each time

    if int(guess) < num:
        print('Too low')
    
    if int(guess) > num:
        print('Too high')

    if guess == num:
        break

if guess == num:
    print('You guessed it!')

if guess != num:
    print('Nope.')
