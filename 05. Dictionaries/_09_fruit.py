fruit = {
    'orange': 'a sweet, orange, citrus fruit',
    'apple': 'good for making cider',
    'lemon': 'a sour, yellow citrus fruit',
    'grape': 'a small, sweet fruit growing in bunched',
    'lime': 'a sour, green citrus fruit'}
print(fruit)

veg = {
    'cabbage': 'every child\'s favourite',
    'sprouts': 'mmm, lovely',
    'spinach': 'can I have some fruit, please'}
print(veg)

# to add fruit dict into veg dict
veg.update(fruit)
print(veg)
# to add veg dict into fruit dict
fruit.update(veg)
print(fruit)

# if we do not want to modify the originals, we create a new one using copy
print()
nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)

# to confirm we use a different dict
print(id(nice_and_nasty))
print(id(fruit))
print(id(veg))
