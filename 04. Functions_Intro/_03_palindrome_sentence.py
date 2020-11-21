# importing function 'is_palindrome2' from another file
from _03_palindrome_source import is_palindrome2


def palindrome_sentence(string: str) -> bool:
    clean_string = ''
    for letter in string:
        if letter.isalpha():
            clean_string += letter
    # return clean_string[::-1].casefold() == clean_string.casefold()
    # calling a function inside a function
    return is_palindrome2(clean_string)


while True:
    to_test = input('Please enter a sentence to test (enter 0 to exit):')

    if to_test != '0':
        if palindrome_sentence(to_test):
            print('The word "{}" is a palindrome'.format(to_test))
        else:
            print('The word "{}" is not a palindrome'.format(to_test))
    else:
        print('Exiting the program...')
        break


