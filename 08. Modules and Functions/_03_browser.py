import webbrowser

# webbrowser.open('https://www.python.org', new=1)

# it is always good to check documentation about a certain funtionality
# help(webbrowser)

# trying  differents parameters
# for i in range(10):
#     print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep=';', end=' ')


# trying to open a new tab in a different manner
safari = webbrowser.get(using='safari')
safari.open_new('https://www.python.org')