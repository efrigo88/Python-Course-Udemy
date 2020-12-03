# Variable number of parameters "*args" examples
##
numbers = (0, 1, 2, 3, 4, 5)

# print(numbers, sep=';')
# # it unpacks
# print(*numbers, sep=';')
# print(0, 1, 2, 3, 4, 5, sep=';')


# packing example
def test_star(*args):
    # now it packs into a tuple
    print(args)
    # print each element to prove this
    for x in args:
        print(x)


test_star(0, 1, 2, 3, 4, 5)
