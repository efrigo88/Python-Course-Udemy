# without params
def multiply1():
    result = 10 * 4
    return result


# with params
def multiply2(x, y):
    result = x * y
    return result


# call first one
res = multiply1()
print('without parameters: {}'.format(res))

# call second one
res = multiply2(10, 5)
print('with parameters: {}'.format(res))

print()
for i in range(1, 10):
    res = multiply2(2, i)
    print(res)



