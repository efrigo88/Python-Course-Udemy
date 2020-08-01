parrot = 'Norwegian Blue'

print(parrot)

print(parrot[3])

for i in range(0, len(parrot)):
    print(parrot[i])

print('\n')

# mini challenge (I used the function find to get index for the letter, instead of counting manually)
print(parrot)
print(parrot[parrot.find('w')])
print(parrot[parrot.find('e')])
print(parrot[parrot.find(' ')])
print(parrot[parrot.find('w')])
print(parrot[parrot.find('i')])
print(parrot[parrot.find('n')])
#