from builtins import print

available_parts = [
    ('Computer', 500),
    ('Monitor', 200),
    ('Keyboard', 24),
    ('Mouse', 20),
    ('Mouse Mat', 22),
    ('HDMI Cable', 10),
]

PART_NAME = 0
current_choice = '-'
computer_parts = []     # create an empty list to hold parts

while current_choice != '0':
    if current_choice in '123456':
        print('Adding option {}: {}'.format(current_choice, available_parts[int(current_choice) - 1][PART_NAME]))
        computer_parts.append(available_parts[int(current_choice) - 1])
    else:
        print('Please add options from the list below:')
        for index, (part_nm, part_price) in enumerate(available_parts):
            print('Item Nº {}: {} (${})'.format(index + 1, part_nm, part_price))
        print('0: to finish')
    current_choice = input()

price = 0
print('You selected the following components:')
for index, (part_nm, part_price) in enumerate(computer_parts):
    print('{}: {}'.format(index + 1, part_nm))
    price = price + part_price
print('Price to pay: ${}'.format(price))

