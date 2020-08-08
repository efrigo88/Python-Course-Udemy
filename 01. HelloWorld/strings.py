print('Python is fun')
print("Python's strings are easy to use")
print('We can even include "quotes" in strings')
print('hello' + ' world')

##
greetings = 'Hello'
# name = input('Please enter your name: ')
name = 'Emi'
# if we want a space, we can add that too
print(greetings + ' ' + name)

#
print(type(greetings))
age = 32
print(type(age))
age = '32'
print(type(age))

#
age = 32
print(name + ' is ' + str(age) + ' years old')

# f-strings example, It could not work in earlier versions of python, so watch out
age = 32
print(name + f' is {age} years old')

print(f'Pi is approximately {22 / 7:12.50f}')
pi = 22 / 7
print(f'Pi is approximately {pi:12.50f}')
