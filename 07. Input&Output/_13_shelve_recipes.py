import shelve

# blt = ['bacon', 'lettuce', 'tomato', 'bread']
# beans_on_toast = ['beans', 'bread']
# scrambled_eggs = ['eggs', 'butter', 'milk']
# soup = ['tin of soup']
# pasta = ['pasta', 'cheese']

with shelve.open('recipes', writeback=True) as recipes:
    # recipes['blt'] = blt
    # recipes['beans on toast'] = beans_on_toast
    # recipes['scrambled eggs'] = scrambled_eggs
    # recipes['pasta'] = pasta
    # recipes['soup'] = soup

    # if we want to modify elements, we have to create an aux variable, work it
    # and overwrite a previous list if we need it.
    # temp_list = recipes['blt']
    # temp_list.append('butter')
    # recipes['blt'] = temp_list

    # temp_list = recipes['pasta']
    # temp_list.append('tomato')
    # recipes['pasta'] = temp_list

    # there is a way to add elements in an easier manner
    # we have to use the writeback parameter
    # recipes['soup'].append('croutons')


    for snack in recipes:
        print(snack, recipes[snack])
