available_exits = ['north', 'south', 'east', 'west']

chosen_exit = ''

while chosen_exit not in available_exits:
    chosen_exit = input('Please choose a direction: ')
    if chosen_exit.casefold() == 'quit':
        print('Game Over')
        break
if chosen_exit in available_exits:
    print("aren't glad you got out of there?")
