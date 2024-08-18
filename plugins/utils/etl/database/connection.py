import logging
import sys
sys.path.append('/workspaces/etl-spotify')
from sqlalchemy import create_engine
from plugins.utils.etl.database.db import WarehouseConnection
from plugins.utils.etl.database.sde_config import get_warehouse_creds
import psycopg2

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

print(get_warehouse_creds())
def create_conn(
    connection_string=WarehouseConnection(
        get_warehouse_creds()
    ).connection_string(),
):
    # connect to the postgres database
    try:
        engine = create_engine(connection_string)
        logger.info("Connected to postgres database!!")
        return engine
    except Exception as e:
        logger.error("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        logger.error(f"Enable to connect to postgres : {e}")


def close_conn(engine):
    # close the connection
    engine.dispose()


print(create_conn())