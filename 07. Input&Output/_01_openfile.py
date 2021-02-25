# open the file, full and reduced path
jabber = open('files/sample.txt', 'r')
# jabber = open('C:\\Python-Course-Udemy\\07. Input&Output\\files\\sample.txt', 'r')

# it uses a special type of variable
print(type(jabber))
print('=' * 40)

# use a for to print the lines independently
# for line in jabber:
#     print(line)

print('=' * 40)
for line in jabber:
    if 'jabberwock' in line.lower():
        print(line, end='')

# always remember to close the file
jabber.close()
