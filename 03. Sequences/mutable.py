shopping_list = ['milk',
                 'pasta',
                 'eggs',
                 'spam',
                 'bread',
                 'rice']
another_list = shopping_list

print(id(shopping_list))
print(id(another_list))

print()
shopping_list += ['chocolate']

print(shopping_list)
# the id remained unchanged
print(id(shopping_list))

# we can see that this variable was updated as well with the new value
# it's like a pointer (reference) in memory
print()
print(another_list)
print(id(another_list))

# another example
print()
a = b = c = d = e = f = another_list
print('Adding Cream')
b.append('cream')
print(c)
print(d)

