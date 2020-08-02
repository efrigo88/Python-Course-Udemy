parrot = 'Norwegian Blue'

print(parrot)
print(parrot[3])

for i in range(0, len(parrot)):
    print(parrot[i])

print('\n')

# mini challenge (I used the function 'find()' to get the letter's index, instead of counting manually)
print(parrot)
print(parrot[parrot.find('w')])
print(parrot[parrot.find('e')])
print(parrot[parrot.find(' ')])
print(parrot[parrot.find('w')])
print(parrot[parrot.find('i')])
print(parrot[parrot.find('n')])
#

# same mini challenge with negative indexes

print(parrot)
w = parrot.find('w') - 14
e = parrot.find('e') - 14
space = parrot.find(' ') - 14
i = parrot.find('i') - 14
n = parrot.find('n') - 14

print('Negative indexes used:', w, e, space, i, n)

print(parrot[w])
print(parrot[e])
print(parrot[space])
print(parrot[w])
print(parrot[i])
print(parrot[n])