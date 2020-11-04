import random


def get_integer(prompt):
    """
    Gets an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.
    :param prompt: The string that the user will see, when
        they're prompted to enter the value.
    :return: The integer which the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print('"{}" is not a valid number'.format(temp))


highest = 100
answer = random.randint(1, highest)
n_of_guesses = 1

print('Please guess a number between 1 and {}: '.format(highest))
guess = get_integer(': ')

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

    guess = get_integer(': ')
    n_of_guesses += 1








