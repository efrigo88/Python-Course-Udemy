even = set(range(0, 40, 2))
print('Even')
print(even)
print(len(even))

squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print('Squares')
print(squares)
print(len(squares))

# UNION
print()
print(even.union(squares))  # this method avoid duplicates
print(len(even.union(squares)))

# INTERSECTION
print('-' * 40)
print(even.intersection(squares))
print(even & squares)

# DIFFERENCE
print('-' * 40)
print('Even minus Squares')
# using "difference" method would be clearer than using the operator "-"
# because it tells you that you're working with sets
print(sorted(even.difference(squares)))
print(sorted(even - squares))
print('Squares minus Even')
print(sorted(squares.difference(even)))
print(sorted(squares - even))
