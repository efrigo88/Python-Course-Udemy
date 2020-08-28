even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# to unite two lists
even.extend(odd)
print(even)

# we can sort the elements in a list using the method sort()
print('ordered')
even.sort()
print(even)

# remember that the method reorder the list instead of creating another
print('another_even, ordered')
another_even = even
print(another_even)

# to sort in reverse order
print('reversed even')
even.sort(reverse=True)
print(even)

# now it was reordered
print('another_even reversed')
print(another_even)


