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