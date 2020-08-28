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
        index = int(current_choice) - 1
        chosen_part = available_parts[index]

        if chosen_part in computer_parts:
            computer_parts.remove(chosen_part)
            print('Removing {}'.format(current_choice))
        else:
            computer_parts.append(available_parts[index])
            print('Adding {}'.format(current_choice))

        if not computer_parts:
            print('Your list is empty')
        else:
            print('Your list now contains {}'.format(computer_parts))
    else:
        print('Please add options from the list below:')
        # we use enumerate to get the index as well as the element's name
        for x, part in enumerate(available_parts):
            print('{}: {}'.format(x + 1, part))
        print('0: to finish')
    current_choice = input()

print(computer_parts)