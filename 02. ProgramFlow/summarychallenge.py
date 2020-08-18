choice = None
flag = 0
menu = """Please choose your option from the list below:
1.  Learn Python
2.  Learn Java
3.  Go Swimming
4.  Have Dinner
5.  Go to bed
0.  Exit"""

while choice != 0:
    if flag == 0:
        print(menu)
    choice = int(input())

    if choice in range(1, 6):
        print('You have chosen option {}'.format(choice))
        flag = 1
    elif choice == 0:
        print('You exited the program')
        break
    else:
        input('invalid option, press ENTER to continue')
        flag = 0