for i in range(1, 20):
    print('i is now {}'.format(i))

# for with steps
print()
for i in range(0, 10, 2):
    print('i is now {}'.format(i))

# going backwards
print()
for i in range(10, 0, -2):
    print('i is now {}'.format(i))

# you could replace an IF, but is not recommended
print()
age = 65
if age in range(16, 66):
    print('Have a good day at work!')
else:
    print('Sorry!')

