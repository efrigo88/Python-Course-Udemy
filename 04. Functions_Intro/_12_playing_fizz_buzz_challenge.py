# Function to get the result according to the input number
def fizz_buzz(number: int) -> str:
    """
    Function that retrieves a results according to the Fizz Buzz game.

    :param number: The integer which we want to try out.
    :return: str indicating:
                    fizz: number divisible by 3,
                    buzz: number divisible by 5,
                    fizz buzz: number divisible by 3 and 5,
                    number: for every other case.
    """
    if number % 3 == 0 and number % 5 == 0:
        return 'fizz buzz'
    elif number % 3 == 0:
        return 'fizz'
    elif number % 5 == 0:
        return 'buzz'
    else:
        return str(number)


# Challenge starts
counter = 1
while counter < 101:
    print('Machine: {}'.format(fizz_buzz(counter)))
    counter += 1
    your_answer = input('Your go: ')
    print('-' * 15)
    real_answer = fizz_buzz(counter)

    if your_answer != real_answer:
        print('"{}" was a wrong answer, It should\'ve been "{}". Game Over'
              .format(your_answer, real_answer))
        break
    counter += 1
else:
    print('You\'ve won the game, congratulations!!!')