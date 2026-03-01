import sqlite3
import pandas as pd

DB_PATH = "vidpro.db"
QUERY_PATH = "sql_solution/query.sql"
OUTPUT_PATH = "output/output_sql.csv"

def read_query(path):
    with open(path, "r") as f:
        return f.read()

def main():
    try:
        query = read_query(QUERY_PATH)
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql_query(query, conn)
        conn.close()
        df.to_csv(OUTPUT_PATH, sep=";", index=False)
    except Exception as e:
        print("Error running SQL solution:", e)

if __name__ == "__main__":
    main()