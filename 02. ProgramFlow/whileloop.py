# mi example, just to practice
maximum = 1000000
multiplier = 1.05
init = 1

while init < maximum:
    init = init + (init * multiplier)
    if init > maximum:
        break
    print('Init equals to {}'.format(init))


# course example
i = 0
while i < 10:
    print('i is now {}'.format(i))
    i += 1
