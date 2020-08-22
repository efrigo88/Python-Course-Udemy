result = True
another_result = result

# id to print the unique id of an object
print(id(result))
print(id(another_result))


print()
result = 'Correct'
another_result = result
print(id(result))
print(id(another_result))

result += 'ish'
print(id(result))
