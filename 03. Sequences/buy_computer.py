from builtins import print

available_parts = ['Computer',
                   'Monitor',
                   'Keyboard',
                   'Mouse',
                   'Mouse Mat',
                   'HDMI Cable']
current_choice = '-'
computer_parts = []     # create an empty list

while current_choice != '0':
    if current_choice in '123456':
        print('Adding {}'.format(current_choice))
        if current_choice == '1':
            computer_parts.append('Computer')
        elif current_choice == '2':
            computer_parts.append('Monitor')
        elif current_choice == '3':
            computer_parts.append('Keyboard')
        elif current_choice == '4':
            computer_parts.append('Mouse')
        elif current_choice == '5':
            computer_parts.append('Mouse Mat')
        elif current_choice == '6':
            computer_parts.append('HDMI Cable')
    else:
        print('Please add options from the list below:')
        for i in available_parts:
            print('{}: {}'.format(available_parts.index(i) + 1, i))
        print('0: to finish')
    current_choice = input()

print(computer_parts)