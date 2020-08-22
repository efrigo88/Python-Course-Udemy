computer_parts = ['computer',
                  'monitor',
                  'keyboard',
                  'mouse',
                  'mouse mat']

for part in computer_parts:
    print('The following part is {}, the index is {}'
          .format(part, computer_parts.index(part)))

# to print only one element
print(computer_parts[2])
# slice
print(computer_parts[1:3])
# with negatives
print(computer_parts[-2])

# remember that you can transform a str into a list to do some shit
chain = 'test'
lst = list(chain)
print(lst)
chain_again = ''.join(lst)
print(chain_again)





