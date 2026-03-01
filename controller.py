import sys
from utils.utils import *
from sql_solution.run_sql_solution import SqlSolution
from pandas_solution.run_pandas_solution import PandasSolution

setup_logger()

class Controller:
    def __init__(self):
        pass

    def main(self):
        if sys.argv[1] == "sql":
            logging.debug(f"Starting application for {sys.argv[1]} solution.")
            SqlSolution().main()
            logging.debug(f"Done with {sys.argv[1]} solution.")
        elif sys.argv[1] == "pandas":
            logging.debug(f"Starting application for {sys.argv[1]} solution")
            PandasSolution().main()
            logging.debug(f"Done with {sys.argv[1]} solution.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        logging.error("Execution mode not provided. Use 'sql' or 'pandas'.")
        sys.exit(1)

    mode = sys.argv[1].lower()
    logging.info(f"Received execution mode: {mode}")

    if mode == "sql" or mode == "pandas":
        Controller().main()

    else:
        logging.error("Invalid mode. Use 'sql' or 'pandas'.")
        sys.exit(1)