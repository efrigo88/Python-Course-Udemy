day = 'Monday'
temperature = 30
raining = True

if (day == 'Saturday' and temperature > 27) or not raining:
    print('Go swimming')
else:
    print('Learn Python')

# Truthy Values
print()
if 0:
    print('True')
else:
    print('False')

print()
name = input('Please Enter your Name: ')
if name:    # if the variable has something...
    print('Hello, {}'.format(name))
else:   # if the variable is empty...
    print('Are you a man with no name?')

# Another way of doing the same thing
if name != '':
    print('Hello, {}'.format(name))
else:
    print('Are you a man with no name?')
