data = [4, 5, 104, 105, 110, 6, 120, 130, 100,
        130, 150, 160, 170, 183, 200, 3, 185,
        187, 1000, 188, 191, 350, 360]

min_valid = 100
max_valid = 200

# less efficient and difficult to understand at first sight
# for index in range(len(data) - 1, -1, -1):
#     if data[index] < min_valid or data[index] > max_valid:
#         #print(index, data)
#         del data[index]
# print(data)

# when we use reversed, it reverses the iterator numbers
# it's more efficient and easier to understand
top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]
print(data)
