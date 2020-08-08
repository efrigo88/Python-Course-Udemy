letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters)
print()
#
backwards = letters[25::-1]
print(backwards)
# we can be even more efficient leaving the start point empty as well
backwards = letters[::-1]
print(backwards)

# mini challenge
# remember that the first value always must be greater than the second one when revert slicing
print()
# get 'qpo'
beginning = letters.find('q')
ending = letters.find('o') - 1
answer = letters[beginning:ending:-1]
print(answer)
print(letters[16:13:-1])    # teacher's answer

# get 'edcba'
print()
start = letters.find('e')
answer = letters[start::-1]
print(answer)
print(letters[4::-1])    # teacher's answer

# get the last 8 characters in reverse order
print()
beginning = len(letters)
ending = beginning - 9
answer = letters[beginning:ending:-1]
print(answer)
print(letters[:-9:-1])    # teacher's answer



