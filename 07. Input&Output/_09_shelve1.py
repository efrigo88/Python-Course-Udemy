import shelve

# with shelve.open('ShelfTest') as fruit:
#     fruit['orange'] = 'a sweet, orange, citrus fruit'
#     fruit['apple'] = 'good for making cider'
#     fruit['lemon'] = 'a sour, yellow citrus fruit'
#     fruit['grape'] = 'a small, sweet fruit growing in bunches'
#     fruit['pie'] = 'a sour, green citrus fruit'
    
#     print(fruit['lemon'])
#     print(fruit['grape'])


# now trying with a dictionary to see the difference, we cannot print elements with a normal shelve,
# but we are able to do this using a dictionary
# with shelve.open('ShelfTest') as fruit:
#     fruit = {'orange': 'a sweet, orange, citrus fruit',
#              'apple': 'good for making cider',
#              'lemon': 'a sour, yellow citrus fruit',
#              'grape': 'a small, sweet fruit growing in bunches',
#              'pie': 'a sour, green citrus fruit'
#             }

# print(fruit['lemon'])
# print(fruit['grape'])


# if we want to keep shelve active, we should slightly change the syntax
# remember to close the connection
fruit = shelve.open('ShelfTest')
fruit['orange'] = 'a sweet, orange, citrus fruit'
fruit['apple'] = 'good for making cider'
fruit['lemon'] = 'a sour, yellow citrus fruit'
fruit['grape'] = 'a small, sweet fruit growing in bunches'
fruit['pie'] = 'a sour, green citrus fruit'

print(fruit['lemon'])
print(fruit['grape'])
fruit.close()
