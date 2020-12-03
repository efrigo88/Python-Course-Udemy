def sum_numbers(*values: float) -> float:
    """
    Function that sums up all numbers passed as a parameter.

    :param values: list of `int` or `float` we want to sum up
    :return: `float` as the total of input values

    """
    # print(values)
    acc = 0
    for value in values:
        acc += value

    return acc


# testing
print(sum_numbers(1.5, 2, 3, 4.5))