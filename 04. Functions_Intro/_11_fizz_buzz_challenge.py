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


# "for" to test function output
for i in range(1, 101):
    print(fizz_buzz(i))