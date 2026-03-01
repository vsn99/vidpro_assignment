import sqlite3
import pandas as pd
import logging
from utils.utils import load_table, export_to_csv
from schema.CompanyXYZ_schema import DTYPES

DB_PATH = "vidpro.db"
OUTPUT_PATH = "output/output_pandas.csv"

class PandasSolution:
    def __init__(self):
        pass

    def load_tables(self, db_path: str):
        '''Uses function from utils to create dataframes for all 4 tables.'''
        conn = sqlite3.connect(db_path)

        orders = load_table(DB_PATH, "orders").astype(DTYPES["orders"])
        items = load_table(DB_PATH, "items").astype(DTYPES["items"])
        sales = load_table(DB_PATH, "sales").astype(DTYPES["sales"])
        customer = load_table(DB_PATH, "customer").astype(DTYPES["customer"])

        conn.close()
        return orders, items, sales, customer

    def compute_item_totals(
        self, 
        orders: pd.DataFrame,
        items: pd.DataFrame,
        sales: pd.DataFrame,
        customer: pd.DataFrame,
        min_age: int = 18,
        max_age: int = 35,
    ):
        """
        Compute total quantity of each item bought per customer within a specified age range.
        """

        orders_filtered = orders[
            (orders["quantity"].notna()) & (orders["quantity"] != 0)
        ] # Filter valid quantities

        orders_items = orders_filtered.merge(items, on="item_id", how="inner") # Join orders + items

        sales_customer = sales.merge(customer, on="customer_id", how="inner") # Join sales + customer

        sales_customer = sales_customer[
            (sales_customer["age"] >= min_age) &
            (sales_customer["age"] <= max_age)
        ] # Filter age range

        merged = orders_items.merge(sales_customer, on="sales_id", how="inner") # Final join

        result = (
            merged
            .groupby(["customer_id", "age", "item_name"], as_index=False)
            ["quantity"]
            .sum()
        ) # Group and aggregate

        result = result.rename(columns={
            "customer_id": "Customer",
            "age": "Age",
            "item_name": "Item",
            "quantity": "Quantity"
        }) # Rename columns

        return result

    def main(self):
        try:
            logging.debug(f"Starting Pandas Solution. {__name__}")
            orders, items, sales, customer = self.load_tables(DB_PATH)
            result_df = self.compute_item_totals(
                orders,
                items,
                sales,
                customer,
                min_age=18,
                max_age=35
            )
            export_to_csv(result_df, OUTPUT_PATH, delimiter=';')
            logging.debug(f"Pandas solution executed successfully. {__name__}")
        except Exception as e:
            logging.error(f"Error running Pandas solution: {e}")