# cities = ['Adelaide',
#           'Alice Springs',
#           'Darwin',
#           'Melbourne',
#           'Sydney'
#           ]
#
# # it is needed to use open to indicate that we want to write a file
# with open('writing/cities.txt', 'w') as city_file:
#     for city in cities:
#         # we have to print the elements inside the opened file
#         # if we want to write the file immediately, we'll have to use
#         # the flush parameter: print(city, file=city_file, flush=True)
#         # by default, we should not use it.
#         print(city, file=city_file)


cities = []

with open('writing/cities.txt', 'r') as city_file:
    for city in city_file:
        cities.append(city.strip('\n'))
        # we can also use replace, it seems method above is more efficient
        # cities.append(city.replace('\n', ''))

# printing the list
print(cities)
# printing elements one by one
for city in cities:
    print(city)
