import pandas as pd

# we import some data
airports = pd.read_csv('C:/Python-Course-Udemy/extra_pandas_practice/airports.csv')
airport_freq = pd.read_csv('C:/Python-Course-Udemy/extra_pandas_practice/airport-frequencies.csv')
runways = pd.read_csv('C:/Python-Course-Udemy/extra_pandas_practice/runways.csv')

# simple SELECT
# print(airports)

# SELECT LIMIT 3
test1 = airports.head(5)
# print(type(test1))

# SELECT id FROM airports WHERE ident = 'KLAX'
test2 = airports[airports.ident == 'KLAX'].id
# print(type(test2))

# SELECT DISTINCT type FROM airports
test3 = airports.type.unique()
# print(test3)

# SELECT * FROM airports WHERE iso_region = 'US-CA' AND type = 'seaplane_base'
test4 = airports[(airports.iso_region == 'US-CA') &
                 (airports.type == 'seaplane_base')]
# print(test4)

# SELECT ident, name, municipality FROM airports
# WHERE iso_region = 'US-CA' AND type = 'large_airport'
test5 = airports[(airports.iso_region == 'US-CA') &
                 (airports.type == 'seaplane_base')][['ident',
                                                      'name',
                                                      'municipality']]
# print(test5)

# select * from airport_freq where airport_ident = 'KLAX' order by type
test6 = airport_freq[airport_freq.airport_ident == 'KLAX'].sort_values('type')
# print(test6)

# select * from airport_freq where airport_ident = 'KLAX' order by type desc
test7 = airport_freq[airport_freq.airport_ident == 'KLAX'].sort_values('type', ascending=False)
# print(test7)

# select * from airports where type in ('heliport', 'balloonport')
test8 = airports[airports.type.isin(['heliport', 'balloonport'])]
# print(test8)

# select * from airports where type not in ('heliport', 'balloonport')
test9 = airports[~airports.type.isin(['heliport', 'balloonport'])]
print(test9)