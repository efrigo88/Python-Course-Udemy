# without params
def multiply1():
    result = 10 * 4
    return result


# with params
def multiply2(x: float, y: float) -> float:
    """
    Multiply 2 numbers.

    Although this function is intended to multiply 2 numbers,
    you can also use it to multiply a sequence.  If you pass
    a string, for example, as the first argument, you'll get
    the string repeated `y` times as the returned value.

    :param x: First parameter (`int`)
    :param y: Second parameter (`int`)
    :return: The product of `x` and `y`.
    """
    return x * y


# call first one
res = multiply1()
print('without parameters: {}'.format(res))

# call second one
res = multiply2(10, 5)
print('with parameters: {}'.format(res))

print()
for i in range(1, 10):
    res = multiply2(2, i)
    print(res)



