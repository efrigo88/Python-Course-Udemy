# indentation differences
for i in range(1, 11):
    print('No. {} squared is {} and cube is {}'.format(i, i ** 2, i ** 3))
print('*' * 45)

# ----------------------
print()
for i in range(1, 11):
    print('No. {} squared is {} and cube is {}'.format(i, i ** 2, i ** 3))
    print('*' * 45)


# Example to remember about IF statements
print()
name = input('Please enter your name: ')
age = input('Hello {}!, How old are you?: '.format(name))

#
print()
if name and age:
    if int(age) >= 18:
        print('You are old enough to vote.')
    else:
        diff = 18 - int(age)
        if diff == 1:
            print('Your age is {}, you cannot vote. Please come back in 1 year'.format(age))
        else:
            print('Your age is {}, you cannot vote. Please come back in {} years'.format(age, diff))
else:
    print('You have to enter values for both variables')

# elif
print()
age = int(age)

if age >= 18:
    if age == 900:
        print('Sorry Yoda, you die in The Return of the Jedi')
    else:
        print('You are old enough to vote.')
elif 0 < age < 18:
    print('Your age is {}, you cannot vote. Please come back in {} year/s'.format(age, 18 - age))
else:
    print('Sorry, wrong age, please run the program again')


