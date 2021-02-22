farm_animals = {'sheep',
                'cow',
                'hen',
                }
print(farm_animals)

print()
for animal in farm_animals:
    print(animal)

print('=' * 40)

# transform from a list to a set
wild_animals_list = ['lion',
                     'tiger',
                     'panther',
                     'elephant',
                     'hare'
                     ]
wild_animals = set(wild_animals_list)
print(wild_animals)
for animal in wild_animals:
    print(animal)

print()
farm_animals.add('horse')
wild_animals.add('horse')
print(farm_animals)
print(wild_animals)

# empty set creation
# using {} does not work because it creates an empty dict
print()
empty_set = set()
empty_set.add('test_object')
print(empty_set)

print()
even = sorted(set(range(0, 20, 2)))
print(even)

squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(squares)



