i = 1
while i < 21:
    if (i % 3 == 0) or (i % 5 == 0):
        i += 1
        continue
    else:
        print(i)
    i += 1

