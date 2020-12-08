fruit = {
    'orange': 'a sweet, orange, citrus fruit',
    'apple': 'good for making cider',
    'lemon': 'a sour, yellow citrus fruit',
    'grape': 'a small, sweet fruit growing in bunched',
    'lime': 'a sour, green citrus fruit',
}

print(fruit)
print(fruit['orange'])
print()
# print(sorted(fruit))

# to add an element
fruit['pear'] = 'an odd shaped apple'
print(fruit)

# if you reuse the key, you will overwrite the value
fruit['lime'] = 'great with tequila'
print(fruit)

# to remove an element, if you forget the key, the entire dic will be deleted
del fruit['pear']
print(fruit)

# another and better way of deleting
fruit.clear()
print(fruit)




