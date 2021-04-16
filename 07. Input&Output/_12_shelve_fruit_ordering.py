import shelve

fruit = shelve.open('ShelfTest')
fruit['orange'] = 'a sweet, orange, citrus fruit'
fruit['apple'] = 'good for making cider'
fruit['lemon'] = 'a sour, yellow citrus fruit'
fruit['grape'] = 'a small, sweet fruit growing in bunches'
fruit['pie'] = 'a sour, green citrus fruit'

# shelve does not mantain its objects in order, so we need to order them by ourselves
ordered_keys = list(fruit.keys())
ordered_keys.sort()

for f in ordered_keys:
    print(f'{f} - {fruit[f]}')

fruit.close()
