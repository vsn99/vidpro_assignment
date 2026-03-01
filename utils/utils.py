import sqlite3
import pandas as pd
import logging
import os

def load_table(db_path: str, table_name: str):
    """
    Load a single table from SQLite database.
    """
    query = f"SELECT * FROM {table_name}"

    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql_query(query, conn)

    return df


def export_to_csv(
    df: pd.DataFrame,
    output_path: str,
    delimiter: str = ","
):
    """
    Export DataFrame to CSV with configurable delimiter.
    """
    df.to_csv(output_path, sep=delimiter, index=False)


def read_query(path):
    with open(path, "r") as f:
        return f.read()
    
def setup_logger():
    env = os.getenv("APP_ENV", "dev").lower()

    if env == "prd" or env == "qa":
        level = logging.INFO
    else:
        level = logging.DEBUG

    logging.basicConfig(
        level=level,
        format="%(asctime)s,%(levelname)s,%(name)s,%(funcName)s,%(message)s",
        filename="simple_project.log",
        filemode="a",
    )