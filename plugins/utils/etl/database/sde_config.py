import os 
import sys 

sys.path.append("/opt")
sys.path.append('/workspaces/etl-spotify')


from plugins.utils.etl.database.db import DBConnection
from dotenv import load_dotenv

# Recover env variables 
#load_dotenv(dotenv_path='/opt/.env')
load_dotenv()


def get_warehouse_creds() -> DBConnection:
    return DBConnection(
        user=os.getenv('POSTGRES_USER'),
        pwd=os.getenv('POSTGRES_PASSWORD'),
        database=os.getenv('POSTGRES_DB'),
        host=os.getenv('POSTGRES_HOST'),
        port=int(os.getenv('POSTGRES_PORT', 5432)),
    )


print(get_warehouse_creds())