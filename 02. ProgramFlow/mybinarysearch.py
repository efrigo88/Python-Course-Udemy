import random
#
low = 1
high = 10
target = random.randint(1, high)
n_of_guesses = 0

guess = low + (high - low) // 2     # first guess

while True:

    if guess == target:
        print('Success. Number = {}'.format(guess))
        print('Number of guesses: {}'.format(n_of_guesses))
        break
    elif guess < target:
        low = guess + 1
        guess = low + (high - low) // 2
        n_of_guesses += 1
    else:
        high = guess - 1
        guess = low + (high - low) // 2
        n_of_guesses += 1



