# an example for me
chain = 'abcdefghijklmnopqrstuvwxyz'
for i in range(0, len(chain)):
    print('The letter in this position is: {0}'.format(chain[i]))
###################
print()
for i in range(1, 13):
    print('No. {0:2} squared is {1:3} and cube is {2:4}'.format(i, i ** 2, i ** 3))
    # we use the ':2' or ':4' as an alignment method(width), to add some formatting to the output

print()
for i in range(1, 13):
    print('No. {0:2} squared is {1:<3} and cube is {2:<4}'.format(i, i ** 2, i ** 3))
    # left align '<'

print()
for i in range(1, 13):
    print('No. {0:2} squared is {1:^3} and cube is {2:^4}'.format(i, i ** 2, i ** 3))
    # center align '^'

print()
print('Pi is approximately {0:12}'.format(22 / 7))      # we can round float numbers as well
print('Pi is approximately {0:12f}'.format(22 / 7))     # we use f for increasing the width
print('Pi is approximately {0:12.50f}'.format(22 / 7))  # precision 50, it's more important than width
print('Pi is approximately {0:52.50f}'.format(22 / 7))  # same precision, width increase
print('Pi is approximately {0:62.50f}'.format(22 / 7))  # same precision, width increase
print('Pi is approximately {0:72.50f}'.format(22 / 7))  # same precision, width increase

print()
for i in range(1, 13):
    print('No. {:2} squared is {:3} and cube is {:4}'.format(i, i ** 2, i ** 3))
    # we can still control the width even without the indexes for the curly braces





