def factorial(number: int = 1) -> int:
    """
    Calculate the factorial of a provided number.

    :param number: The number (int) whose factorial is going to be calculated.
    :return: An int, the result of the calculation.
    """
    if number < 0:
        raise ValueError('Error. Please provide only positive numbers')

    value = 0

    for i in range(0, number + 1):
        if 0 <= i <= 1:
            value = 1
        else:
            value = value * i
    return value


# function testing
for x in range(0, 11):
    print(x, factorial(x))



