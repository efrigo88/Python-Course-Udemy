def guess_binary(answer, low, high):
    n_of_guesses = 1

    while True:

        guess = low + (high - low) // 2     # Binary Search method

        if guess == answer:
            return n_of_guesses
        elif guess < answer:
            low = guess + 1
        else:
            high = guess - 1

        n_of_guesses += 1


# Establish the range limits, LOW and HIGH
LOW = 1
HIGH = 1000

correct_count = 0
max_guesses = 0

for number in range(LOW, HIGH + 1):
    number_of_guesses = guess_binary(number, LOW, HIGH)
    # personal mod: arrange the zeros in front of number to make them equal
    number = str(number)
    if len(str(HIGH)) - len(str(number)) > 0:
        diff = len(str(HIGH)) - len(str(number))
        number = (diff * '0') + str(number)
    ###
    print("{} guessed in {}".format(number, number_of_guesses))

    if number_of_guesses > max_guesses:
        max_guesses, correct_count = number_of_guesses, 1
    elif number_of_guesses == max_guesses:
        correct_count += 1

print('I guessed without being told {} times. Max {} guesses.'
      .format(correct_count, max_guesses))

