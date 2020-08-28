empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

# I created a new list, so previous one was not affected
sorted_numbers = sorted(numbers)
print(sorted_numbers)

print()
digits1 = list('432985617')
digits2 = sorted('432985617')
print(digits1)
print(digits2)

print()
# ways of copying lists
# more_numbers = list(numbers)
# more_numbers = numbers[:]
more_numbers = numbers.copy()
# one way to check
print(id(numbers))
print(id(more_numbers))
# second way, same lists, but with different object ids
print(numbers is more_numbers)

