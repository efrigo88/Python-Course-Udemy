panagram = 'The quick brown fox jumps over the lazy dog'

words = panagram.split()
print(words)

numbers = '9,223,372,036,854,775,807'
print(numbers.split(','))

generated_list = [
    '9', ' ',
    '2', '2', '3', ' ',
    '3', '7', '2', ' ',
    '0', '3', '6', ' ',
    '8', '5', '4', ' ',
    '7', '7', '5', ' ',
    '8', '0', '7',
]

values = ''.join(generated_list)
print(values)

values_list = values.split()
print(values_list)

print()
# Use a loop to produce a list of ints, rather than strings.
# You can either modify the contents of the "value_list" list in place,
# or create a new list of ints.
# solution1, using an empty list
value_list_int = []
for value in values_list:
    value_list_int.append(int(value))
print('Solution 1')
print(value_list_int)

# solution2, modifying the original list
for index, value in enumerate(values_list):
    values_list[index] = int(value)
print('Solution 2')
print(values_list)


