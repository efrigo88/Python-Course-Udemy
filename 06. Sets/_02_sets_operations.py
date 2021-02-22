# even = set(range(0, 40, 2))
# print('Even')
# print(even)
# print(len(even))

# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print('Squares')
# print(squares)
# print(len(squares))

# # UNION
# print()
# print('UNION')
# print(even.union(squares))  # this method avoid duplicates
# print(len(even.union(squares)))

# # INTERSECTION
# print('-' * 40)
# print('INTERSECTION')
# print(even.intersection(squares))
# print(even & squares)   # another way of saying intersection

# # DIFFERENCE
# print('-' * 40)
# print('Even minus Squares')
# # using "difference" method would be clearer than using the operator "-"
# # because it tells you that you're working with sets
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))
# print('Squares minus Even')
# print(sorted(squares.difference(even)))
# print(sorted(squares - even))

# we can use difference_update method to remove the set passed by parameter
# directly from the source set, it removes elements physically.
# print('-' * 40)
# print(sorted(even))
# print(squares)
# even.difference_update(squares)
# print(sorted(even))

# the opposite of intersection
# (before I run this section watch out about line 40 (update method))
# print()
# print('Symmetric even minus squares')
# print(sorted(even.symmetric_difference(squares)))
# print('Symmetric squares minus even')
# print(sorted(squares.symmetric_difference(even)))

# # DISCARD & REMOVE methods
# squares.discard(4)
# squares.remove(16)  # will throw an error if the element does not exist
# squares.discard(8)  # will do nothing
# print(squares)

# # to safely use remove method, we should ask before deletion
# # this method is useful because sometimes we need an error to occur
# number_to_delete = 8
# if number_to_delete in squares:
#     squares.remove(number_to_delete)
# # example with try - except
# try:
#     squares.remove(number_to_delete)
# except KeyError:
#     print('The item {} is not a member of the set'.format(number_to_delete))

# # Subsets & Supersets
# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 16)
# squares = set(squares_tuple)
# print(squares)
# if squares.issubset(even):
#     print('squares is a subset of even')
# if even.issuperset(squares):
#     print('even is a superset of squares')

# Frozen Sets, elements in it cannot change, useful for dictionary keys
even = frozenset(range(0, 100, 2))
print(even)


