a = 12
b = 3

print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4.0
print(a // b)   # 4 integer division, rounded down towards minus infinity
print(a % b)    # 0 modulo: the remainder of after integer division

print()

for i in range(0, (a // b)):   # here you can only use integers to use the range statement
    print(i)

for i in range(0, int(a / b)):   # if not, you must convert the outcome to int type
    print(i)

# coding exercise
bun_price = 2.40
money = 15
result = money // bun_price
print(result)
#

# operator precedence
print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))
print(((a + b) / 3) - (4 * 12))
print((((a + b) / 3) - 4) * 12)

c = a + b
d = c / 3
e = d - 4
f = e * 12
print(f)
