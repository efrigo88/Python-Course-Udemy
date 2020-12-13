fruit = {
    'orange': 'a sweet, orange, citrus fruit',
    'apple': 'good for making cider',
    'lemon': 'a sour, yellow citrus fruit',
    'grape': 'a small, sweet fruit growing in bunched',
    'lime': 'a sour, green citrus fruit',
}
print(fruit)
print()
fruit_keys = fruit.keys()
print(fruit_keys)
fruit['tomato'] = 'not nice with ice cream'
# we can add an element, and the variable we'd previously created takes
# the new addition.
print(fruit_keys)

# another way of displaying its information
print()
print(fruit.items())

# we can create a tuple using that method
print()
f_tuple = tuple(fruit.items())
print(f_tuple)

print()
for snack in f_tuple:
    item, description = snack
    print('{} is "{}"'.format(item, description))

# and we can go back to a dictionary again using the dict function
print(dict(f_tuple))
