# Create a program that takes some text and returns a list of all the
# characters in the text that are not vowels, sorted in alphabetical
# order.
#
# You can either enter the text from the keyboard or initialise a string
# variable with the string.

sample_text = '9abc.de3fghijkl&mno#pqr7stu?vwxyz'
vowels = frozenset('aeiou')
purged_text = ''

for x in sample_text:
    if x.isalpha():
        purged_text += x.lower()

final_set = set(purged_text).difference(vowels)
print(sorted(list(final_set)))

