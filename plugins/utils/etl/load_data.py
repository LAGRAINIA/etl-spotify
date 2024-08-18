import os 
import sys 
sys.path.append('/workspaces/etl-spotify')

from plugins.utils.etl.database.connection import close_conn, create_conn
import pandas as pd 
import logging



logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


def read_table(engine, table_name):
    """read data from the landing schema"""
    try:
        with engine.connect() as connection:
            result = connection.execute(f"SELECT DISTINCT TABLE_NAME FROM INFORMATION_SCHEMA.{table_name}")
            df = pd.DataFrame(result.fetchall(), columns=result.keys())
        logger.info('Table read from the landing_area!!!!')
        return df
    except Exception as e:
        logger.error('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        logger.error(f'Enable to read data from landing_area: {e}')


engine = create_conn()
print(read_table(engine=engine, table_name='COLUMNS'))
# with engine.connect() as connection:
#     result = connection.execute("SELECT * FROM landing_area")
#     df = pd.DataFrame(result.fetchall(), columns=result.keys())
#     print(df.head())
