import pandas as pd
import pyodbc

# we import from sql conn
# sql_conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=721930e39c37;DATABASE=Test_Pandas;Trusted_Connection=yes')
sql_conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};Server=721930e39c37;Database=Test_Pandas;User Id=sa;Password=pass123;')

query = "SELECT  [id]," \
                "[ident]," \
                "[type]," \
                "[name]," \
                "[latitude_deg]," \
                "[longitude_deg]," \
                "[elevation_ft]," \
                "[iso_country]," \
                "[iso_region]," \
                "[municipality]," \
                "[gps_code]," \
                "[iata_code]," \
                "[local_code] " \
        "FROM [Test_Pandas].[dbo].[airports]"

df = pd.read_sql(query, sql_conn)

print(df.head(3))