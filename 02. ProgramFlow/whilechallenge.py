import random

print('Enter the number which will be the highest number to guess: ')
highest = int(input())

answer = random.randint(1, highest)
n_of_guesses = 1

print('Please guess a number between 1 and {}: '.format(highest))
guess = int(input())

while True:
    if guess == answer:
        print('Well done, you guessed it')
        print('Number of guesses: {}'.format(n_of_guesses))
        break
    elif guess == 0:
        print('You exited the program')
        print('Number of guesses: {}'.format(n_of_guesses))
        break
    elif guess < answer:
        print('Please guess higher')
    else:
        print('Please guess lower')

    guess = int(input())
    n_of_guesses += 1



