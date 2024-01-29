import logging

import pandas as pd
from connection import close_conn, create_conn

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


def load_table_to_landing(df, engine, table_name):
    # load the csv file to the schema
    try:
        df.to_sql(
            table_name,
            engine,
            if_exists='replace',
            index=False,
            schema='landing_area',
        )
        logger.info("Table load to the landing area!!!")
    except Exception as e:
        logger.error("!!!!!!!!!!!!!!!!!!!!!!")
        logger.error(f"Enable to load the data to landing area : {e}")


if __name__ == "__main__":
    file_path = "dataset/Warehouse_and_Retail_Sales.csv"
    engine = create_conn()
    df = pd.read_csv(file_path)
    load_table_to_landing(df, engine, "Retail_sales")
    close_conn(engine)
