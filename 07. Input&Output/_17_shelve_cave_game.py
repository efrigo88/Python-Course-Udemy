import shelve

# we get game data from .db using shelve function
locations = shelve.open('location')
vocabulary = shelve.open('vocabulary')

# starting position
loc = '1'

while True:
    availableExits = ", ".join(locations[loc]['exits'].keys())

    print(locations[loc]['desc'])

    if loc == '0':
        break
    else:
        allExits = locations[loc]['exits'].copy()
        allExits.update(locations[loc]['namedExits'])
      

    direction = input(f'Available exits are: {availableExits.upper()}, you pick: ') 
    print()

    # Parse the user input, using our vocabulary dictionary if necessary
    if len(direction) > 1:  # more than 1 letter, so check vocab
        words = direction.split()
        for word in words:
            word = word.upper()
            if word in vocabulary:   # does it contain a word we know?
                direction = vocabulary[word]
                break

    # if the answer contain only one letter
    direction = direction.upper()
    if direction in allExits:
        loc = str(allExits[direction])
    else:
        print(f'You cannot go in this -{direction}- direction, please choose a valid one')

# we close the connections before exit program
locations.close()
vocabulary.close()