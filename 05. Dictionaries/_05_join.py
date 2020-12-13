myList = ['a', 'b', 'c', 'd']

# when using join, there is no need to use this variable
# newString = ''

# the bad way
# for c in myList:
#     newString += c + ', '

#  the good one
newString = ', '.join(myList)
print(type(newString))
print(newString)

# we can use a string as well
print()
letters = 'djfwpdokqkjfnknvcpsodmclwdssnv'
newString = ', '.join(letters)
print(newString)

print()
numbers = '123456789'
newString = ' mississippi '.join(numbers)
print(newString)



