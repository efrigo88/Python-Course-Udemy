"""
Generates vehicle sales reports based on Sqlite database.
"""

import pandas as pd
import numpy as np
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
        join1 = sales_df.merge(vehicles_df,
                               left_on='vehicle_id',
                               right_on='vehicle_id',
                               how='inner')
        join2 = join1.merge(invoices_df,
                            left_on='invoice_id',
                            right_on='invoice_id',
                            how='inner')
        join3 = join2.merge(vehicle_models_df,
                            left_on='vehicle_model_id',
                            right_on='vehicle_model_id',
                            how='inner')

        # group by, aggregation and sorting
        sql_group_by = join3.groupby('brand_name')['price']\
            .agg(['count', 'sum'])\
            .sort_values(['count', 'sum'], ascending=False)

        # rename columns
        renamed = sql_group_by.reset_index()\
            .rename(columns={'brand_name': 'vehicle_brand',
                             'count': 'n_sales',
                             'sum': 'total_value'})

        # csv file output
        renamed.to_csv(filename, index=False)

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
        join1 = sales_df.merge(customers_df,
                               left_on='customer_id',
                               right_on='customer_id',
                               how='inner')
        join2 = join1.merge(vehicles_df,
                            left_on='vehicle_id',
                            right_on='vehicle_id',
                            how='inner')
        join3 = join2.merge(vehicle_models_df,
                            left_on='vehicle_model_id',
                            right_on='vehicle_model_id',
                            how='inner')

        # select desired columns from the whole
        desired_columns = join3[['customer_name',
                                 'brand_name',
                                 'model_name',
                                 'vehicle_year',
                                 'sale_dt']]

        # rename columns
        renamed = desired_columns\
            .rename(columns={'brand_name': 'vehicle_brand',
                             'model_name': 'vehicle_model'})

        # date filtering and sorting
        filtered = renamed[renamed.sale_dt >= '2020-01-01']\
            .sort_values('customer_name')

        # csv file output
        filtered.to_csv(filename, index=False)

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

        # get data from sqlite
        # bring sales directly filtered by date
        sales_df = pd.read_sql_query("select * from Sales where sale_dt < '2016-01-01'", self.con)
        #
        customers_df = pd.read_sql_query("select * from Customers", self.con)
        vehicles_df = pd.read_sql_query("select * from Vehicles", self.con)
        vehicle_models_df = pd.read_sql_query("select * from Vehicle_models", self.con)

        # auxiliary df to get max sale_id for every client
        aux = sales_df.groupby('customer_id')['sale_id']\
            .agg('max').reset_index()\
            .rename(columns={'sale_id': 'last_sale_id'})

        # necessary joins
        sales_customers = sales_df.merge(customers_df,
                                         left_on='customer_id',
                                         right_on='customer_id',
                                         how='inner')

        sales_cust_veh = sales_customers.merge(vehicles_df,
                                               left_on='vehicle_id',
                                               right_on='vehicle_id',
                                               how='inner')

        sales_cust_veh_vm = sales_cust_veh.merge(vehicle_models_df,
                                                 left_on='vehicle_model_id',
                                                 right_on='vehicle_model_id',
                                                 how='inner')

        reduced_df = sales_cust_veh_vm.merge(aux,
                                             left_on=['customer_id', 'sale_id'],
                                             right_on=['customer_id', 'last_sale_id'],
                                             how='inner')

        # column selection / column rename / sorting by desired column
        final_df = reduced_df[['customer_name',
                               'brand_name',
                               'model_name',
                               'vehicle_year',
                               'sale_dt']]\
            .rename(columns={'brand_name': 'vehicle_brand',
                             'model_name': 'vehicle_model'})\
            .sort_values('customer_name')

        # csv file output
        final_df.to_csv(filename, index=False)

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

        # get data from sqlite
        sales_df = pd.read_sql_query("select * from Sales", self.con)
        vehicles_df = pd.read_sql_query("select * from Vehicles", self.con)
        vehicle_models_df = pd.read_sql_query("select * from Vehicle_models", self.con)

        # auxiliary df to get clients who have bought more than one car
        aux0 = sales_df.groupby('customer_id')['vehicle_id'] \
            .agg('count').reset_index() \
            .rename(columns={'vehicle_id': 'cars_bought'})
        aux = aux0[aux0.cars_bought != 1]

        # necessary joins
        sales_veh = sales_df.merge(vehicles_df,
                                   left_on='vehicle_id',
                                   right_on='vehicle_id',
                                   how='inner')

        sales_veh_vehm = sales_veh.merge(vehicle_models_df,
                                         left_on='vehicle_model_id',
                                         right_on='vehicle_model_id',
                                         how='inner')

        filtered_df = sales_veh_vehm.merge(aux,
                                           left_on='customer_id',
                                           right_on='customer_id',
                                           how='inner')

        # keep columns I need / sorting
        reduced_df = filtered_df[['customer_id',
                                  'brand_name',
                                  'sale_dt']]\
            .sort_values(['customer_id', 'sale_dt'])

        # persists the data to calculate RANK in sqlite, I couldn't
        # do it using pandas
        reduced_df.to_sql("reduced_df_method4",
                          self.con,
                          if_exists="replace",
                          index=False)

        ranked_df = pd.read_sql_query("select * "
                                      "from (SELECT brand_name,"
                                      "sale_dt,"
                                      "RANK() OVER (PARTITION BY "
                                      "customer_id "
                                      "ORDER BY sale_dt) AS ranked "
                                      "FROM reduced_df_method4) "
                                      "where ranked < 3", self.con)

        # get next rows values for 2 cols (win function: lead)
        ranked_df["next_brand_name"] = ranked_df.brand_name.shift(-1)
        ranked_df["next_sale_dt"] = ranked_df.sale_dt.shift(-1)

        # first cleaning
        df_purged = ranked_df[ranked_df.ranked != 2]

        # col casting, here lies the warning issue!!!
        df_purged['sale_dt'] = pd.to_datetime(df_purged['sale_dt'])
        df_purged['next_sale_dt'] = pd.to_datetime(df_purged['next_sale_dt'])

        # date diff calculation
        df_purged["avg_days_between_sales"] = \
            df_purged["next_sale_dt"] - df_purged["sale_dt"]
        df_purged["avg_days_between_sales"] = \
            df_purged["avg_days_between_sales"] / np.timedelta64(1, 'D')

        # column selection / column rename / sorting by desired column
        final_df = df_purged[['brand_name',
                              'next_brand_name',
                              'avg_days_between_sales']] \
            .rename(columns={'brand_name': 'first_veh_brand',
                             'next_brand_name': 'most_common_second_veh_brand'}) \
            .sort_values('avg_days_between_sales', ascending=False)

        # csv file output
        final_df.to_csv(filename, index=False)


if __name__ == '__main__':

    test = ReportGenerator()

    # test output
    test.sales_by_brand('sales_by_brand.csv')
    test.new_customers('new_customers.csv')
    test.old_customers('old_customers.csv')
    test.next_vehicle('next_vehicle.csv')
