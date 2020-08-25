from builtins import print

available_parts = ['Computer',
                   'Monitor',
                   'Keyboard',
                   'Mouse',
                   'HDMI Cable',
                   'DVD Drive']
# load the valid choices in a cool way
valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
current_choice = '-'
computer_parts = []     # create an empty list

while current_choice != '0':
    if current_choice in valid_choices:
        print('Adding {}'.format(current_choice))
        index = int(current_choice) - 1
        computer_parts.append(available_parts[index])
    else:
        print('Please add options from the list below:')
        # we use enumerate to get the index as well as the element's name
        for x, part in enumerate(available_parts):
            print('{}: {}'.format(x + 1, part))
        print('0: to finish')
    current_choice = input()

print(computer_parts)