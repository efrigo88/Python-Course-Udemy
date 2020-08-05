age = 32
print('My Age is ' + str(age) + ' years old')   # old way
print('My Age is {0} years old'.format(age))     # new way

print('There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}'
      .format(31, 'Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec'))

print('Jan:{2}, Feb:{0}, Mar:{2}, Apr:{1}, May:{2}, Jun:{1}'.format(28, 30, 31))

print()

print("""
Jan: {2}, 
Feb: {0}, 
Mar: {2}, 
Apr: {1}, 
May: {2}, 
Jun: {1}""".format(28, 30, 31))

print()
dataset = [['January', 31], ['February', 28], ['March', 31], ['April', 30], ['May', 31], ['june', 30]]

for ds in dataset:
    print('{0} has {1} days'.format(ds[0], ds[1]))





