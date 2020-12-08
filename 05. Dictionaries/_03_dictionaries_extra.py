################################################################################
# how to proceed when you check for an element not contained
# in the dictionary, using the 'get' method
fruit = {
    'orange': 'a sweet, orange, citrus fruit',
    'apple': 'good for making cider',
    'lemon': 'a sour, yellow citrus fruit',
    'grape': 'a small, sweet fruit growing in bunched',
    'lime': 'a sour, green citrus fruit',
}

while True:
    dict_key = input('Please enter a fruit: ')
    if dict_key == 'quit':
        break
    # if dict_key in fruit:
    #     description = fruit.get(dict_key)
    #     print(description)
    # else:
    #     print('We don\'t have a {}'.format(dict_key))

    # same result but using get second argument to return a message
    description = fruit.get(dict_key, 'We don\'t have a {}'.format(dict_key))
    print(description)

# to sort, i'd be good to create a list and sort it
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
ordered_keys = sorted(list(fruit.keys()))   # one ln of code less
for f in ordered_keys:
    print('{} - {}'.format(f, fruit[f]))

# we can print only values
print()
for val in fruit.values():
    print(val)

# to display different key or values
print()
print(fruit.keys())
print(fruit.values())


