import sqlite3
import pandas as pd
import logging
from utils.utils import read_query

DB_PATH = "vidpro.db"
QUERY_PATH = "sql_solution/query.sql"
OUTPUT_PATH = "output/output_sql.csv"

class SqlSolution:
    def __init__(self):
        pass

    def main(self):
        try:
            logging.debug(f"Starting SQL Solution. {__name__}")
            query = read_query(QUERY_PATH)
            conn = sqlite3.connect(DB_PATH)
            df = pd.read_sql_query(query, conn)
            conn.close()
            df.to_csv(OUTPUT_PATH, sep=";", index=False)
            logging.debug(f"SQL solution executed successfully. {__name__}")
        except Exception as e:
            logging.error("Error running SQL solution: ", e)