# Create a program that takes some text and returns a list of all the
# characters in the text that are not vowels, sorted in alphabetical
# order.
#
# You can either enter the text from the keyboard or initialise a string
# variable with the string.
def vowels_removal(text: '') -> list:

    vowels = frozenset({'a', 'e', 'i', 'o', 'u'})
    purged_text = ''
    output_set = set()

    for x in text:
        if x.isalpha():
            purged_text += x.lower()

    input_set = set(purged_text)

    for element in input_set:
        if element not in vowels:
            output_set.add(element)

    return list(output_set)


test = '9abc.de3fghijkl&mno#pqr7stu?vwxyz'
result = sorted(vowels_removal(test))
print(result)

