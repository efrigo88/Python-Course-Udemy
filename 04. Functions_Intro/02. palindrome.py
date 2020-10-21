def is_palindrome(word):
    lst = list(word)
    rev = []
    empty_string = ''
    for index, value in enumerate(reversed(lst)):
        rev.append(value)
    for i in rev:
        empty_string += i
    if word == empty_string:
        return True
    else:
        return False


# to check the palindrome function
print(is_palindrome('kayak'))
