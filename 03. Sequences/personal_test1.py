chain = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lst = []

for i in chain:
    lst += ['Test Subject {}'.format(i)]
print(lst)
#
print()
for j in lst:
    print(j)
