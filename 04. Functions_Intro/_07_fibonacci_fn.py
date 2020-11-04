def fibonacci_pos(n):
    """Return the `n` th Fibonacci number, for positive `n`."""
    if n < 0:
        raise ValueError('"n" must be positive, you have entered "{}"'
                         .format(n))
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


def fibonacci_seq(n):
    """Return the Fibonacci sequence, given a positive `n` to limit it"""

    if n < 0:
        raise ValueError('"n" must be positive, you have entered "{}"'
                         .format(n))

    result = [0, 1, 1]
    n_minus1, n_minus2 = 1, 1

    if n == 0:
        return '0'
    elif n == 1:
        return '0, 1'
    elif n == 2:
        return '0, 1, 1'

    pos = 2

    while True:
        res = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = res
        result.append(res)

        if pos == n - 1:
            print(str(result)[1:-1])
            break
        pos += 1


number = int(input('Please enter a number to get the Fibonacci number:'))
print(fibonacci_pos(number))

# to test first function massively
print()
number = 25
for i in range(number + 1):
    print(i, fibonacci_pos(i))

print()
number = int(input('Please enter a number to limit Fibonacci Sequence:'))
print(fibonacci_seq(number))







