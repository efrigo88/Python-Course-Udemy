"""
    What I need to do:
    Write a program that prints the numbers from 1 to 100. But for multiples
    of three print “Fizz” instead of the number and for the multiples of
    five print “Buzz”. For numbers which are multiples of both three and
    five print “FizzBuzz”.”
"""


# First: I created a function to evaluate numbers and multiples
def is_multiple(number: float, multiple: int = 1) -> bool:
    res = number % multiple
    if res != 0:
        return False
    return True


# Set beginning and end
start = 1
end = 100

for i in range(start, end + 1):
    if is_multiple(i, 3) is True and is_multiple(i, 5) is True:
        print(str(i) + ' FizzBuzz')
    elif is_multiple(i, 3) is True:
        print(str(i) + ' Fizz')
    elif is_multiple(i, 5) is True:
        print(str(i) + ' Buzz')
    else:
        print(i)
