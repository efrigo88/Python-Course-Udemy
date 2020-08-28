pangram = 'The quick brown fox jumps over the lazy dog'

letters = sorted(pangram)
print(letters)

print()
numbers = [10.2, 5.5, 7.9, 2.3, 4.4]
print(numbers)
sorted_numbers = sorted(numbers)
print(sorted_numbers)

print()
new_numbers = numbers
numbers.sort()

print()
# using the key allows us to correctly sort the capital 'T'
missing_letter = sorted('The quick brown fox jumped over the lazy dog',
                        key=str.casefold)
print(missing_letter)

print()
names = ['Graham',
         'John',
         'terry',
         'eric',
         'Terry',
         'michael'
        ]
names.sort(key=str.casefold)
print(names)
