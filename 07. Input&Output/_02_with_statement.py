# with statement will close the file automatically
# with open('files/sample.txt', 'r') as jabber:
#     for line in jabber:
#         if 'JAB' in line.upper():
#             print(line, end='')

# going line by line with the readline method
# with open('files/sample.txt', 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

# readlines method returns a list with all the lines
# with open('files/sample.txt', 'r') as jabber:
#     lines = jabber.readlines()
# print(type(lines))
# print(lines)
# print('=' * 40)
# for line in lines:
#     print(line, end='')

# printing the lines backwards
# with open('files/sample.txt', 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
# print('=' * 40)
# for line in lines[::-1]:
#     print(line, end='')

# printing the whole thing backwards with the read method
# read method generates a string with the contents of a file,
# if the file contains string elements obviously
with open('files/sample.txt', 'r') as jabber:
    lines = jabber.read()
for line in lines[::-1]:
    print(line, end='')
