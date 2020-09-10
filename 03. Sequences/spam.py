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
# note that we left a comma at the end of line 9
# we can do this, it's very useful

ingredient_to_avoid = 'spam'

for meal in menu:
    if ingredient_to_avoid not in meal:
        print('Safe meal: {}'.format(meal))
    else:
        print('Meal to avoid: {}. Has a spam score of {}'
              .format(meal, meal.count(ingredient_to_avoid)))


