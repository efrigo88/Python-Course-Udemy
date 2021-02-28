cities = ['Adelaide',
          'Alice Springs',
          'Darwin',
          'Melbourne',
          'Sydney'
          ]

# it is needed to use open to indicate that we want to write a file
with open('writing/cities.txt', 'w') as city_file:
    for city in cities:
        # we have to print the elements inside the opened file
        # if we want to write the file immediately, we'll have to use
        # the flush parameter: print(city, file=city_file, flush=True)
        # by default, we should not use it.
        print(city, file=city_file)


