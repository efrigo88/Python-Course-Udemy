def is_palindrome1(word):
    lst = list(word)
    rev = []
    rev_string = ''

    for index, value in enumerate(reversed(lst)):
        rev.append(value)
    for i in rev:
        rev_string += i

    return word == rev_string


# more efficient one
def is_palindrome2(word: str) -> bool:
    """
    The function checks if the provided string is a palindrome.
    A 'palindrome' is a string that reads the same forwards as backwards.

    :param word: The string that you want to check.
    :return: It returns True if a palindrome is provided, False otherwise
    """
    # backwards = word[::-1]
    # return word == backwards
    return word[::-1].casefold() == word.casefold()


while True:
    to_test = input('Please enter a word to test (enter 0 to exit):')

    if to_test != '0':
        if is_palindrome2(to_test):
            print('The word "{}" is a palindrome'.format(to_test))
        else:
            print('The word "{}" is not a palindrome'.format(to_test))
    else:
        print('Exiting the program...')
        break



