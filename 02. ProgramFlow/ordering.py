# how to order a string alphabetically
print()
out_of_order = 'CBADEFGHIJKLZNOPQRSTUVWXYM'
order_vector = sorted(out_of_order)
result = ''

for x in order_vector:
    result = result + x
print(result)

# when working with strings, you can transform them to lists to be able to exchange values into it
chain = 'CBADEFGHIJKLMNOPQRSTUVWXYZ'
chain_to_list = list(chain)

x = chain_to_list[0]
y = chain_to_list[1]
z = chain_to_list[2]

chain_to_list[0] = z
chain_to_list[1] = y
chain_to_list[2] = x

print(chain_to_list)
print(''.join(chain_to_list))