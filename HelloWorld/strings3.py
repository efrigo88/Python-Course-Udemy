# Slicing

#                   1
#         01234567890123
parrot = 'Norwegian Blue'
print(parrot[0:9])
print(parrot[:9])
# mini challenge: obtain 'Blue' by slicing, I used two ways
print(parrot[10:14])
print(parrot[10:])

#
print()
a = parrot[:6]
b = parrot[6:]
print(a)
print(b)
print(a + b)

# using the colon without any indexes, it throws the whole string
print()
print(parrot[:])

# Slicing with negative numbers
print()
print(parrot[-4:-2])    # Bl
print(parrot[-4:12])    # Bl
print(parrot[-14:-8])   # Norweg

# Using a step in a slice
print()
print(parrot[0:6:2])     # 'Nre' adding 2 as step, it will jump every two positions
print(parrot[0:6:3])     # 'Nw'

number = '9,346:583 593;493 973:944'
separators = number[1::4]     # this could be very useful to clean numbers
print(separators)

values = ''.join(char if char not in separators else ' ' for char in number).split()
print([int(val) for val in values])




