data = [4, 5, 104, 105, 110, 6, 120, 130, 100,
        130, 150, 160, 170, 183, 200, 3, 185,
        187, 1000, 188, 191, 350, 360]

min_valid = 100
max_valid = 200

for index in range(len(data) - 1, -1, -1):
    if data[index] < min_valid or data[index] > max_valid:
        #print(index, data)
        del data[index]
print(data)
