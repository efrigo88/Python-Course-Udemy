import pandas as pd

# we import some data
airport = pd.read_csv('C:/Python-Course-Udemy/extra_pandas_examples_datasets/airports.csv')
airport_freq = pd.read_csv('C:/Python-Course-Udemy/extra_pandas_examples_datasets/airport-frequencies.csv')
runways = pd.read_csv('C:/Python-Course-Udemy/extra_pandas_examples_datasets/runways.csv')

# to show the first three rows
print(airport.head(5))


