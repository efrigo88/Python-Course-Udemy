even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# we get two nested lists
numbers = [even, odd]

print(numbers)

# we use two for statements to access to each element
for number_list in numbers:
    print(number_list)

    for value in number_list:
        print(value)





