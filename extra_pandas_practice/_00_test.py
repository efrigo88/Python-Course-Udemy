import pandas as pd

# we import some data
airport = pd.read_csv('C:/Python-Course-Udemy/extra_pandas_practice/airports.csv')
airport_freq = pd.read_csv('C:/Python-Course-Udemy/extra_pandas_practice/airport-frequencies.csv')
runways = pd.read_csv('C:/Python-Course-Udemy/extra_pandas_practice/runways.csv')

# to show the first three rows
print(airport.head(5))


