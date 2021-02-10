"""
Generates vehicle sales reports based on Sqlite database.
"""

import pandas as pd
import sqlite3


class ReportGenerator:
    """
    Implement the following 4 functions:
    - sales_by_brand
    - new_customers
    - old_customers
    - next_vehicle
    """

    def __init__(self):
        self.dbname = "vehicle_crm.sqlite"
        self.con = sqlite3.connect(self.dbname)
        self.cur = self.con.cursor()

    def __del__(self):
        self.con.close()

    def sales_by_brand(self, filename):
        """
        Creates a report of vehicle sales broken by vehicle brand.
        Writes the report into a CSV file.

        Report fields:
        - vehicle_brand: vehicle brand
        - n_sales: number of sales within a group
        - total_value: sum of prices of all sales within a group

        Sort by:
        - n_sales descending
        - total_value descending

        :param str filename: Output file name
        """

        # get data from sqlite
        sales_df = pd.read_sql_query("select * from Sales", self.con)
        vehicles_df = pd.read_sql_query("select * from Vehicles", self.con)
        invoices_df = pd.read_sql_query("select * from Invoices", self.con)
        vehicle_models_df = pd.read_sql_query("select * from Vehicle_models", self.con)

        # joins
        join1 = sales_df.merge(vehicles_df, left_on='vehicle_id', right_on='vehicle_id', how='inner')
        join2 = join1.merge(invoices_df, left_on='invoice_id', right_on='invoice_id', how='inner')
        join3 = join2.merge(vehicle_models_df, left_on='vehicle_model_id', right_on='vehicle_model_id', how='inner')

        # groupby - sorting and column rename
        sql_groupby = join3.groupby('brand_name')['price'].agg(['count', 'sum']).sort_values(['count', 'sum'], ascending=False)
        df_final = sql_groupby.reset_index().rename(columns={'brand_name': 'vehicle_brand', 'count': 'n_sales', 'sum': 'total_value'})

        # file output
        df_final.to_csv(filename, index=False)


    def new_customers(self, filename):
        """
        Creates a report of customers who purchased a new vehicle after 1st January 2020
        Writes the report into a CSV file.

        Report fields:
        - customer_name: customer name
        - vehicle_brand: brand of the last purchased vehicle
        - vehicle_model: model of the last purchased vehicle
        - vehicle_year: year of the last purchased vehicle
        - sale_dt: sale date

        Sort by:
        - customer_name ascending

        :param str filename: Output file name
        """

        # get data from sqlite
        sales_df = pd.read_sql_query("select * from Sales", self.con)
        customers_df = pd.read_sql_query("select * from Customers", self.con)
        vehicles_df = pd.read_sql_query("select * from Vehicles", self.con)
        vehicle_models_df = pd.read_sql_query("select * from Vehicle_models", self.con)

        # join
        join1 = sales_df.merge(customers_df, left_on='customer_id', right_on='customer_id', how='inner')
        join2 = join1.merge(vehicles_df, left_on='vehicle_id', right_on='vehicle_id', how='inner')
        join3 = join2.merge(vehicle_models_df, left_on='vehicle_model_id', right_on='vehicle_model_id', how='inner')


        # date filtering
        filtered = join3[join3.sale_dt >= '2020-01-01']

        # rename columns
        df_final = filtered.reset_index().rename(
            columns={'count': 'n_sales', 'sum': 'total_value'})

        # file output
        df_final.to_csv(filename, index=False)



    def old_customers(self, filename):
        """
        Creates a report of customers who purchased the last vehicle before 1st January 2016
        Writes the report into a CSV file.

        Report fields:
        - customer_name: customer name
        - vehicle_brand: brand of the last purchased vehicle
        - vehicle_model: model of the last purchased vehicle
        - vehicle_year: year of the last purchased vehicle
        - sale_dt: sale date

        Sort by:
        - customer_name ascending

        :param str filename: Output file name
        """
        # TODO
        pass

    def next_vehicle(self, filename):
        """
        Creates a report of vehicles sold to customer who previously purchased another vehicle.
        Brakes the report by first vehicle brand.
        Writes the report into a CSV file.

        Report fields:
        - first_veh_brand: first vehicle brand
        - most_common_second_veh_brand: most common brand of the second vehicle purchased by the same customer
        - avg_days_between_sales: average number of days between the subsequent sales, rounded to nearest integer

        Sort by:
        - first_veh_brand ascending

        :param str filename: Output file name
        """
        # TODO
        pass


if __name__ == '__main__':

    test = ReportGenerator()
    # test.sales_by_brand('examplename.csv')

    test.new_customers('examplename.csv')