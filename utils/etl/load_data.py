import os 
from database.connection import close_conn, create_conn
import pandas as pd 
import logging
from dotenv import load_dotenv

# Logger intitialization 
logging.basicConfig(format='[%(levelname)s]: %(message)s', level=logging.DEBUG)


# recover env variables 
load_dotenv()

# Database Location

engine = create_conn()



df = pd.read_sql_query(
            f'SELECT * FROM INFORMATION_SCHEMA.COLUMNS', engine
        )
