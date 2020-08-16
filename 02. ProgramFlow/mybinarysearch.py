import random
#
low = 1
high = 100
target = random.randint(1, high)
n_of_guesses = 0

guess = low + (high - low) // 2

while True:

    if guess == target:
        print('Success. Number = {}'.format(guess))
        print('Number of guesses: {}'.format(n_of_guesses))
        break
    elif guess < target:
        if low == guess:
            guess += 1
        else:
            low = guess
        guess = guess + (high - guess) // 2
        n_of_guesses += 1
    else:
        high = guess
        guess = low + (guess - low) // 2
        n_of_guesses += 1



