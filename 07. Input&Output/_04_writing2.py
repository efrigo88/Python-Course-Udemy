# imelda = 'More Mayhem', \
#          'Imelda May', \
#          '2011', \
#          (
#              (1, 'Pulling the Rug'),
#              (2, 'Psycho'),
#              (3, 'Mayhem'),
#              (4, 'Kentish Town Waltz')
#          )
#
# # pay attention to the output file format
# with open('writing/imelda3.txt', 'w') as imelda_file:
#     print(imelda, file=imelda_file)


with open('writing/imelda3.txt', 'r') as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents)
print(imelda)

# there are better methods to unpack, we will see them later
title, artist, year, tracks = imelda

print(title)
print(artist)
print(year)
print(tracks)
