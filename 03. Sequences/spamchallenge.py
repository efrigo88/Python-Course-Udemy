menu = [
    ['egg', 'bacon'],
    ['egg', 'sausage', 'bacon'],
    ['egg', 'spam'],
    ['egg', 'bacon', 'spam'],
    ['egg', 'bacon', 'sausage', 'spam'],
    ['spam', 'bacon', 'sausage', 'spam'],
    ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'],
    ['spam', 'sausage', 'spam', 'bacon', 'spam', 'tomato', 'spam'],
]

item_to_remove = 'spam'

for meal in menu:
    qty_elements = len(meal) - 1
    for index, item in enumerate(reversed(meal)):
        if item == item_to_remove:
            del meal[qty_elements - index]

print('Menu without \'{}\':'.format(item_to_remove))
for i, item in enumerate(menu):
    print('Menu {}: {}'.format(i + 1, item))

