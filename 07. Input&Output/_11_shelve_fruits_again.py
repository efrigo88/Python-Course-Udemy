import shelve

fruit = shelve.open('ShelfTest')
fruit['orange'] = 'a sweet, orange, citrus fruit'
fruit['apple'] = 'good for making cider'
fruit['lemon'] = 'a sour, yellow citrus fruit'
fruit['grape'] = 'a small, sweet fruit growing in bunches'
fruit['pie'] = 'a sour, green citrus fruit'

# print(fruit['lemon'])
# print(fruit['grape'])
# print()

# fruit['lime'] = 'great with tequila'

# for snack in fruit:
#     print(f'{snack}: {fruit[snack]}')

# small program to ask for input and show the fruit's description
# while True:
#     shelf_key = input('Please enter a Fruit: ')

#     if shelf_key == 'quit':
#         break
    
#     desc = fruit.get(shelf_key, f'We do not have a {shelf_key}')
#     print(desc)


# another way to achieve the same thing
while True:
    dict_key = input('Please enter a Fruit: ')

    if dict_key == 'quit':
        break
    elif dict_key in fruit:
        desc = fruit[dict_key]
        print(desc)
    else:
        print(f'We do not have a {dict_key}')

fruit.close()

