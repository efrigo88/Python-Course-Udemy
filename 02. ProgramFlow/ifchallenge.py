name = input('Please enter your name: ')
age = int(input('Hello {}, how old are you? '.format(name)))

if 18 <= age <= 30:
    print('Perfect {}, you can go!'.format(name))
else:
    print('Sorry {}, but your age does not match the requirements'.format(name))

